# -*- coding: utf-8 -*-
"""
Leetcode - Self Dividing Numbers
https://leetcode.com/problems/self-dividing-numbers

Created on Fri Dec 14 21:41:31 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Pythonic iteration over all integers in target range.

    Time complexity: O(n ** m)
      - Amortized iterate over all integers and contained digits
    Space complexity: O(n)
      - Amortized store all integers in range
    """

    def find_self_dividing_nums(self, l, r):
        """
        Determines all self-dividing numbers within target limits (inclusive).

        :param int l: lower limit of target range
        :param int r: upper limit of target range
        :return: array of all self-dividing numbers in range
        :rtype: list[int]
        """
        if (not l or
            not r or 
            r < l):
            return list()

        return [i
                for i
                in range(l, r + 1, 1)
                if self.is_self_dividing(i)]

    def is_self_dividing(self, i):
        """
        Determines whether target integer is self-dividing.

        :param int i: target integer
        :return: True if target integer is self-dividing
        :rtype: bool
        """
        if not i:
            return False

        p = i

        while p > 0:

            # Extract remaining digits and target digit
            p, d = divmod(p, 10)

            if (d == 0 or
                i % d != 0):
                # Found target integer is not self-dividing
                return False

        # Found target integer is self-dividing
        return True

class Solution2:
    """
    Iteration over all integers in range.

    Time complexity: O(n ** m)
      - Amortized iterate over all integers and contained digits
    Space complexity: O(n)
      - Amortized store all integers in range
    """

    def find_self_dividing_nums(self, l, r):
        """
        Determines all self-dividing numbers within target limits (inclusive).

        :param int l: lower limit of target range
        :param int r: upper limit of target range
        :return: array of all self-dividing numbers in range
        :rtype: list[int]
        """
        if (not l or
            not r or 
            r < l):
            return list()

        t = list()

        for i in range(l, r + 1, 1):

            if self.is_self_dividing(i):
                t.append(i)

        return t

    def is_self_dividing(self, i):
        """
        Determines whether target integer is self-dividing.

        :param int i: target integer
        :return: True if target integer is self-dividing
        :rtype: bool
        """
        if not i:
            return False

        p = i

        while p > 0:

            # Extract remaining digits and target digit
            p, d = divmod(p, 10)

            if (d == 0 or
                i % d != 0):
                # Found target integer is not self-dividing
                return False

        # Found target integer is self-dividing
        return True

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: lower and upper limits of target range
        :rtype: tup[int, int]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        l = int(inputs[0])

        r = int(inputs[1])

        return l, r


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    l, r = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_self_dividing_nums(l, r)
    print(z)


## END OF FILE