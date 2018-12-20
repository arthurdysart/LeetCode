# -*- coding: utf-8 -*-
"""
Leetcode - Flipping an Image
https://leetcode.com/problems/flipping-an-image

Created on Wed Dec 19 21:49:26 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Pythonic iteration over all elements in input 2D array.

    Time complexity: O(n * m)
      - Iterate over all array elements
    Space complexity: O(1)
      - Update constant number of pointers and update array in-place
    """

    def flip_invert_arr(self, a):
        """
        Flips and inverts input 2D array of binary integers.

        :param list[list[int]] a: input 2D array of integers
        :return: updated 2D array
        :rtype: list[int[int]]
        """
        if not a:
            return list([list()])

        n = len(a)
        m = len(a[0])

        for i in range(0, n, 1):

            a[i] = [a[i][m - 1 - j] ^ 1
                    for j
                    in range(0, m, 1)]

        return a

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input 2D array of integers
        :rtype: list[list[int]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = list()
        else:
            a = [list(map(int, x.split(",")))
                 for x
                 in inputs[0].split("],[")]

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .flip_invert_arr(a)
    print(z)


## END OF FILE