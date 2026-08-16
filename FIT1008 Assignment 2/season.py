from __future__ import annotations
from data_structures.array_set import ArraySet
from data_structures.referential_array import ArrayR
from data_structures.array_list import ArrayList
from enums import TeamGameResult
from game_simulator import GameSimulator, GameSimulationOutcome
from dataclasses import dataclass
from team import Team


@dataclass
class Game:
    """
    Simple container for a game between two teams.
    Both teams must be team objects, there cannot be a game without two teams.

    Note: Python will automatically generate the init for you.
    Use Game(home_team: Team, away_team: Team) to use this class.
    See: https://docs.python.org/3/library/dataclasses.html

    Do not make any changes to this class.
    """
    home_team: Team = None
    away_team: Team = None


class WeekOfGames:
    """
    Simple container for a week of games.

    A fixture must have at least one game.
    """

    def __init__(self, week: int, games: ArrayR[Game] | ArrayList[Game]) -> None:
        """
        Container for a week of games.

        Args:
            week (int): The week number.
            games (ArrayR[Game]): The games for this week.
        
        No complexity analysis is required for this function.
        Do not make any changes to this function.
        """
        self.games = games
        self.week: int = week

    def __iter__(self):
        """
        Complexity:

            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            # Set index to 0

        """
        self._index = 0
        return self

    def __next__(self):
        """
        Complexity:

            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            # Check for the index, return the result

        """
        if self._index >= len(self.games):
            raise StopIteration
        result = self.games[self._index]
        self._index += 1
        return result


class Season:

    def __init__(self, teams: ArrayR[Team] | ArrayList[Team]) -> None:
        """
        Initializes the season with a schedule.

        Args:
            teams (ArrayR[Team]): The teams played in this season.

        Complexity:

            Best Case Complexity: O(N^2)
            Worst Case Complexity: O(N^2)
            # N = number of teams
            # Dominated by _generate_schedule() which is O(N^2)

        """
        self.teams = teams

        self.leaderboard = ArrayList(len(teams)) # An ArrayList to store the leaderboard
        for team in teams:
            self.leaderboard.append(team) # Append (team, points) to the leaderboard
            # Each team are initialized with 0 points

        self.schedule = ArrayList() # An ArrayList to store the schedule of the season
        wks_of_games = self._generate_schedule() # Generate the schedule of the season
        for i in range(len(wks_of_games)):
            self.schedule.append(WeekOfGames(i+1, wks_of_games[i])) 

    def _generate_schedule(self) -> ArrayList[ArrayList[Game]]:
        """
        Generates a schedule by generating all possible games between the teams.

        Return:
            ArrayList[ArrayList[Game]]: The schedule of the season.
                The outer array is the weeks in the season.
                The inner array is the games for that given week.

        Complexity:
            Best Case Complexity: O(N^2) where N is the number of teams in the season.
            Worst Case Complexity: O(N^2) where N is the number of teams in the season.
        
        Do not make any changes to this function.
        """
        num_teams: int = len(self.teams)
        weekly_games: ArrayList[ArrayList[Game]] = ArrayList()
        flipped_weeks: ArrayList[ArrayList[Game]] = ArrayList()
        games: ArrayList[Game] = ArrayList()

        # Generate all possible matchups (team1 vs team2, team2 vs team1, etc.)
        for i in range(num_teams):
            for j in range(i + 1, num_teams):
                games.append(Game(self.teams[i], self.teams[j]))

        # Allocate games into each week ensuring no team plays more than once in a week
        week: int = 0
        while games:
            current_week: ArrayList[Game] = ArrayList()
            flipped_week: ArrayList[Game] = ArrayList()
            used_teams: ArraySet = ArraySet(len(self.teams))

            week_game_no: int = 0
            for game in games:
                if game.home_team.name not in used_teams and game.away_team.name not in used_teams:
                    current_week.append(game)
                    used_teams.add(game.home_team.name)
                    used_teams.add(game.away_team.name)

                    flipped_week.append(Game(game.away_team, game.home_team))
                    games.remove(game)
                    week_game_no += 1

            weekly_games.append(current_week)
            flipped_weeks.append(flipped_week)
            week += 1

        for flipped_week in flipped_weeks:
            weekly_games.append(flipped_week)
        
        return weekly_games

    def simulate_season(self) -> None:
        """
        Simulates the season.

        Complexity:
            Assume GameSimulator.simulate() is O(1)
            Remember to define your variables in your complexity.

            Let T = number of teams 
            Let P = number of players per team

            Each team plays against every other team once in the season, so we will have T^2 games in total (T^2 from T*(T-1)/2)
            For each game T*P steps are required to update for all players in the game.
            Total complexity is O(T^2 * T * P) = O(T^3 * P)

            Best Case Complexity: O(T^3 * P)
            Worst Case Complexity: O(T^3 * P)

            Best and Worst case complexity is the same because it always does the same number of steps for each game no matter how

        """
        for week in self.schedule: # Go through every week in the schedule
            for game in week: # For each game in the week
                result = GameSimulator.simulate(game.home_team, game.away_team) # Simulate the game

                if result.home_goals > result.away_goals: # If home team got more goals than away team
                    game.home_team.add_result(TeamGameResult.WIN) 
                    game.away_team.add_result(TeamGameResult.LOSS)
                elif result.home_goals < result.away_goals: # If home team got less goals than away team
                    game.home_team.add_result(TeamGameResult.LOSS)
                    game.away_team.add_result(TeamGameResult.WIN)
                else: # If both home team and away team got same goals
                    game.home_team.add_result(TeamGameResult.DRAW)
                    game.away_team.add_result(TeamGameResult.DRAW)
                
                # Update the leaderboard with the points of each team
                # Home team
                for i in range(len(self.leaderboard)):
                    if self.leaderboard[i] == game.home_team: # If team is the home team
                        self.leaderboard.delete_at_index(i)
                        break

                # Find new position from the updated points of the home team
                index_to_insert_ht = 0
                while (index_to_insert_ht < len(self.leaderboard) and self.leaderboard[index_to_insert_ht].points >= game.home_team.points):
                    index_to_insert_ht += 1
                self.leaderboard.insert(index_to_insert_ht, game.home_team) # Insert the home team in the leaderboard

                # Away team
                for i in range(len(self.leaderboard)):
                    if self.leaderboard[i] == game.away_team: # If team is the away team
                        self.leaderboard.delete_at_index(i)
                        break

                # Find new position from the updated points of the home team
                index_to_insert_at = 0
                while (index_to_insert_at < len(self.leaderboard) and self.leaderboard[index_to_insert_at].points >= game.away_team.points):
                    index_to_insert_at += 1
                self.leaderboard.insert(index_to_insert_at, game.away_team) # Insert the away team in the leaderboard

                # Update player that score goals
                for scorer in result.goal_scorers:
                    found = False
                    for team in self.teams:
                        for player in team.get_players():
                            if player.name == scorer:
                                player.goals += 1
                                found = True
                                break
                        if found:
                            break
        


    def delay_week_of_games(self, orig_week: int, new_week: int | None = None) -> None:
        """
        Delay a week of games from one week to another.

        Args:
            orig_week (int): The original week to move the games from.
            new_week (int or None): The new week to move the games to. If this is None, it moves the games to the end of the season.

        Complexity:

            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)
            # N = number of weeks in the season

        """
        wk_to_move = self.schedule[orig_week - 1] # Get the week to move
        self.schedule.delete_at_index(orig_week - 1) # Remove week from schedule

        if new_week is None: # If new_week is None, move the week to the end of the season
            self.schedule.append(wk_to_move)
        else: 
            self.schedule.insert(new_week - 1, wk_to_move)

    def __len__(self) -> int:
        """
        Returns the number of teams in the season.

        Complexity:

            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            # Return the length of the teams list

        """
        return len(self.teams)

    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the season object.

        Complexity:
            Analysis not required.
        """
        return ""

    def __repr__(self) -> str:
        """Returns a string representation of the Season object.
        Useful for debugging or when the Season is held in another data structure."""
        return str(self)
