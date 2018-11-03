# -*- coding: utf-8 -*-
"""
Leetcode - Valid palindrome
https://leetcode.com/problems/valid-palindrome
Two pointer (merging) solution

Created on Sat Nov  3 15:47:03 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    def is_palindrome(self, s):
        """
        Determines if alphanumeric characters in string "s" constitute a palindrome.

        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        else:
            # Initializes left start and end pointers
            l = 0
            r = len(s) - 1
            while l < r:
                if not s[l].isalnum():
                    l += 1
                elif not s[r].isalnum():
                    r -= 1
                elif s[l].upper() != s[r].upper():
                    return False
                else:
                    l += 1
                    r -= 1
            return True

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
        .is_palindrome(s)
    print(r)