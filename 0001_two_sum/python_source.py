# -*- coding: utf-8 -*-
"""
Leetcode - Two Sum
https://leetcode.com/problems/two-sum

Created on Sun Nov 11 19:31:41 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Time complexity: O(n)
        - Amortized iterate over all elements in array
    Space complexity: O(n)
        - Amortized store all elements in array
    """
    def two_sum(self, a, x):
        """
        Determines indicies of elements whose sum equals target "x".

        :type a: list[int]
        :type x: int
        :rtype: list[int]
        """
        # Check for insufficent input
        if (len(a) < 2 or 
            x is None):
            return [-1, -1]

        # Initialize cache for queried elements
        c = {}

        n = len(a)
        for i in range(0, n):
            t = x - a[i]
            if t in c:
                return [c[t], i]
            else:
                c[a[i]] = i
            
        # No pair found in array
        return [-1, -1]


class Solution_2:
    """
    Time complexity: O(n ** 2)
        - Check all pairs of integers in array
    Space complexity: O(1)
        - No external data structures required
    """
    def two_sum(self, a, x):
        """
        Determines indicies of elements whose sum equals target "x".

        :type a: list[int]
        :type x: int
        :rtype: list[int]
        """
        # Check for insufficent input
        if (len(a) < 2 or 
            x is None):
            return [-1, -1]

        n = len(a)
        for i in range(0, n):
            t = x - a[i]
            for j in range(i + 1, n):
                if a[j] == t:
                    return [i, j]

        # No pair found in array
        return [-1, -1]

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of integers and sum target
        :rtype: tuple[list[int], int]
        """
        inputs = [x for x in sys_stdin]
        a = [int(x) for x in inputs[0].strip("[]\n").split(",")]
        x = int(inputs[1])
        return a, x


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a, x = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .two_sum(a, x)
    print(z)


## END OF FILE