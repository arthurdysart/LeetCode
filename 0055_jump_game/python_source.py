# -*- coding: utf-8 -*-
"""
Leetcode - Jump Game
https://leetcode.com/problems/jump-game

Created on Mon Dec 10 13:31:03 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all array elements and ranges of their values.
    Implements greedy algorithm.

    Time complexity: O(n)
      - Iterate over all elements in input array
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def is_jump_arr(self, a):
        """
        Determines whether input jump array can be completely traversed.

        :param list[int] a: input array of integers
        :return: True if array can be traversed completely via jump values
        :rtype: bool
        """
        if not a:
            return True

        p = float("-inf")

        n = len(a)
        for i in range(0, n - 1, 1):

            # Evalaute max number of jumps available at target index
            p = max(p - 1,
                    a[i])

            if p < 1:
                # Not possible to traverse beyond target index
                return False

        return True


class Solution2:
    """
    Iteration over all array elements and ranges of their values.

    Time complexity: O(n * k)
      - Iterate over all elements and ranges of their values
    Space complexity: O(n)
      - Collect all subarray evaluations
    """

    def is_jump_arr(self, a):
        """
        Determines whether input jump array can be completely traversed.

        :param list[int] a: input array of integers
        :return: True if array can be traversed completely via jump values
        :rtype: bool
        """
        if not a:
            return True

        n = len(a)

        # Initialize array cache if subarray can be traversed
        p = [None
             if i != n - 1
             else True
             for i
             in range (0, n, 1)]

        for i in range(n - 2, -1, -1):

            if any(p[i + j]
                   for j
                   in range(a[i], 0, -1)
                   if i + j < n):
                # Set target index as completable subarray
                p[i] = True
            else:
                # Set target index as uncompletable subarray
                p[i] = False

        return p[0]

class Solution3:
    """
    Iteration over all array elements and ranges of their values.

    Time complexity: O(n * k)
      - Iterate over all elements and ranges of their values
    Space complexity: O(n)
      - Collect all subarray evaluations
    """

    def is_jump_arr(self, a):
        """
        Determines whether input jump array can be completely traversed.

        :param list[int] a: input array of integers
        :return: True if array can be traversed completely via jump values
        :rtype: bool
        """
        if not a:
            return True
        elif a[0] == 0:
            return False

        n = len(a)

        # Initialize array cache if subarray can be traversed
        p = [None
             if i != n - 1
             else True
             for i
             in range (0, n, 1)]

        for i in range(n - 2, -1, -1):
            # Evaluate subarray from start in reverse order
            p = self.eval_jump_arr(i, n, p, a)

        return p[0]

    def eval_jump_arr(self, i, n, p, a):
        """
        Determines whether subarray can be completely traversed.

        :param int i: start index of subarray
        :param int n: total number of elements in array
        :param list[bool] p: array cache of subarray evaluations
        :param list[int] a: input array of integers
        :return: updated array cache of subarray evaluations
        :rtype: list[bool]
        """
        if (not p or
            not a):
            return list()

        for j in range(a[i], 0, -1):

            if (i + j < n and
                p[i + j]):
                # Set target index as completable subarray
                p[i] = True
                return p

        # Set target index as uncompletable subarray
        p[i] = False
        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of integers
        :rtype: list[int]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = list()
        else:
            a = [int(x)
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
        .is_jump_arr(a)
    print(z)


## END OF FILE