# -*- coding: utf-8 -*-
"""
Leetcode - Pascal's Triangle
https://leetcode.com/problems/pascals-triangle

Created on Thu Dec 13 16:33:59 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from functools import lru_cache
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Pythonic iteration over all Pascal triangle depths and node values.
    Implements memoization algorithm (top-down dynamic programming).

    Time complexity: O(n ** m)
      - Iterate over all triangle depths and values
    Space complexity: O(n ** m)
      - Store all intermediate triangle values
    """

    def create_pascal_triangle(self, n):
        """
        Creates Pascal triangle to specified depth "n".

        :param int n: max depth of target Pascal triangle
        :return: array of all triangle levels to max depth "n" (inclusive)
        :rtype: list[list[int]]
        """
        if n == 0:
            return list()

        return [self.gen_triangle_level(i)
                for i
                in range(1, n + 1, 1)]

    @lru_cache(maxsize = 200, typed = False)
    def gen_triangle_level(self, i):
        """
        Generates specified level "i" of Pascal triangle.
        Implements memoization via LRU cache decorator function.

        :param int i: target level of Pascal triangle
        :return: array of all values belonging to target level
        :rtype: list[int]
        """
        if i == 1:
            return list([1])

        # Select previous level
        t = self.gen_triangle_level(i - 1)
        m = len(t) + 1

        return [1
                if (j == 0 or
                    j == m - 1)
                else t[j - 1] + t[j]
                for j
                in range(0, m, 1)]

class Solution2:
    """
    Iteration over all Pascal triangle depths and node values.
    Implements tabulation algorithm (bottom-up dynamic programming).

    Time complexity: O(n ** m)
      - Iterate over all triangle depths and values
    Space complexity: O(n ** m)
      - Store all intermediate triangle values
    """

    def create_pascal_triangle(self, n):
        """
        Creates Pascal triangle to specified depth "n".

        :param int n: max depth of target Pascal triangle
        :return: array of all triangle levels to max depth "n" (inclusive)
        :rtype: list[list[int]]
        """
        if n == 0:
            return list()

        # Initialize full cache array
        c = [[None] * i
             for i
             in range(1, n + 1, 1)]

        for i in range(0, n, 1):
            for j in range(0, i + 1, 1):
                # Iterate over level-depth "i" and node position "j"

                if (j == 0 or
                    j == i):
                    # Evaluate as outer triangle edge
                    c[i][j] = 1

                else:
                    # Evaluate as sum of corresponding previous elements
                    c[i][j] = c[i - 1][j - 1] + c[i - 1][j]

        return c

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: max depth of target Pascal triangle
        :rtype: list[str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        n = int(inputs[0])

        return n


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    n = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .create_pascal_triangle(n)
    print(z)


## END OF FILE