# -*- coding: utf-8 -*-
"""
Leetcode - Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target

Created on Sat Nov 24 13:50:34 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Successive binary search of 2 1D arrays.

    Time complexity: O(log(n * m))
      - Execute binary search on first-elements then target row of 2D array
    Space complexity: O(1)
      - Update constant pointers
    """

    def find_next_letter(self, a, x):
        """
        Determines next letter greater than specified target character.

        :param list[str] a: input array of sorted characters
        :param str x: target character
        :return: next character greater than target character
        :rtype: str
        """
        if len(a) < 1:
            return ""
        elif x >= a[-1]:
            # First element is next greater than letter
            return a[0]

        n = len(a)

        l = 0
        r = n - 1
        while l < r:
            m = l + (r - l) // 2
            if a[m] <= x:
                l = m + 1
            else:
                r = m

        if a[l] <= x:
            # Next element is next greater than target
            return a[l + 1]
        else:
            # Current element is next greater than target
            return a[l]

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of sorted characters and target character
        :rtype: tuple[list[str], str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = []
        else:
            a = [x
                 for x
                 in inputs[0].split("\", \"")]

        x = inputs[1]

        return a, x


if __name__ == "__main__":
    # Imports standard input
    a, x = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_next_letter(a, x)
    print(z)