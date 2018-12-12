# -*- coding: utf-8 -*-
"""
Leetcode - To Lower Case
https://leetcode.com/problems/to-lower-case

Created on Tue Dec 11 21:53:48 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Pythonic iteration over all characters in string.

    Time complexity: O(n)
      - Iterate over all characters in string
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def make_lower_case(self, s):
        """
        Transforms input string into lowercase.

        :param str s: input string
        :return: transformed string in lowercase
        :rtype: str
        """
        if not s:
            return ""

        return "".join(c.lower()
                       for c
                       in s)

class Solution2:
    """
    Iteration over all characters in string.

    Time complexity: O(n)
      - Iterate over all characters in string
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def make_lower_case(self, s):
        """
        Transforms input string into lowercase.

        :param str s: input string
        :return: transformed string in lowercase
        :rtype: str
        """
        if not s:
            return ""

        return "".join(chr(ord(c) + 32)
                       if (ord(c) > 64
                       and ord(c) < 91)
                       else c
                       for c
                       in s)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input string
        :rtype: str
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        s = inputs[0]

        return s


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    s = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .make_lower_case(s)
    print(z)


## END OF FILE