# -*- coding: utf-8 -*-
"""
Leetcode - Spiral Matrix
https://leetcode.com/problems/spiral-matrix

Created on Fri Nov 23 13:51:02 2018
@author: Arthur Dysart
"""


# IMPORTED MODULES
import sys


# MODULE DEFINITIONS
class Solution:
    def get_spiral_order(self, a):
        """
        Traverses all elements of 2D array in spiral order.

        :param list[list[int]] a: 2D array of positive integers
        :return: array of elements from input 2D array in spiral order
        :rtype: list[int]
        """
        if not a:
            return list()

        # Initialize output array with first row of spiral matrix
        t = a[0]

        n = len(a)
        m = len(a[0])

        i = 0
        j = m - 1
        for s, x in enumerate(self.gen_sect_len(n, m)):
            for y in range(0, x):
                i, j = self.eval_next_loc(s, i, j)
                t.append(a[i][j])
        return t

    def gen_sect_len(self, n, m):
        """
        Calculates section length by rows (even iterable) or columns (odd).

        :param int n: total number of rows in spiral matrix
        :param int m: total number of columns in spiral matrix
        :return: length of section in spiral matrix
        :rtype: int
        """
        if m >= n:
            # Number of sections depends on row count
            l = 2 * (n - 1)
        else:
            # Number of sections depends on column count
            l = 2 * m - 1
        
        for x in range(0, l, 1):
            if x % 2 == 0:
                # Calculate section length for even iteration
                yield n - ((x // 2) + 1)
            else:
                # Calculate section length for odd iteration
                yield m - ((x + 1) // 2)

    def eval_next_loc(self, s, i, j):
        """
        Updates row or column pointer corresponding to next element.

        :param int s: integer identifying section number
        :param int i: row pointer in spiral matrix
        :param int j: column pointer in spiral matrix
        :return: updated row and column pointers
        :rtype: tuple[int, int]
        """
        if s % 4 == 0:
            # Traverse column downward
            i += 1
        elif s % 4 == 1:
            # Traverse row backward
            j -= 1
        elif s % 4 == 2:
            # Traverse column upward
            i -= 1            
        else:
            # Traverse column forward
            j += 1
        return i, j

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: 2D array of positive integers
        :rtype: list[list[int]]
        """
        inputs = [x.strip("[]\n ").split("], [") for x in sys_stdin]
        a = [list(map(int,x.split(","))) for x in inputs[0]]
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    r = Solution()\
        .get_spiral_order(a)

    print(r)


## END OF FILE