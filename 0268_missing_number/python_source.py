# -*- coding: utf-8 -*-
"""
Leetcode - Missing Number
https://leetcode.com/problems/missing-number

Created on Thu Nov 29 23:37:21 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration and bitwise manipulation of array elements using XOR.

    Time complexity: O(n)
      - Amortized traverse all array elements
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def find_missing_number(self, a):
        """
        Determines the missing integer in input array.

        :param list[int] a: input array of integers
        :return: missing integer from array
        :rtype: int
        """
        if not a:
            return 0

        n = len(a)
        p = n

        for i in range(0, n, 1):
            p ^= i ^ a[i]

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of integers
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
        .find_missing_number(a)
    print(z)


## END OF FILE