# -*- coding: utf-8 -*-
"""
Leetcode - Monotonic Array
https://leetcode.com/problems/monotonic-array

Created on Sat Dec 22 23:07:46 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all elements in array.

    Time complexity: O(n)
      - Iterate over all array elements
    Space complexity: O(1)
      - Amortized collect one element in unique set
    """

    def is_monotonic(self, a):
        """
        Determines whether array is strictly either increasing or decreasing.

        :param list[int] a: input array of integers
        :return: True if input array is monotonically increasing or decreasing
        :rtype: bool
        """
        if len(a) < 2:
            return True

        s = set()

        n = len(a)
        for i in range(0, n - 1, 1):

            if a[i + 1] - a[i] == 0:
                # Ignore value pair
                continue

            elif a[i + 1] - a[i] > 0:
                # Add increasing value pair
                s.add(True)

            else:
                # Add increasing value pair
                s.add(False)

            if len(s) > 1:
                # Found non-monotonic value pair
                return False

        return True

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
            a = list()
        else:
            a = [int(x)
                 for x
                 in inputs[0].split(",")]

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_monotonic(a)
    print(z)


## END OF FILE