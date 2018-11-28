# -*- coding: utf-8 -*-
"""
Leetcode - Find the Difference
https://leetcode.com/problems/find-the-difference

Created on Sat Nov  3 19:11:50 2018
Updated on Wed Nov 28 12:25:06 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration and bit maniuplation of all string characters using XOR.

    Time complexity: O(n)
      - Amortized iterate over all string characters
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def find_difference(self, s, t):
        """
        Determines unique character using XOR operator.

        :param str s: first input string
        :param str t: second input string
        :return: unique character between both strings
        :rtype: str
        """
        n = len(s)
        c = ord(t[n])

        for i in range(n):
            # Removes duplicate characters using XOR
            c ^= ord(s[i]) ^ ord(t[i])

        return chr(c)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: first and second input strings
        :rtype: tuple[str, str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        s = inputs[0]
        t = inputs[1]

        return s, t


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    s, t = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_difference(s, t)
    print(z)


## END OF FILE