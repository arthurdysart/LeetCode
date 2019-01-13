# -*- coding: utf-8 -*-
"""
Leetcode - K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Created on Sat Jan 12 23:07:47 2019
@author: Arthur Dysart
"""


# REQUIRED MODULES
import json
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Sort and slice over all elements of input array.

    Time complexity: O(n * log(n))
      - Sort all array elements
    Space complexity: O(n)
      - Amortized collect all input array elements
    """

    def find_k_closest(self, a, k):
        """
        Determines "k" coordinates with smallest distance to origin.

        :param list[list[int]] a: array of coordinate arrays
        :return: array of "k" closest coordinates to origin
        :rtype: list[list[int]]
        """
        if not a:
            return []

        # Sort input array by Euclidean distance from origin
        a.sort(key = lambda x: x[0] ** 2 + x[1] ** 2)

        # Return the "k" smallest elements
        return a[:k]

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input coordinates and number of output coordinates
        :rtype: list[list[int]], int
        """
        return [json.loads(x)
                for x
                in sys_stdin]


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a, k = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_k_closest(a, k)
    print(json.dumps(z))


## END OF FILE