# -*- coding: utf-8 -*-
"""
Leetcode - Find the Difference
https://leetcode.com/problems/find-the-difference
Bit manipulation solution

Created on Sat Nov  3 19:11:50 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    def find_difference(self, s, t):
        """
        Determines unique character using XOR operator.
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        c = ord(t[n])
        for i in range(n):
            # Removes duplicate characters using XOR
            c ^= ord(s[i]) ^ ord(t[i])
        return chr(c)

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip() for x in sys_stdin]
    s = inputs[0]
    t = inputs[1]
    return s, t


if __name__ == "__main__":
    # Imports standard input
    s, t = stdin(sys.stdin)

    # Evaluates solution
    r = Solution()\
        .find_difference(s, t)
    print(r)