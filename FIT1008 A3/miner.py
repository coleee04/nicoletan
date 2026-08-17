from __future__ import annotations
from typing import Iterable

from data_structures import *
from minecraft_block import MinecraftBlock


class Miner:
    """
    A class representing a miner in a mining simulation.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the miner with a name and an empty inventory.
        Args:
            name (str): The name of the miner.
        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Assigning variables and creating an empty inventory ArrayList is a constant time operation.
        """
        self.name = name
        self.inventory = ArrayList()

    def mine(self, block: MinecraftBlock) -> None:
        """
        Mines a block and adds the item to the miner's bag.

        Args:
            block (MinecraftBlock): The block to be mined.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Appending to ArrayList is constant time operation to add to the end of the list
        """
        self.inventory.append(block.item)

    def clear_inventory(self) -> Iterable:
        """
        Clears the miner's inventory and returns what he had in the inventory before the clear.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Save current inventory as old_inventory and start a new empty one
            Only quick assignments
        """
        old_inventory = self.inventory
        self.inventory = ArrayList()
        return old_inventory

    def __str__(self) -> str:
        return f"Miner: {self.name}"
