# -*- coding: utf-8 -*-
"""
Leetcode - Word pattern
https://leetcode.com/problems/word-pattern

Created on Sat Nov  3 17:45:22 2018
Updated on Wed Nov 28 11:55:19 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over character indicies in string.

    Time complexity: O(n)
      - Amortized iterate over all characters in pattern
    Space complexity: O(n)
      - Amortized store all forward and backward pattern-substring pairs
    """

    def word_pattern(self, x, s):
        """
        Determines whether words in string follows target pattern.
        
        :param str x: target pattern for string
        :param str s: substrings as words
        :return: True if substrings follow target pattern
        :rtype: bool
        """
        if (not x or
            not s):
            return False

        # Split string into substrings as words
        s = s.split()
        if len(s) != len(x):
            return False

        a = dict()
        b = dict()

        n = len(x)
        for i in range(0, n, 1):
            # Check pattern maps to string
            if x[i] not in a:
                a[x[i]] = s[i]
            elif a[x[i]] != s[i]:
                return False

            # Check string maps to pattern
            if s[i] not in b:
                b[s[i]] = x[i]
            elif b[s[i]] != x[i]:
                return False

        # Found valid word pattern
        return True

class Solution2:
    """
    Check whether pattern and input string are an isomorphic pair.

    Time complexity: O(n)
      - Amortized iterate over all pattern characters and string substrings
    Space complexity: O(n)
      - Amortized store all unique pattern characters and string substrings
    """

    def word_pattern(self, pattern, string):
        """
        Determines whether words in string follows target pattern.

        :param str pattern: target pattern for string
        :param str string: substrings as words
        :return: True if substrings follow target pattern
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

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: target pattern and input string
        :rtype: tuple[str, str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        x = inputs[0]
        s = inputs[1]

        return x, s

if __name__ == "__main__":
    # Imports standard input
    x, s = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .word_pattern(x, s)
    print(z)