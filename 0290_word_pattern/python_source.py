# -*- coding: utf-8 -*-
"""
Leetcode - Word pattern
https://leetcode.com/problems/word-pattern
Pythonic solution

Created on Sat Nov  3 17:45:22 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution(object):
    def word_pattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # Checks empty pattern or string
        if (not string or
            not pattern):
            return False

        strings = string.split()
        unique_strings = set(strings)
        unique_patterns = set(pattern)
        pairs = set(zip(pattern,
                        strings))

        # Determines equal number of total patterns and total strings
        if (len(pattern) != len(strings) or
        # Determines equal number of unique patterns and unique strings
            len(unique_patterns) != len(unique_strings) or
        # Determines equal number of unique patterns and pattern-string pairs
            len(unique_patterns) != len(pairs)):
            return False
        else:
            # Identifies match between pattern and input string
            return True

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip() for x in sys_stdin]
    p = inputs[0]
    s = inputs[1]
    return p, s


if __name__ == "__main__":
    # Imports standard input
    p, s = stdin(sys.stdin)
    
    # Evaluates solution
    r = Solution()\
        .word_pattern(p, s)
    print(r)