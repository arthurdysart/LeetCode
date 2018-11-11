# -*- coding: utf-8 -*-
"""
Leetcode - Reorder Log Files
https://leetcode.com/problems/reorder-log-files

Created on Sun Nov 11 14:28:21 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iterative solution across all logs
    Time complexity: O(len(s))
        - Iterate through all logs
    Space complexity: O(len(s))
        - Amortized store all logs as either digit or letter logs
    """

    def reorder_log_files(self, a):
        """
        Reorders logs according to content and alphanumeric identifier.

        :param list[str] a: list of log-like strings
        :return: sorted list of logs
        :rtype: list[str]
        """
        # Initialize letter "a_a" and digit "a_n" logs
        a_a = list()
        a_n = list()

        # Categorize each log
        for s in a:
            s = s.split()
            if s[1].isdigit():
                s = " ".join(s)
                a_n.append(s)
            else:
                s = s[0], " ".join(s[1:])
                a_a.append(s)

        # Sort letter logs
        a_a = sorted(a_a, key=lambda x: (x[1], x[0]))
        a_a = [" ".join(s) for s in a_a]

        return a_a + a_n


class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: characteristic factor for spiral matrix
        :rtype: int
        """
        inputs = [x for x in sys_stdin]
        a = inputs[0].strip("[]\n\"").split("\",\"")
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .reorder_log_files(a)
    print(z)


## END OF FILE