# -*- coding: utf-8 -*-
"""
Leetcode - Reverse words in a string
https://leetcode.com/problems/reverse-words-in-a-string

Created on Sat Nov  3 16:11:58 2018
Updated on Wed Nov 28 00:51:34 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
class Solution:
    """
    Iteration over character indicies in string.

    Time complexity: O(n)
      - Iterate over all characters in string
    Space complexity: O(n)
      - Amortized add all substrings of input string to output list
    """

    def reverse_words(self, s):
        """
        Reverses order of words in input string.

        :param str s: input string
        :return: string with reversed word order
        :rtype: str
        """
        if len(s) == 0:
            return ""

        n = len(s)
        t = list()

        l = 0
        while l < n:

            # Find next valid starting character
            while (l < n and
                   s[l].isspace()):
                l += 1

            # Find end of substring
            r = l
            while (r < n and
                   not s[r].isspace()):
                r += 1

            # Add substring if not empty
            if s[l:r]:
                t.append(s[l:r])

            # Increment starting index
            l = r + 1

        return " ".join(reversed(t))

class Solution2:
    """
    Pythonic string manipulation.

    Time complexity: O(n)
      - Iterate over all characters in string
    Space complexity: O(n)
      - Amortized add all substrings of input string to temporary list
    """

    def reverse_words(self, s):
        """
        Reverses order of words in input string.
        
        :param str s: input string
        :return: string with reversed word order
        :rtype: str
        """
        return " ".join(reversed(s.strip().split()))

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


if __name__ == "__main__":
    # Imports standard input
    s = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .reverse_words(s)
    print(z)