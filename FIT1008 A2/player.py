from __future__ import annotations
from enums import PlayerPosition
from data_structures import ArrayList

# Do not change the import statement below
# If you need more modules and classes from datetime, do not use
# separate import statements. Use them from datetime like this:
# datetime.datetime, or datetime.date, etc.
import datetime


class Player:

    def __init__(self, name: str, position: PlayerPosition, age: int) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (PlayerPosition): The position of the player
            age (int): The age of the player

        Complexity:

            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            # Assignments and initializations are constant time operations.

        """
        self.name = name
        self.position = position
        # Since age changes every year, we store the birth year of the player instead
        current_year = datetime.date.today().year
        self.birth_year = current_year - age
        self.goals = 0 # Number of goals scored by the player, initialized to 0
        self.stats = ArrayList() 

    def reset_stats(self) -> None:
        """
        Reset the stats of the player.
        
        This doesn't delete the existing stats, but resets them to 0.
        I.e. all stats that were previously set should still be available, with a value of 0.

        Complexity:

            Best Case Complexity: O(1)
            # When self.stats.__len__ is 0, the loop will not run and the function will return immediately.
            
            Worst Case Complexity: O(N)
            # N = number of stats, the loop run N times to reset each stat to 0.
        
        """
        for index in range(self.stats.__len__()):
            stat_name = self.stats[index][0]
            stat_value = self.stats[index][1]
            self.stats[index] = (stat_name, 0)
            # Keeping stat_name, stat_value reset to 0

    def __setitem__(self, statistic: str, value: int) -> None:
        """
        Set the given value for the given statistic for the player.

        Args:
            statistic (string): The key of the stat
            value (int): The value of the stat

        Complexity:

            Best Case Complexity: O(1)
            # Statistic argument is found at first place (i.e. index 0) of self.stats, value is updated directly.
            
            Worst Case Complexity:O(N)
            # N = number of stats
            # Statistic is found at last position of self.stats, or not found at all.
        
        """
        for index in range(self.stats.__len__()):
            stat_name = self.stats[index][0]
            stat_value = self.stats[index][1]
            if stat_name == statistic:
                self.stata[index] = (stat_name, value) # Update the stat by replacing the whole tuple
                return
        self.stats.append((statistic, value)) # Add new stat if not found

    def __getitem__(self, statistic: str) -> int:
        """
        Get the value of the player's stat based on the passed key.

        Args:
            statistic (str): The key of the stat

        Returns:
            int: The value of the stat

        Complexity:

            Best Case Complexity: O(1)
            # Statistic argument is found at first place (i.e. index 0) of self.stats, value is updated directly.
            
            Worst Case Complexity:O(N)
            # N = number of stats
            # Statistic is found at last position of self.stats, or not found at all.
        
        """
        for index in range(self.stats.__len__()):
            stat_name = self.stats[index][0]
            stat_value = self.stats[index][1]
            if stat_name == statistic:
                return stat_value # Return value of stat if found
        raise KeyError(f"Statistic '{statistic}' not found.") # Raise KeyError if stat not found

    def get_age(self) -> int:
        """
        Get the age of the player

        Returns:
            int: The age of the player

        Complexity:

            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            # Constant time operation to get the current year and subtract the birth year.
        
        """
        current_year = datetime.date.today().year
        return current_year - self.birth_year

    def __str__(self) -> str:
        """
        Optional but highly recommended.

        You may choose to implement this method to help you debug.
        However your code must not rely on this method for its functionality.

        Returns:
            str: The string representation of the player object.

        Complexity Analysis not required.
        """
        return "...String Representation of Player..."

    def __repr__(self) -> str:
        """ String representation of the Player object.
        Useful for debugging or when the Player is held in another data structure.
        """
        return str(self)
