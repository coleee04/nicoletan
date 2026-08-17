from __future__ import annotations
from collections.abc import Callable
from algorithms.mergesort import mergesort

from typing import Tuple, TypeVar, Optional 

from data_structures import *

K = TypeVar('K')
I = TypeVar('I')


class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: ArrayList[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements ArrayList.

        As such you can assume the length of elements to be non-zero.
        The elements ArrayList will contain tuples of key, item pairs.

        First sort the elements ArrayList and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(ArrayList[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            Best Case Complexity: O(NlogN)
            Worst Case Complexity: O(NlogN)

        Justification:
            N is the length of the elements list.
            The elements are sorted using mergesort with O(NlogN) complexity.
            Building balanced tree takes O(N) complexity
            Overall is O(NlogN) dominating the time complexity of the constructor.
        """
        super().__init__()
        new_elements: ArrayList[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)

    def __sort_elements(self, elements: ArrayList[Tuple[K, I]]) -> ArrayList[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.

        Args:
            elements (ArrayList[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            ArrayList(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: O(NlogN * comp(T))
            Worst Case Complexity: O(NlogN * comp(T)) 
        
        Justification:
            N is the length of the list and comp is the cost of comparison for the object type T (the elements in the list).
            We're sorting Tuple[K,I] pairs based on the key (K) using mergesort.
            O(NlogN) total comparisons, each costs comp(T) to compare two elements.

        """
        return mergesort(elements, key=lambda x: x[0])
    
    def __build_balanced_tree(self, elements: ArrayList[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (ArrayList[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)

        Justification:
            N is the length of the elements list
            List is sorted and we always insert the middle element first
            Each element is inserted into the tree once, while each insertioon is O(1)    
        """
        def build_tree(start: int, end: int) -> None:
            if start > end:
                return
            
            mid = (start + end) // 2
            key, item = elements[mid]
            self[key] = item  # Insert into the tree
            # Recursion to build the left and right subtrees
            build_tree(start, mid - 1)
            build_tree(mid + 1, end)

        build_tree(0, len(elements) - 1)


    def filter_keys(self, filter_func1: Callable[[K], bool], filter_func2: Callable[[K], bool]) -> ArrayList[Tuple[K, I]]:
        """
        Filters the keys in the tree based on two criteria.

        Args:
            filter_func1 (callable): A function that takes a value and returns True if the key is more than criteria1.
            filter_func2 (callable): A function that takes a value and returns True if the key is less than criteria2.
        Returns:
            ArrayList[Tuple[K, I]]: An ArrayList of tuples containing Key,Item pairs that match the filter.

        Complexity:
            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)

        Justification:
            N is the number of nodes in the tree.
            Visits every node once, checking the filter functions, each with O(!) complexity.
        """
        result = ArrayList()
        def recursive_func(node: Optional[BinarySearchTree.Node[K, I]]) -> None:
            if node is None:
                return
            recursive_func(node.left)
            recursive_func(node.right)
            if filter_func1(node.key) and filter_func2(node.key):
                result.append((node.key, node.item))

        recursive_func(self.root)
        return result
