# -*- coding: utf-8 -*-
"""
Leetcode - Transpose Matrix
https://leetcode.com/problems/transpose-matrix

Created on Fri Nov 23 11:13:48 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all elements of 2D array.

    Time complexity: O(n * m)
        - Iterate over all elements of 2D array
    Space complexity: O(n * m)
        - Store all elements in new 2D array
    """

    def transpose_matrix(self, a):
        """
        Transform all rows into columns in 2D array.

        :param list[list[int]] a: input 2D array of integers
        :return: 2D array transposed
        :rtype: list[list[int]]
        """
        return [list(x) for x in zip(*a)]

class Solution2:
    """
    Iteration over all elements of 2D array.
    Temporary arrays created by comprehension and updated by list indexing.

    Time complexity: O(n * m)
        - Iterate over all elements of 2D array
    Space complexity: O(n * m)
        - Store all elements in new 2D array
    """

    def transpose_matrix(self, a):
        """
        Transform all rows into columns in 2D array.

        :param list[list[int]] a: input 2D array of integers
        :return: 2D array transposed
        :rtype: list[list[int]]
        """
        if not a:
            return list(list())

        n = len(a[0])
        m = len(a)

        u = [None for x in range(n)]
        for i in range(n):
            v = [None for x in range(m)]
            for j in range(m):
                v[j] = a[j][i]
            u[i] = v

        return u

class Solution3:
    """
    Iteration over all elements of 2D array.
    Temporary arrays updated by list appending.

    Time complexity: O(n * m)
        - Iterate over all elements of 2D array
    Space complexity: O(n * m)
        - Store all elements in new 2D array
    """

    def transpose_matrix(self, a):
        """
        Transform all rows into columns in 2D array.

        :param list[list[int]] a: input 2D array of integers
        :return: 2D array transposed
        :rtype: list[list[int]]
        """
        if not a:
            return list(list())

        n = len(a[0])
        m = len(a)

        u = list()
        for i in range(n):
            v = list()
            for j in range(m):
                v.append(a[j][i])
            u.append(v)

        return u

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input 2D array of integers
        :rtype: list[list[int]]
        """
        inputs = [x.strip("[]\n").split("],[") for x in sys_stdin]
        a = [list(map(int,x.split(","))) for x in inputs[0]]
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .transpose_matrix(a)
    print(z)


## END OF FILE