# -*- coding: utf-8 -*-
"""
Leetcode - Find Duplicate File in System
https://leetcode.com/problems/find-duplicate-file-in-system

Created on Tue Nov 27 22:11:24 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import defaultdict
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration and parsing of input strings.

    Time complexity: O(n * m)
      - Iterate over all path groups and file name-content pair strings
    Space complexity: O(m)
      - Collect all absolute file paths in paths dictionary
    """

    def find_duplicates(self, a):
        """
        Reports absolute paths for duplicate files grouped by file contents.

        :param list[str] a: array of input file paths
        :return: array of absolte file paths grouped by file contents
        :rtype: list[list[str]]
        """
        d = defaultdict(list)

        for p in a:
            s = p.split(" ")
            # Separate parent directory path
            r = s[0]

            for f in s[1:]:
                # Separate file name and contents
                n, c = f.rstrip(")").split("(")
                # Record full path by file contents
                d[c].append("/".join([r, n]))

        # Collect groups only with multiple paths
        t = [x
             for x
             in d.values()
             if len(x) > 1]

        return t

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of strings representing directory paths and files
        :rtype: list[str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = []
        else:
            a = [x
                 for x
                 in inputs[0].split("\", \"")]

        return a


if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_duplicates(a)
    print(z)