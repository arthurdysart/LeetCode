# -*- coding: utf-8 -*-
"""
Leetcode - Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray

Created on Sun Nov 25 14:49:39 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Modified tabulation (bottom-up dynamic programming) algorithm.

    Time complexity: O(n ** 2)
      - Amortized evaluate all start index and subarray length combinations
    Space complexity: O(n ** 2)
      - Amortized store all start index and subarray length combinations
    """

    def find_max_prod(self, a):
        """
        Determines maximum subarray product for input 1D array.

        :param list[int] a: array of integers
        :return: maximum possible subarray product
        :rtype: int
        """
        if len(a) == 0:
            return 0
        elif len(a) == 1:
            return a[0]
        
        n = len(a)
        p = float("-inf")

        # Iterate over all subaray lengths
        for i in range(0, n, 1):
            t = 1
            # Iterate over all start indicies
            for j in range(i, n, 1):
                t *= a[j]
                p = max(p, t)

                if t == 0:
                    break

        if p == float("-inf"):
            return 0
        else:
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


if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_max_prod(a)
    print(z)