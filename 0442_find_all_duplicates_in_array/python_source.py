# -*- coding: utf-8 -*-
"""
Leetcode - Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array

Created on Fri Dec 21 21:39:30 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import defaultdict
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all elements in input array using two-pointers.

    Time complexity: O(n)
      - Iterate over all array elements
    Space complexity: O(1)
      - Update constant number of pointer and update array in-place
    """

    def find_duplicate_vals(self, a):
        """
        Determines array values which occur twice.

        :param list[int] a: input array of integers
        :return: array with duplicate integers
        :rtype: list[int]
        """
        if not a:
            return list()

        t = list()

        n = len(a)
        for i in range(0, n, 1):

            # Set target index
            j = abs(a[i]) - 1

            if a[j] > 0:
                # Modify target value as its negative which indicates visited
                a[j] *= -1

            else:
                # Collect target value because negative indicates duplicate
                t.append(abs(a[i]))

        return t

class Solution1:
    """
    Iteration over all elements in input array using two-pointers.

    Time complexity: O(n)
      - Iterate over all array elements
    Space complexity: O(n)
      - Update hash map of value-counts pairs
    """

    def find_duplicate_vals(self, a):
        """
        Determines array values which occur twice.

        :param list[int] a: input array of integers
        :return: array with duplicate integers
        :rtype: list[int]
        """
        if not a:
            return list()

        c = defaultdict(int)

        t = list()

        n = len(a)
        for i in range(0, n, 1):

            # Set target value
            p = abs(a[i])

            if c[p] < 1:
                # Increment value count
                c[p] += 1

            else:
                # Collect target value
                t.append(p)

        return t

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of integers
        :rtype: tup[int, int]
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
        .find_duplicate_vals(a)
    print(z)


## END OF FILE