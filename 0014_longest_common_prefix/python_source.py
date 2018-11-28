# -*- coding: utf-8 -*-
"""
Leetcode - Longest common prefix
https://leetcode.com/problems/longest-common-prefix

Created on Sat Nov  3 15:29:06 2018
Updated on Tue Nov 27 23:20:20 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over character indicies in array of strings.

    Time complexity: O(n * m)
      - Amortized iterate over all character indicies and input strings
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def longest_common_prefix(self, a):
        """
        Determines the longest common prefix in array of input strings.
        
        :param list[str] a: array of input strings
        :return: substring representing longest common prefix
        :rtype: str
        """
        if len(a) == 0:
            return ""
        elif len(a) == 1:
            return a[0]

        # Determine shortest string
        s = min(a, key = len)

        n = len(a)
        m = len(s)

        for j in range(0, m, 1):
            for i in range(0, n - 1, 1):

                if a[i][j] != a[i + 1][j]:
                    # Found non-matching character
                    return a[i][:j]

        if m > 0:
            # Return shortest string
            return s
        else:
            # Return null string
            return ""

class Solution2:
    """
    Iteration over character indicies in array of strings.

    Time complexity: O(n * m)
      - Amortized iterate over all character indicies and input strings
    Space complexity: O(m)
      - Amortized collect all unique elements for given character index
    """

    def longest_common_prefix(self, a):
        """
        Determines the longest common prefix in array of input strings.

        :param list[str] a: array of input strings
        :return: substring representing longest common prefix
        :rtype: str
        """
        if not a:
            return ""

        # Finds shortest word
        m = min(a, key = len)

        n = len(m)
        for i in range(0, n, 1):
            c = {s[i] for s in a}

            if len(c) > 1:
                return m[:i]
        return m

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of strings
        :rtype: list[str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = []
        else:
            a = [x.strip("\"")
                 for x
                 in inputs[0].split(",")]

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .longest_common_prefix(a)
    print(z)


## END OF FILE