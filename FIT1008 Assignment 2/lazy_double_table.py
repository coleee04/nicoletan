from __future__ import annotations

from data_structures.referential_array import ArrayR
from data_structures.abstract_hash_table import HashTable
from typing import TypeVar


V = TypeVar('V')


class LazyDoubleTable(HashTable[str, V]):
    """
    Lazy Double Table uses double hashing to resolve collisions, and implements lazy deletion.

    Feel free to check out the implementation of the LinearProbeTable class if you need to remind
    yourself how to implement the methods of this class.

    Type Arguments:
        - V: Value Type.
    """
    
    # No test case should exceed 1 million entries.
    TABLE_SIZES = (5, 13, 29, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869)
    HASH_BASE = 31
    lazy_dlt_mark = object() # Lazy deletion marker

    def __init__(self, sizes = None) -> None:
        """
        No complexity analysis is required for this function.
        Do not make any changes to this function.
        """
        if sizes is not None:
            self.TABLE_SIZES = sizes

        self.__size_index = 0
        self.__array: ArrayR[tuple[str, V]] = ArrayR(self.TABLE_SIZES[self.__size_index])
        self.__length = 0
    
    @property
    def table_size(self) -> int:
        return len(self.__array)

    def __len__(self) -> int:
        """
        Returns the number of elements in the hash table
        """
        return self.__length

    def keys(self) -> ArrayR[str]:
        """
        Returns all keys in the hash table.
        :complexity: O(N) where N is the table size.
        """
        res = ArrayR(self.__length)
        i = 0
        for x in range(self.table_size):
            if self.__array[x] is not None:
                res[i] = self.__array[x][0]
                i += 1
        return res

    def values(self) -> ArrayR[V]:
        """
        Returns all values in the hash table.

        :complexity: O(N) where N is the table size.
        """
        res = ArrayR(self.__length)
        i = 0
        for x in range(self.table_size):
            if self.__array[x] is not None:
                res[i] = self.__array[x][1]
                i += 1
        return res

    def __contains__(self, key: str) -> bool:
        """
        Checks to see if the given key is in the Hash Table

        :complexity: See __getitem__.
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> V:
        """
        Get the value at a certain key

        :complexity: See hashy probe.
        :raises KeyError: when the key doesn't exist.
        """
        position = self.__hashy_probe(key, False)
        return self.__array[position][1]
    
    def is_empty(self) -> bool:
        return self.__length == 0
    
    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular
        order).
        """
        result = ""
        for item in self.__array:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result

    def hash(self, key: str) -> int:
        """
        Hash a key for insert/retrieve/update into the hashtable.
        :complexity: O(len(key))
        """
        value = 0
        a = 31415
        for char in key:
            value = (ord(char) + a * value) % self.table_size
            a = a * self.HASH_BASE % (self.table_size - 1)
        return value

    def hash2(self, key: str) -> int:
        """
        Used to determine the step size for our hash table.

        Complexity:

            Best Case Complexity: O(len(key))
            Worst Case Complexity: O(len(key) + M)
            # M is the number of slots in the hash table, representing the number of probes we need to find the correct slot.
        
        """
        val = 0
        a = 31415
        for char in key:
            val = (a * val + ord(char)) % self.table_size
            a = a * 17 % (self.table_size - 1) # Use a new base different with HASH_BASE
        
        # Avoid zero step size
        if val == 0:
            step = 1
        else:
            step = val
        
        while self.__gcd(step, self.table_size) != 1:
            step += 1
        
        return step
    
    def __gcd(self, a: int, b: int) -> int:
        """
        Returns the greatest common divisor of a and b.
        """
        while b != 0:
            a, b = b, a % b 
            # Repeating update new a = current b and new b = a % b if b != 0
        return a


    def __hashy_probe(self, key: str, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using hashy probing.

        Raises:
            KeyError: When the key is not in the table, but is_insert is False.
            RuntimeError: When a table is full and cannot be inserted.

        Complexity:

            Best Case Complexity: O(1)
            # Key or an empty slot is found in the first position

            Worst Case Complexity: O(N)
            # N = table size
            # Probe the entire table to find the key or an empty slot if it's almost full
        
        """
        # Initial position
        position = self.hash(key)
        step = self.hash2(key)
        lazy_delete = -1 # Initialise to -1 to indicate no deleted slot yet

        for _ in range(self.table_size): # Try for every possible slot in the table up to max table size
            current = self.__array[position] # Check if the current position is None, deleted, or an actual key/value pair

            if current is None:
                if is_insert:
                    # Insert to the marked first shown deleted slot if inserting
                    return lazy_delete if lazy_delete != -1 else position
                else:
                    # Not inserting
                    raise KeyError(key)
                
            elif current is self.lazy_dlt_mark:
                if is_insert and lazy_delete == -1:
                    lazy_delete = position # Mark down first found deleted slot
                
            elif current[0] == key:
                return position # Key found
            
            position = (position + step) % self.table_size # Move to next position

        # If is_insert is True but nothing returned yet
        if is_insert:
            raise RuntimeError("Table is full")
        else:
            raise KeyError(key)


    def __setitem__(self, key: str, data: V) -> None:
        """
        Set a (key, value) pair in our hash table.

        Remember! This is where you will need to call __rehash if the table is full!
        
        Complexity:

            Best Case Complexity: O(1)
            # Key is inserted without collision

            Worst Case Complexity: O(N + R)
            # N = table size
            # R = time taken to rehash the table if table is full
        
        """
        if self.__length + 1 > self.table_size // 2:
            self.__rehash() # Rehash if the table is more than half full

        position = self.__hashy_probe(key, True)

        if self.__array[position] is None or self.__array[position] is self.lazy_dlt_mark:
            self.__length += 1
        
        self.__array[position] = (key, data)
        

    def __delitem__(self, key: str) -> None:
        """
        Deletes a (key, value) pair in our hash table.

        Complexity:

            Best Case Complexity: O(1)
            # Key is deleted without collision

            Worst Case Complexity: O(N)
            # N = table size
            # Probe the entire table to find the key if collisions are bad
        
        """
        position = self.__hashy_probe(key, False)

        if self.__array[position] is not None:
            self.__array[position] = self.lazy_dlt_mark # Mark the deleted position
            self.__length -= 1


    def __rehash(self) -> None:
        """
        Need to resize table and reinsert all values

        Complexity:

            Best Case Complexity: O(N)
            Worst Case Complexity: O(N)
            # N = table size
            # Go through every slot in the old table with N slots and reinsert valid ones into the new hash table
        
        """
        prev_array = self.__array
        self.__size_index += 1
        self.__array = ArrayR(self.TABLE_SIZES[self.__size_index])
        self.__length = 0

        for item in prev_array:
            if item is not None and item is not self.lazy_dlt_mark:
                key, value = item
                self[key] = value
