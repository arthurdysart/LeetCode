# -*- coding: utf-8 -*-
"""
Leetcode - Intersection of two arrays
https://leetcode.com/problems/intersection-of-two-arrays

Created on Sun Oct 28 15:41:45 2018
Updated on Sun Dec  2 20:30:23 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
class Solution:
    """
    Pythonic iteration over all elements of input arrays.

    Time complexity: O(min(len(n), len(m)))
      - Traverse all elements of smaller input array
    Space complexity: O(min(len(n), len(m)))
      - Amortized collect all elements of smaller input array
    """

    def find_intersection(self, a1, a2):
        """
        Determines common elements in both input arrays.

        :param list[int] a1: first input array
        :param list[int] a2: second input array
        :return: array of elements common to both input arrays
        :rtype: list[int]
        """
        return list(set(a1).intersection(set(a2)))

class Solution2:
    """
    Iteration over all elements of smaller input array with binary search.

    Time complexity: O(min(len(n), len(m)))
      - Traverse all elements of smaller input array
    Space complexity: O(min(len(n), len(m)))
      - Amortized collect all elements of smaller input array
    """

    def find_intersection(self, a1, a2):
        """
        Determines common elements in both input arrays.

        :param list[int] a1: first input array
        :param list[int] a2: second input array
        :return: array of elements common to both input arrays
        :rtype: list[int]
        """
        # Checks for empty arrays
        if (not a1 or
            not a2):
            return list()

        # Assign smaller array "u" and larger array "v"
        if len(a1) < len(a2):
            u = list(set(a1))
            v = list(set(a2))
        else:
            u = list(set(a2))
            v = list(set(a1))

        u.sort()

        # Search smaller array "u" for elements of larger array "v"
        r = [x
             for x
             in v
             if self.is_present(x, u)]
        return r

    def is_present(self, x, u):
        """
        Determines whether target element is in array using binary search.

        :param int x: target element
        :param list[int] u: target array
        :return: True if target element found in target array
        :rtype: bool
        """
        l = 0
        r = len(u) - 1

        while l <= r:
            m = l + (r - l) // 2

            if u[m] == x:
                return True
            elif u[m] < x:
                l = m + 1
            else:
                r = m - 1

        return False

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input arrays of integers
        :rtype: tup[list[int], list[int]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        a1 = self.cast_int_arr(inputs[0])
        a2 = self.cast_int_arr(inputs[1])

        return a1, a2

    def cast_int_arr(self, s):
        """
        Converts string to array of integers.

        :param str s: input string
        :return: array of integers
        :rtype: list[int]
        """
        if s == "":
            a = list()
        else:
            a = [int(x)
                 for x
                 in s.split(",")]
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a1, a2 = Input()\
             .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_intersection(a1, a2)
    print(z)


## END OF FILE