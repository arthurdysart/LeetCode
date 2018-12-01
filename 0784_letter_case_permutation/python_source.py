# -*- coding: utf-8 -*-
"""
Leetcode - Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation

Created on Fri Nov 30 22:20:04 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import deque
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Breadth first traversal (BFT) over all string permutations.

    Time complexity: O(2 ** n)
      - Iterate over all string permutations
    Space complexity: O(2 ** n)
      - Collect all string permutations
    """

    def permute_letter_case(self, s):
        """
        Collects permutations with upper or lower case alphabetical characters.

        :param str s: input string
        :return: list of all string permutations
        :rtype: list[str]
        """
        if not s:
            return list([""])

        t = deque([s])

        n = len(s)
        for i in range(0, n, 1):
            if s[i].isalpha():
                # Update queue permutations at target index
                t = self.eval_char_loc(i, t)

        return list(t)

    def eval_char_loc(self, i, t):
        """
        Evaluates collected permutations at target string index "i".

        :param int i: target string index
        :param deque[str] t: queue of collected permutations
        :return: updated queue with collected permutations
        :rtype: deque[str]
        """
        if not t:
            return deque()

        m = len(t)
        for j in range(0, m, 1):

            p = t.popleft()

            # Evaluate lowercase string
            l = [p[:i],
                 p[i].lower(),
                 p[i + 1:]]
            t.append("".join(l))

            # Evaluate uppercase string
            r = [p[:i],
                 p[i].upper(),
                 p[i + 1:]]
            t.append("".join(r))

        return t

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
        .permute_letter_case(s)
    print(z)


## END OF FILE