# -*- coding: utf-8 -*-
"""
Leetcode - Valid parentheses
https://leetcode.com/problems/valid-parentheses

Created on Thu Dec  6 18:48:32 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import deque
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over character indicies in string.

    Time complexity: O(n)
      - Iterate over all characters in string
    Space complexity: O(n)
      - Amortized collect all open parentheses characters
    """

    def is_valid_parentheses(self, s):
        """
        Determines whether string follows valid parentheses heuristics.

        :param str s: input string
        :return: True if string contains all valid parentheses
        :rtype: bool
        """
        if not s:
            return True

        # Initialize hash table for all parentheses types
        p = {"(": ")",
             "[": "]",
             "{": "}"}

        q = deque()

        n = len(s)
        for i in range(0, n, 1):

            if s[i] in p.keys():
                # Collect open parentheses
                q.append(s[i])

            elif s[i] in p.values():

                if (q and
                    p[q[-1]] == s[i]):
                    # Remove complete parentheses pair
                    q.pop()

                else:
                    # Found unpaired parentheses
                    return False

        # Evaluate if all parentheses are paired
        return (not q)

class Solution2:
    """
    Iteration over character indicies in string.

    Time complexity: O(n)
      - Iterate over all characters in string
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def is_valid_parentheses(self, s):
        """
        Determines whether string follows valid parentheses heuristics.

        :param str s: input string
        :return: True if string contains all valid parentheses
        :rtype: bool
        """
        if not s:
            return True

        # initialize counters for all parentheses types
        p1 = 0
        p2 = 0
        p3 = 0

        n = len(s)
        for i in range(0, n, 1):

            # Check if regular parentheses
            if s[i] == "(":
                p1 += 1
            elif s[i] == ")":
                if p1 > 0:
                    # Found unpaired close parentheses
                    p1 -= 1
                    continue
                else:
                    return False

            # Check if square parentheses
            elif s[i] == "[":
                p2 += 1
            elif s[i] == "]":
                if p2 > 0:
                    # Found unpaired close parentheses
                    p2 -= 1
                    continue
                else:
                    return False

            # Check if curly parentheses
            elif s[i] == "{":
                p3 += 1

            elif s[i] == "}":
                if p3 > 0:
                    # Found unpaired close parentheses
                    p3 -= 1
                    continue
                else:
                    return False
            
            # Found non-parenthesis character
            else:
                continue

        # Evaluate if all parentheses are paired
        return (p1 == 0 and
                p2 == 0 and
                p3 == 0)

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


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    s = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_valid_parentheses(s)
    print(z)


## END OF FILE