# -*- coding: utf-8 -*-
"""
Leetcode - Reverse words in a string
https://leetcode.com/problems/reverse-words-in-a-string
Pythonic solution

Created on Sat Nov  3 16:11:58 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    def reverse_words(self, s):
        """
        Reverses order of words in string "s".

        :type s: str
        :rtype: bool
        """
        return " ".join(reversed(s.strip().split()))

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    return [x for x in sys_stdin][0]


if __name__ == "__main__":
    # Imports standard input
    s = stdin(sys.stdin)
    
    # Evaluates solution
    r = Solution()\
        .reverse_words(s)
    print(r)