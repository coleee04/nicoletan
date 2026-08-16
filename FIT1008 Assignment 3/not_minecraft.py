from __future__ import annotations
from cave_system import *
from data_structures import *
from data_structures.array_stack import ArrayStack
from minecraft_block import MinecraftBlock
from minecraft_checklist import MinecraftChecklist
from random_gen import RandomGen
from miner import Miner
from algorithms.mergesort import mergesort


class NotMinecraft:
    """
    A class representing a NotMinecraft game.
    """

    def __init__(self, cave_system: CaveSystem, checklist: MinecraftChecklist) -> None:
        """
        Initializes the NotMinecraft game.

        Args:
            cave_system (CaveSystem): The cave system for the game.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)

        Justification:
            Assignment of instance variables takes constant time complexity.
        """
        self.cave_system = cave_system
        self.checklist = checklist
        self.miner = Miner("Steve")

    def dfs_explore_cave(self) -> ArrayList[MinecraftBlock]:
        """
        Performs a depth-first search (DFS) to explore the cave system and collect blocks.
        Returns:
            ArrayList[MinecraftBlock]: A list of collected blocks.
        Complexity:
            Not required
        """
        blocks = ArrayList[MinecraftBlock]()
        stack = ArrayStack(len(self.cave_system) * 2)
        visited = ArrayList[CaveNode]()
        start_cave = self.cave_system.entrance

        if start_cave is None:
            return blocks

        # Start DFS from the first cave
        stack.push(start_cave)

        while not stack.is_empty():
            current_cave = stack.pop()

            # Check if alr visited
            alr_visited = False
            for i in range(len(visited)):
                if visited[i] == current_cave:
                    alr_visited = True
                    break
            if alr_visited:
                continue

            visited.append(current_cave)

            for i in range(len(current_cave.blocks)):
                block = current_cave.blocks[i]
                blocks.append(block)

            for i in range(len(current_cave.neighbours)-1, -1, -1):
                    stack.push(current_cave.neighbours[i])

        return blocks

    def objective_mining_filter(self, blocks: ArrayList[MinecraftBlock], block1: MinecraftBlock,
                                block2: MinecraftBlock) -> ArrayList:
        """
        Given a list of blocks, filter the blocks that should be considered according to scenario 1.
        
        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
            block1 (MinecraftBlock): Filtered blocks should have a ratio of value to mining time > block1.
            block2 (MinecraftBlock): Filtered blocks should have a ratio of value to mining time < block2.
        
        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)

        Justification:
            N = Number of blocks in the given list
            Iterating through and filter the list of blocks based on the mining time and value ratio
        """
        filtered_blocks = ArrayList[MinecraftBlock]()
        
        ratio1 = block1.item.value / block1.hardness if block1.hardness != 0 else float('inf')
        ratio2 = block2.item.value / block2.hardness if block2.hardness != 0 else float('inf')

        lower = min(ratio1, ratio2)
        upper = max(ratio1, ratio2)

        for i in range(len(blocks)):
            block = blocks[i]
            ratio = block.item.value / block.hardness if block.hardness != 0 else float('inf')
            
            if lower < ratio < upper:
                filtered_blocks.append(block)
        
        return filtered_blocks

    def objective_mining(self, blocks: ArrayList[MinecraftBlock]) -> None:
        """
        Mines the cave system to achieve the objective of collecting blocks.

        Complexity:
            Best Case Complexity: O(M)
            Worst Case Complexity: O(M * N)

        Justification:
            M = Number of blocks from DFS
            N = Number of blocks in self.checklist
            Traverses through checklist for every M blocks.
            Best case if no M blocks are in the checklist, then O(M).
            Worst case if all M blocks are in the checklist, remove_block takes O(N), then O(M * N)
        """
        def get_key(block: MinecraftBlock):
            ratio = block.item.value / block.hardness if block.hardness != 0 else float('inf')
            return (-ratio, id(block))

        # Collect blocks to mine based on checklist
        to_mine = ArrayList()
        for i in range(len(blocks)):
            block = blocks[i]

            if block in self.checklist:
                to_mine.append(block)

        # Sort the to_mine list
        to_mine = mergesort(to_mine, key=get_key)

        # Mine each block in order

        for i in range(len(to_mine)):
            block = to_mine[i]
 
            self.miner.mine(block)
            self.checklist.remove_block(block)

    def objective_mining_summary(self, blocks: ArrayList[MinecraftBlock], block1: MinecraftBlock,
                                 block2: MinecraftBlock) -> None:
        """
        Returns the summary of the objective mining.
        This is to explain how objective mining will be called and tested.
        Complexity:
            Not Required
        """
        filtered_blocks = self.objective_mining_filter(blocks, block1, block2)

        self.chicken_jockey_attack(filtered_blocks)

        self.objective_mining(filtered_blocks)

    def profit_mining(self, blocks: ArrayList[MinecraftBlock], time_in_seconds: int) -> None:
        """
        Mines the cave system casually.

        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
            time_in_seconds (int): The time in seconds to mine.

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N^2)

        Justification:
            N = number of blocks in the input list
            Best case when time runs out after a few swaps, exiting early, O(N).
            Worst case when all blocks are sorted by ratio, O(N^2) due to nested loops for sorting.
        """
        time_used = 0

        while time_used < time_in_seconds:
            best_index = -1
            best_ratio = -1

            for i in range(len(blocks)):
                block = blocks[i]
                if block.hardness + time_used <= time_in_seconds:
                    ratio = block.item.value / block.hardness
                    if ratio > best_ratio:
                        best_ratio = ratio
                        best_index = i

            if best_index == -1:
                break  # No more block can be mined in the time left

            block = blocks.delete_at_index(best_index)
            self.miner.mine(block)
            time_used += block.hardness

    
    def chicken_jockey_attack(self, blocks: ArrayList[MinecraftBlock]) -> None:
        """
        Chicken Jockey Attack
        Args:
            blocks (ArrayList[MinecraftBlock]): The list of blocks to mine.
        Complexity:
            Not required
        """
        RandomGen.random_shuffle(blocks)

    def main(self, scenario: int, **criteriaArgs) -> None:
        """
        Main function to run the NotMinecraft game.
        Args:
            scenario (int): The scenario number to run.
            criteriaArgs (dict): Additional arguments for the scenario.
        Complexity:
            Not required
        Sample Usage:
            not_minecraft = NotMinecraft(cave_system, checklist)
            not_minecraft.main(1, block1=block1, block2=block2)
            not_minecraft.main(2, time_in_seconds=60)
        """
        if scenario == 1:
            blocks = self.dfs_explore_cave()
            self.objective_mining_summary(blocks, **criteriaArgs)
        elif scenario == 2:
            blocks = self.dfs_explore_cave()
            self.profit_mining(blocks, **criteriaArgs)
