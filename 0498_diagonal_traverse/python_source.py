# -*- coding: utf-8 -*-
"""
Leetcode - Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse

Created on Fri Dec  7 14:02:59 2018
@author: Arthur Dysart
"""


# IMPORTED MODULES
import sys


# MODULE DEFINITIONS
class Solution:
    """
    Iteration over elements in 2D array.

    Time complexity: O(n)
      - Iterate over all elements in 2D array
    Space complexity: O(n)
      - Collect all elements in 2D array
    """

    def find_diagonal_order(self, a):
        """
        Traverses all elements of 2D array in alternating diagonal order.

        :param list[list[int]] a: 2D array of integers
        :return: array of elements from input array in diagonal order
        :rtype: list[int]
        """
        if not a:
            return list()

        n = len(a)
        m = len(a[0])

        # Initialize output 2D array
        t = list()

        for x, c in enumerate(self.gen_diagonal_coord(n, m)):

            # Collect all elements in target diagonal
            p = self.traverse_diagonal(c, m, a)
            
            if x % 2 == 0:
                # Update output array with upward diagonal
                t.extend(p)
            else:
                # Update output array with downward diagonal
                t.extend(reversed(p))

        return t

    def gen_diagonal_coord(self, n, m):
        """
        Generates row-column coordinate of lower limit for target diagonal.
        Yields generator object.

        :param int n: number of rows in 2D array
        :param int m: number of columns in 2D array
        :yield: array of target elements
        :ytype: tup[int, int]
        """
        for i in range(0, n, 1):
            yield i, 0

        for j in range(1, m, 1):
            yield n - 1, j

    def traverse_diagonal(self, c, m, a):
        """
        Collect all elements of target diagonal.

        :param tup[int, int] c: row-column coordinate of diagonal lower limit
        :param int m: number of columns in 2D array
        :param list[list[int]] a: input 2D array of integers
        :return: array of target elements
        :rtype: list[int]        
        """
        i, j = c
        p = list()

        while (i >= 0 and
               j <= m - 1):
            p.append(a[i][j])
            i -= 1
            j += 1

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: 2D array of positive integers
        :rtype: list[list[int]]
        """
        inputs = [x.strip("[]\"\n ").split("],[")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = list([list()])
        else:
            a = [list(map(int,x.split(",")))
                 for x
                 in inputs[0]]

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_diagonal_order(a)
    print(z)


## END OF FILE