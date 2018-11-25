# -*- coding: utf-8 -*-
"""
Leetcode - Minimum Increment to Make Array Unique
https://leetcode.com/problems/minimum-increment-to-make-array-unique

Created on Sun Nov 25 15:00:58 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration and sort over all array elements.

    Time complexity: O(n * log(n))
      - Amortized traverse and sort all array elements 
    Space complexity: O(n)
      - Amortized store all values in unique element set
    """

    def make_array_unique(self, a):
        """
        Calculate minimum number of increments to make array elements unique.

        :param list[int] a: input array of integers
        :return: minimum unit increments to make array elements unique
        :rtype: int
        """
        if not a:
            return 0

        n = len(a)
        u = set()
        v = list()

        p = float("inf")
        for i in range(n):
            p = min(p, a[i])
            if a[i] in u:
                # Add to duplicate list
                v.append(a[i])
            else:
                # Add to unique set
                u.add(a[i])
            
        # Sort dupicates in ascending order
        v.sort()

        m = len(v)

        t = 0
        for j in range(m):
            while (p < v[j]
                   or p in u):
                p += 1
            # Add minimum increments to running total
            t += p - v[j]
            u.add(p)

        return t

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
        .make_array_unique(a)
    print(z)