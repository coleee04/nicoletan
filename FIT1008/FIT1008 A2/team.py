from __future__ import annotations

from data_structures.referential_array import ArrayR
from data_structures.array_list import ArrayList
from data_structures.circular_queue import CircularQueue
from data_structures.hash_table_separate_chaining import HashTableSeparateChaining
from enums import TeamGameResult, PlayerPosition
from player import Player
from typing import Collection, TypeVar

T = TypeVar("T")


class Team:
    def __init__(self, team_name: str, initial_players: ArrayR[Player], history_length: int) -> None:
        """
        Constructor for the Team class

        Args:
            team_name (str): The name of the team
            initial_players (ArrayR[Player]): The players the team starts with initially
            history_length (int): The number of `GameResult`s to store in the history

        Returns:
            None

        Complexity:

            Best Case Complexity: O(N)            
            Worst Case Complexity: O(N)
            # N = number of initial players, each initial player must be added once to the team.

        """
        self.name = team_name 
        self.history_length = history_length 
        self.points = 0 # Initialise points to 0

        # Create an ArrayR to store positions of players (Goalkeeper, Defender, Midfielder, Striker)
        self.players = ArrayR(4) 

        for i in range(4):
            self.players[i] = ArrayList() # Create an empty ArrayList for each position

        for i in range(len(initial_players)):
            player = initial_players[i] # Get the player from the initial players
            position_idx = self.get_position_index(player.position) # Get the index of the player's position
            self.players[position_idx].append(player)

        self.history = None # Game history
        self.posts = None # Blog posts

    def get_position_index(self, position: PlayerPosition) -> int:
        """
        Returns the index of the player's position

        Args:
            position (PlayerPosition): The position to get the index for

        Returns:
            int: The index of the position in the players ArrayR
        """
        if position == PlayerPosition.GOALKEEPER:
            return 0
        elif position == PlayerPosition.DEFENDER:
            return 1    
        elif position == PlayerPosition.MIDFIELDER:
            return 2    
        elif position == PlayerPosition.STRIKER:
            return 3

    def add_player(self, player: Player) -> None:
        """
        Adds a player to the team.

        Args:
            player (Player): The player to add

        Returns:
            None

        Complexity:

            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            # Complexity of ArrayList append is O(1)

        """
        position_idx = self.get_position_index(player.position) # Get the index of the player's position
        self.players[position_idx].append(player) # Add player to the respective position

    def remove_player(self, player: Player) -> None:
        """
        Removes a player from the team.

        Args:
            player (Player): The player to remove

        Returns:
            None

        Complexity:

            Best Case Complexity: O(N)
            # N = number of players in that position
            # Best case when player is found at index 0

            Worst Case Complexity: O(N)
            # Worst case when player is last or not found, N checks is needed to find the player
        
        """
        position_idx = self.get_position_index(player.position)
        # Get position's Array List
        position_lst = self.players[position_idx]
        for i in range(len(position_lst)):
            if position_lst[i] == player:
                position_lst.delete_at_index(i) # Remove player from the position's Array List
                return
        raise ValueError("Player not found.") # Raise error if player not found

    def get_players(self, position: PlayerPosition | None = None) -> Collection[Player]:
        """
        Returns the players of the team that play in the specified position.
        If position is None, it should return ALL players in the team.
        You may assume the position will always be valid.
        Args:
            position (PlayerPosition or None): The position of the players to return

        Returns:
            Collection[Player]: The players that play in the specified position
            held in a valid data structure provided to you within
            the data_structures folder.
            
            This includes the ArrayR, which was previously prohibited.

        Complexity:

            Best Case Complexity: O(N)/O(M)
            Worst Case Complexity: O(N)/O(M)
            # N = maximum number of players in a position (if position is not None)
            # M = total number of players in the team (if position is None)
            # Linear complexity for both best and worst case as we need to copy all players
                  
        """
        pos_players = ArrayList() # An ArrayList to store players with the specified position
        
        if position is not None:
            # Get players for the specified position
            idx = self.get_position_index(position)
            for i in range(len(self.players[idx])):
                pos_players.append(self.players[idx][i])
        else:
            # Get players for all positions
            for i in range(len(self.players)):
                for j in range(len(self.players[i])):
                    pos_players.append(self.players[i][j]) 
        return pos_players
        
    def add_result(self, result: TeamGameResult) -> None:
        """
        Add the `result` to this `Team`'s history

        Args:
            result (GameResult): The result to add
            
        Complexity:

            Best Case Complexity: O(1)
            # If history size is less than limit, we can append the result directly
            
            Worst Case Complexity:  O(N)
            # N = history_length
            # If history is full, oldest result at index 0 must be removed, N-1 elements shifted in front

        """
        if self.history is None:
            self.history = ArrayList() # Create a ArrayList for the history

        if len(self.history) >= self.history_length: 
            self.history.delete_at_index(0) # Remove oldest result
        
        self.history.append(result) # Add the new result to the history

        self.points += result.value # Update the points based on the result

    def get_history(self) -> Collection[TeamGameResult] | None:
        """
        Returns the `GameResult` history of the team.
        If the team has played less than this team's `history_length`,
        return all the result of all the games played so far.

        For example:
        If a team has only played 4 games and they have:
        Won the first, lost the second and third, and drawn the last,
        the result should be a container with 4 objects in this order:
        [GameResult.WIN, GameResult.LOSS, GameResult.LOSS, GameResult.DRAW]

        If this method is called before the team has played any games,
        return None the reason for this is explained in the specification.

        Returns:
            Collection[GameResult]: The most recent `GameResult`s for this team
            or
            None if the team has not played any games.

        Complexity:

            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)
            # N = number of items in the history
            # All items in history is copied to the new ArrayList

        """
        if self.history is None or len(self.history) == 0:
            return None
        
        history_arr = ArrayList() # An ArrayList to store the history of results

        for i in range(len(self.history)):
            history_arr.append(self.history[i])
        return history_arr
    
    def make_post(self, post_date: str, post_content: str) -> None:
        """
        Publish a team blog `post` for a particular `post_date`.
       
        A `Team` can have one published post per day. Any duplicate
        posts should overwrite the original post for that day.
        
        Args:
            `post_date` (`str`) - The date of the post
            `post_content` (`str`) - The content of the post
        
        Returns:
            None

        Complexity:

            Best Case Complexity: O(1)
            # Inserting into a HashTable is O(1) 

            Worst Case Complexity: O(N)
            # N = number of posts in the HashTable
            # All posts are hashed to the same index, many collisions occur
            # Need to traverse the linked list to find the post

        """
        if self.posts is None:
            self.posts = HashTableSeparateChaining() # Create a HashTable for the posts
        self.posts[post_date] = post_content # Add the post to the HashTable

    def __len__(self) -> int:
        """
        Returns the number of players in the team.

        Complexity:

            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            # The length of the team is O(1) for each iteration

        """
        total_num = 0 # Initialise total number of players to 0
        for i in range(len(self.players)):
            total_num += len(self.players[i])
        return total_num
    
    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the team object.

        Complexity analysis not required.
        """
        return ""

    def __repr__(self) -> str:
        """Returns a string representation of the Team object.
        Useful for debugging or when the Team is held in another data structure.
        """
        return str(self)
