# -*- coding: utf-8 -*-
"""
Leetcode - Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences

Created on Sun Nov 25 00:18:47 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import deque
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iterative traversal of 1D array.

    Time complexity: O(n)
      - Amortized iterate across both input arrays
    Space complexity: O(n)
      - Amortized store all elements from input array for append sequence
    """

    def validate_stack_sequences(self, a, b):
        """
        Determines next letter greater than specified target character.

        :param list[int] a: array of integers representing append sequence
        :param list[int] b: array of integers representing pop sequence
        :return: True if append and pop sequences are valid
        :rtype: bool
        """
        if (not a and
            not b):
            # Null input arrays
            return True
        elif (not a or
              not b):
            # One null input array
            return False

        n = len(a)
        m = len(b)
        p = 0

        q = deque()

        for i in range(n):
            # Append according to input sequence
            q.append(a[i])

            while (q and
                   q[-1] == b[p]):
                # Pop according to output sequence
                q.pop()
                p += 1

        if p == m:
            # Complete input and output arrays
            return True
        else:
            # Incomplete output array
            return False

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input arrays for append and pop sequence
        :rtype: tuple[list[int], list[int]]
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

        if inputs[1] == "":
            b = []
        else:
            b = [int(x)
                 for x
                 in inputs[1].split(",")]

        return a, b


if __name__ == "__main__":
    # Imports standard input
    a, b = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .validate_stack_sequences(a, b)
    print(z)