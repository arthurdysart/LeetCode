# -*- coding: utf-8 -*-
"""
Leetcode - DI String Match
https://leetcode.com/problems/di-string-match

Created on Sun Nov 18 16:15:31 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Traverse all string characters and append all range values.

    Time complexity: O(n)
        - Traverse all string characters
    Space complexity: O(n)
        - Appends all values in range to new list
    """
    
    def di_string_match(self, s):
        """
        Creates array of integers following specified "DI" rules.

        :param str s: string containing characters for array rules
        :return: array of integers following sepcified "DI" rules
        :rtype: list[int]
        """
        if not s:
            return list()

        n = len(s)
        l = 0
        r = n

        a = list()
        # Iterate over characters because strings are immutable
        for p in s:
            if p.upper() == "I":
                # Append smallest available value
                a.append(l)
                l += 1             
            else:
                # Append largest available value
                a.append(r)
                r -= 1
        
        # Append last element (note l == r)
        a.append(l)        
        return a

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: string containing characters as "DI" rules 
        :rtype: str
        """
        s = [x.strip("\"\n") for x in sys_stdin][0]
        return s


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    s = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .di_string_match(s)
    print(z)


## END OF FILE