# -*- coding: utf-8 -*-
"""
Leetcode - Largest Time for Given Digits
https://leetcode.com/problems/largest-time-for-given-digits

Created on Sun Dec  2 13:54:08 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from itertools import permutations
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Pythonic iteration over all array elements.

    Time complexity: O(1)
      - Traverse all 24 permutations of fixed-length input array
    Space complexity: O(1)
      - Update constant number of pointers and generator
    """
    def max_time_from_digits(self, a):
        """
        Determines the latest possible time from digits of input array.

        :param list[int] a: input array of integers
        :return: latest possible time created from digits in input array
        :rtype: str
        """
        if not a:
            return str()
        elif len(a) != 4:
            return str()

        p = str()
        for d in permutations(a):
            if self.is_valid_time(d):
                # Compare time strings in lexicographic order
                p = max("{}{}:{}{}".format(*d),
                        p)
        return p

    def is_valid_time(self, d):
        """
        Determines whether target digit permutation constitutes valid time.

        :param list[int] d: target permutation of input digits
        :return: True if valid constructed time
        :rtype: bool
        """
        if not d:
            return str()
        elif len(d) != 4:
            return str()

        # Check hours
        h = d[0] * 10 + d[1]
        if h >= 24:
            return False

        # Check minutes
        m = d[2] * 10 + d[3]
        if m >= 60:
            return False

        # Found valid time
        return True

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of digits
        :rtype: list[int]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = []
        else:
            a = [int(x)
                 for x
                 in inputs[0].split(",")]
        
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .max_time_from_digits(a)
    print(z)


## END OF FILE