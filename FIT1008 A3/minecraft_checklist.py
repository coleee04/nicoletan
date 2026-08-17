from __future__ import annotations
from data_structures import *
from minecraft_block import MinecraftBlock
from betterbst import BetterBST
from algorithms.mergesort import mergesort
from typing import Optional


class MinecraftChecklist:
    def __init__(self, blocks: ArrayR[MinecraftBlock]) -> None:
        """
        Initializes the MinecraftChecklist instance with a list of blocks.

        Complexity:
            Best Case Complexity: O(NlogN)
            Worst Case Complexity: O(NlogN)

        Justification:
            N = number of blocks in checklist
            Sorting and building the Binary Search Tree takes O(NlogN) time complexity.
        """
        elements = ArrayList()
        for i in range(len(blocks)):
            block = blocks[i]
            ratio = block.item.value / block.hardness
            key = (ratio, id(block))
            elements.append((key, block))

        self.checklist = BetterBST(elements)

    def __contains__(self, item: MinecraftBlock) -> bool:
        """
        Checks if the item is in the checklist.

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)
        
        Justification:
            N = number of blocks in checklist
            The for loop iterates through all nodes in the checklist to find the item.
        """
        ratio = item.item.value / item.hardness if item.hardness != 0 else float('inf')
        key = (ratio, id(item)) 
        return key in self.checklist

    def __len__(self) -> int:
        """
        Returns the number of blocks in the checklist.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            The length of checklist is stored and can be accessed in constant time.
        """
        return len(self.checklist)

    def add_block(self, block: MinecraftBlock, key: Optional[tuple] = None) -> None:
        """
        Adds a block to the checklist.

        Complexity:
            Best Case Complexity: O(logN)
            Worst Case Complexity: O(logN)
        Justification:
            N = number of blocks in checklist
            Inserting into BetterBST takes O(logN) time complexity.
        """
        if key is None:
            ratio = block.item.value / block.hardness if block.hardness != 0 else float('inf')
            key = (ratio, id(block))
        if key not in self.checklist:
            self.checklist[key] = block

    def remove_block(self, block: MinecraftBlock) -> None:
        """
        Removes a block from the checklist.

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)

        Justification:
            N = number of blocks in checklist
            The for loop iterates through all nodes in the checklist to find and remove the block.
            Deletion is O(logN) in BetterBST, but dominated by for loop complexity (O(N)).
        """
        for node in self.checklist:
            if node.item.item == block.item and node.item.hardness == block.hardness:
                del self.checklist[node.key]
                return

    def get_sorted_blocks(self) -> ArrayR[MinecraftBlock]:
        """
        Returns the sorted blocks in the checklist.
        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)

        Justification:
            N = number of blocks in checklist
            Keys are already sorted in the BetterBST
            Iterates through and build a sorted array in O(N) time complexity.

        """
        # Create a copy of  checklist
        copied = ArrayList[MinecraftBlock]()
        for node in self.checklist:
            copied.append(node.item)

        # Sort by ratio (value / hardness), descending
        def ratio(block: MinecraftBlock):
            return block.item.value / block.hardness if block.hardness != 0 else float('inf')

        mergesort(copied, key=ratio)

        sorted_blocks = ArrayR(len(copied))
        for i in range(len(copied)):
            sorted_blocks[i] = copied[i]

        return sorted_blocks

    def get_optimal_blocks(self, block1: MinecraftBlock, block2: MinecraftBlock) -> ArrayR[MinecraftBlock]:
        """
        Returns the optimal blocks between two given blocks.
        
        Criteria 1:
            - Optimal blocks have a ratio of value to mining time more than the same ratio for block1.
        Criteria 2:
            - Optimal blocks have a ratio of value to mining time less than the same ratio for block2.
        
        Args:
            block1 (MinecraftBlock): The first block.
            block2 (MinecraftBlock): The second block.
        
        Returns:
            ArrayR: An array of optimal blocks between the two given blocks.
        
        Complexity:
            Best Case Complexity: O(logN)
            Worst Case Complexity: O(N)
        
        Justification:
            N = number of blocks in checklist
            O(log N) if very few matches to be filtered
            O(N) if full traversal is needed
        """
        ratio1 = block1.item.value / block1.hardness
        ratio2 = block2.item.value / block2.hardness

        # Filter functions to check ratios
        def fil_func1(key):
            return key[0] > ratio1
        def fil_func2(key):
            return key[0] < ratio2
        
        # Get filtered pairs of (key, block) 
        pair = self.checklist.filter_keys(fil_func1, fil_func2)

        # Manual selection sort on pair
        n = len(pair)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if pair[j][0] < pair[min_idx][0]:
                    min_idx = j
            # Swap pair[i] and pair[min_idx]
            pair[i], pair[min_idx] = pair[min_idx], pair[i]

        # Building the result array
        optimal_blocks = ArrayR(len(pair))
        for i in range(len(pair)):
            optimal_blocks[i] = pair[i][1]
            
        return optimal_blocks