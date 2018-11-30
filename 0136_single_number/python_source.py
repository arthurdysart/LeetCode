# -*- coding: utf-8 -*-
"""
Leetcode - Single Number
https://leetcode.com/problems/single-number

Created on Thu Nov 29 23:19:36 2018
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

    def find_single_number(self, a):
        """
        Reports the singleton number in input array.

        :param list[int] a: input array of integers
        :return: singleton integer in array
        :rtype: int
        """
        if not a:
            return -1

        p = a[0]

        n = len(a)
        for i in range(1, n, 1):
            p ^= a[i]

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
        .find_single_number(a)
    print(z)


## END OF FILE