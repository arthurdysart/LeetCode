# -*- coding: utf-8 -*-
"""
Leetcode - Robot Return to Origin
https://leetcode.com/problems/robot-return-to-origin

Created on Wed Dec 19 22:01:50 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all characters in input string.

    Time complexity: O(n)
      - Iterate over all string characters
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def is_cyclic_path(self, s):
        """
        Determines whether movement pattern returns to original position.

        :param str s: input string as movement pattern
        :return: True if movement pattern returns to original position
        :rtype: bool
        """
        if not s:
            return True

        x = 0
        y = 0

        for c in s:

            if c == "U":
                x += 1
            elif c == "D":
                x -= 1
            elif c == "L":
                y -= 1
            elif c == "R":
                y += 1
            else:
                # Found invalid movement character
                return False

        return (x == 0 and
                y == 0)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input string
        :rtype: list[list[int]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        s = inputs[0].strip("\"")

        return s


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    s = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_cyclic_path(s)
    print(z)


## END OF FILE