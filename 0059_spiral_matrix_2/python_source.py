# -*- coding: utf-8 -*-
"""
Leetcode - Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii
Amortized solution

Created on Thu Nov  8 18:54:34 2018
@author: Arthur Dysart
"""


# IMPORTED MODULES
import sys


# MODULE DEFINITIONS
class Solution:
    def make_spiral_matrix(self, n):
        """
        Creates spiral matrix from given characteristic factor "n".

        :param int n: characteristic factor for spiral matrix
        :return: completed 2D spiral matrix
        :rtype: list[list[int]]
        """
        # initialize array, row/column pointers, partition counter
        a = [[None] * n for x in range(n)]
        i = 0
        j = 0
        p = 0

        # Complete first row
        a, j, x = self.set_initial_row(a, i, j, n)

        for q in self.gen_part_len(n):
            for t in range(0, q):
                i, j = self.eval_next_loc(p, i, j)
                a[i][j] = x
                x += 1
            # Increase partition number
            p += 1
    
        return a

    def set_initial_row(self, a, i, j, n):
        """
        Completes the first partition (row 0) of spiral matrix.

        :param list[list[]int] a: in-progress spiral matrix
        :param int i: row pointer in spiral matrix
        :param int j: column pointer in spiral matrix
        :param int n: characteristic factor for spiral matrix
        :return: spiral matrix with completed first partition (row 0)
        :rtype: list[list[int]]
        """
        # Update all elements but last
        for x in range(1, n):
            a[i][j] = x
            j += 1
        # Update last element
        a[i][j] = n

        return a, j, n + 1
    
    def gen_part_len(self, n):
        """
        Generates number of elements in each partition.

        :param int n: characteristic factor for spiral matrix
        :yield: number of elements in current partition
        :ytype: int
        """
        for x in range(2 * n - 3, -1, -1):
            if x % 2 == 0:
                yield int((x / 2) + 1)
            else:
                yield int((x + 1) / 2)
    
    def eval_next_loc(self, p, i, j):
        """
        Updates row or column pointer corresponding to next element.

        :param int p: counter for partition number
        :param int i: row pointer in spiral matrix
        :param int j: column pointer in spiral matrix
        :return: updated row and column pointers
        :rtype: tup[int, int]
        """
        # If parition number is even, traverse column
        if p % 2 == 0:
            # If modulus 0 or 1, traverse column downward
            if (p % 4 < 2):
                i += 1
            # If modulus 2 or 3, traverse column upward
            if (p % 4 > 1):
                i -= 1
        # If odd, traverse row
        else:
            # If modulus 0 or 1, traverse row backward
            if (p % 4 < 2):
                j -= 1
            # If modulus 2 or 3, traverse row forward
            if (p % 4 > 1):
                j += 1
        return i, j

def stdin(sys_stdin):
    """
    Imports standard input.
    
    :param _io.TextIOWrapper sys_stdin: standard input
    :return: characteristic factor for spiral matrix
    :rtype: int
    """
    return [int(x) for x in sys_stdin][0]


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    n = stdin(sys.stdin)

    # Evaluates solution
    r = Solution()\
        .make_spiral_matrix(n)

    print(r)


## END OF FILE