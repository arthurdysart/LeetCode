# -*- coding: utf-8 -*-
"""
Leetcode - Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Created on Sun Jan 13 22:58:11 2019
@author: Arthur Dysart
"""


# REQUIRED MODULES
import json
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iterative search of input array.
    Implements binary search algorithm.

    Time complexity: O(log(n))
      - Search input array using binary search algorithm
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def find_peak_index(self, a):
        """
        Determines location of peak index in unimodal mountain array.

        :param list[int] a: array of unimodal values
        :return: index of maximum value
        :rtype: int
        """
        if not a:
            return -1

        l = 0
        r = len(a) - 1

        while l < r:

            m = l + (r - l) // 2

            if a[m] < a[m + 1]:
                # target index is to left of maximum value
                l = m + 1

            else:
                # target index is to right of maximum value
                r = m

        # Pointers converge to index of maximum value
        return l

class Solution1:
    """
    Iterative linear search of input array.

    Time complexity: O(n)
      - Amortized traverse all elements of input array
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def find_peak_index(self, a):
        """
        Determines location of peak index in unimodal mountain array.

        :param list[int] a: array of unimodal values
        :return: index of maximum value
        :rtype: int
        """
        if not a:
            return -1

        p = 0        

        while a[p] < a[p + 1]:
            p += 1

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of unimodal integer values
        :rtype: list[list[int]], int
        """
        try:
            x = next(sys_stdin)
            a = json.loads(x)
        except:
            a = ""

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_peak_index(a)
    print(json.dumps(z))


## END OF FILE