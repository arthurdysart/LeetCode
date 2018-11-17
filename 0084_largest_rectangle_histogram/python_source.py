# -*- coding: utf-8 -*-
"""
Leetcode - Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram

Created on Thu Nov 15 19:51:56 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Dynamic programming (tabulation) solution.

    Time complexity: O(n ** 2)
        - Iterate over all index-sublength pairs
    Space complexity: O(n ** 2)
        - Complete tabulation procedure
    """

    def largest_rectangle_area(self, a):
        """
        Calculates area of maximum rectangle in histrogram.

        :param list[int] a: list of height values in histogram
        :return: area of maximum rectangle
        :rtype: int
        """
        if not a:
            return 0
        elif len(a) < 2:
            return a[0] * 1
        else:
            c = {}
            p = max(a)
            n = len(a)

            # Solve first row
            for j in range(0, n):
                c[(1, j)] = a[j]
                p = max(a[j] * 1, p)

            # Calculate minimum height for subproblems
            for i in range(2, n + 1):
                for j in range(0, n - i + 1):
                    c[(i, j)] = min(c[(i - 1, j)],
                                    c[(i - 1, j + 1)])
    
                    # Calculate target area
                    t = c[(i, j)] * i
                    p = max(p, t)

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of histogram heights
        :rtype: list[int]
        """
        inputs = [x.strip("[]\n").split(",")
                  for x
                  in sys_stdin]
        return [int(x) for x in inputs[0]]


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .largest_rectangle_area(a)
    print(z)


## END OF FILE