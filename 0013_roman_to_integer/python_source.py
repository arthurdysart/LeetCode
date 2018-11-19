# -*- coding: utf-8 -*-
"""
Leetcode - Roman to Integer
https://leetcode.com/problems/roman-to-integer

Created on Sun Nov 18 23:01:57 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Two-pointer iteration across all string characters.
    
    Time complexity: O(n)
        - Iterate over all characters in string
    Space complexity: O(1)
        - Evaluate constant pointers
    """

    def roman_to_int(self, s):
        """
        Calculates the integer representation of input Roman numeral string.

        :param str s: string representation of Roman numeral
        :return: integer representation of Roman numeral
        :rtype: int
        """
        if not s:
            return 0

        # Create hash table for Roman numerals
        d = self.make_reference()

        p = ""
        x = 0
        for c in s.upper():
            # Evaluate M (1000)
            if c == "M":
                if p == "C":
                    p = "CM"
                else:
                    p = "M"
            # Evaluate D (500)
            elif c == "D":
                if p == "C":
                    p = "CD"
                else:
                    p = "D"
            # Evaluate C (100)
            elif c == "C":
                if p == "X":
                    p = "XC"
                else:
                    p = "C"
            # Evaluate L (50)
            elif c == "L":
                if p == "X":
                    p = "XL"
                else:
                    p = "L"
            # Evaluate X (10)
            elif c == "X":
                if p == "I":
                    p = "IX"
                else:
                    p = "X"
            # Evaluate V (5)
            elif c == "V":
                if p == "I":
                    p = "IV"
                else:
                    p = "V"
            # Evaluate I (1)
            else:
                p = "I"
            
            x += d[p]

        return x
        
    def make_reference(self):
        """
        Creates translation reference for Roman numeral characters.

        :return: hash map to translate characters to integers
        :rtype: dict[str, int]
        """
        d = dict([("M",  1000),
                  ("CM",  800),
                  ("D",   500),
                  ("CD",  300),
                  ("C",   100),
                  ("XC",   80),
                  ("L",    50),
                  ("XL",   30),
                  ("X",    10),
                  ("IX",    8),
                  ("V",     5),
                  ("IV",    3),
                  ("I",     1),])
        return d

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: string representation of Roman numeral
        :rtype: str
        """
        inputs = [x for x in sys_stdin]
        s = inputs[0].strip("\"\n")
        return s


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    s = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .roman_to_int(s)
    print(z)


## END OF FILE