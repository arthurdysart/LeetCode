# -*- coding: utf-8 -*-
"""
Leetcode - Maximum Subarray
https://leetcode.com/problems/maximum-subarray

Created on Mon Dec  3 14:39:29 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
class Solution:
    """
    Tabulation (dynamic programming) of all possible solutions.

    Time complexity: O(n ** 2)
      - Iterate over all combinations of subarray length and start index
    Space complexity: O(n ** 2)
      - Collect all subarray sums in sub-problem 2D array
    """

    def find_max_subarr_sum(self, a):
        """
        Determines maximum sum across all subarrays of input array.
        Interpolates sub-problem tabulation (dynamic programming) algorithm.

        :param list[int] a: input array of integers
        :return: maximum subarray sum
        :rtype: int
        """
        if not a:
            return 0

        n = len(a)
        p = float("-inf")

        # Initialize matrix of subarray sums
        t = [[None] * (n - i)
             for i
             in range(0, n, 1)]

        # Evaluate sum for all subarrays with length 1
        for j in range(0, n, 1):
            t[j][0] = a[j]
            p = max(p, a[j])

        # Iterate over all combinations of subarray length > 1 and start index
        for j in range(1, n, 1):
            for i in range(0, n - j, 1):

                # Evaluate sum of target subarray
                t[i][j] = t[i][j - 1] + t[i + j][0]

                p = max(p, t[i][j])

        if p == float("-inf"):
            return 0
        else:
            return p

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

        if inputs[0] == "":
            a = list()
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
        .find_max_subarr_sum(a)
    print(z)


## END OF FILE