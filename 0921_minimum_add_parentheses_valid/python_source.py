# -*- coding: utf-8 -*-
"""
Leetcode - Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

Created on Fri Nov 23 00:49:01 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all values of input string.

    Time complexity: O(n)
        - Iteratively traverse all string characters
    Space complexity: O(1)
        - Update constant number of pointers
    """

    def find_min_add_parenthesis(self, s):
        """
        Determines minimum number of additions to balance parentheses.

        :param str s: input string containing parentheses
        :return: number of parentheses required to balance input string
        :rtype: int
        """
        if not s:
            return 0
        
        t = 0
        p = 0
        for c in s:
            if c == "(":
                # Increment counter for unpaired open character
                p += 1
            elif p > 0:
                # Decrement counter for unpaired open character
                p -= 1
            else:
                # Increment total because unpaired close character
                t += 1
        return p + t

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input string containing parentheses
        :rtype: str
        """
        inputs = [x.strip("[]\"\n") for x in sys_stdin]
        s = inputs[0]
        return s


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    s = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .find_min_add_parenthesis(s)
    print(z)


## END OF FILE