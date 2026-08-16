from __future__ import annotations

from data_structures.hash_table_linear_probing import LinearProbeTable


class HashyDateTable(LinearProbeTable[str]):
    """
    HashyDateTable assumed the keys are strings representing dates, and therefore tries to
    produce a balanced, uniform distribution of keys across the table.

    Conflicts are resolved using Linear Probing.
    
    All values will also be strings.
    """
    def __init__(self) -> None:
        """
        Initialise the Hash Table with with increments of 366 as the table size.
        This means, initially we will have 366 slots, once they are full, we will have 4 * 366 slots, and so on.

        No complexity is required for this function.
        Do not make any changes to this function.
        """
        LinearProbeTable.__init__(self, (366, 4 * 366, 16 * 366))

    def hash(self, key: str) -> int:
        """
        Hash a key for insert/retrieve/update into the hashtable.
        The key will always be exactly 10 characters long and can be any of these formats, but nothing else:
        - DD/MM/YYYY
        - DD-MM-YYYY
        - YYYY/MM/DD
        - YYYY-MM-DD

        The function assumes the dates will always be valid i.e. the input will never be something like 66/14/2020.
        
        Complexity:

        Best Case Complexity: O(1) 
        # All operations have constant time complexity

        Worst Case Complexity: O(1)
        # All operations have constant time complexity, no looping operations
        
        """
        if key[4] == '/' or key[4] == '-': # YYYY-MM-DD or YYYY/MM/DD
            year = int(key[:4])
            month = int(key[5:7])
            day = int(key[8:10])
        else: # DD/MM/YYYY or DD-MM-YYYY
            day = int(key[:2])
            month = int(key[3:5])
            year = int(key[6:10])

        leap =  year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
        day_in_year = day

        if month > 1:
            day_in_year += 31
        if month > 2:
            day_in_year += 29 if leap else 28
        if month > 3:
            day_in_year += 31
        if month > 4:
            day_in_year += 30
        if month > 5:
            day_in_year += 31
        if month > 6:
            day_in_year += 30
        if month > 7:
            day_in_year += 31
        if month > 8:
            day_in_year += 31
        if month > 9:
            day_in_year += 30
        if month > 10:
            day_in_year += 31
        if month > 11:
            day_in_year += 30

        diff_year_loop = (year-1970) * 366 + (day_in_year - 1)
        return diff_year_loop % self.table_size
    

