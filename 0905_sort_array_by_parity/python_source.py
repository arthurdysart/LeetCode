# -*- coding: utf-8 -*-
"""
Leetcode - Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity

Created on Tue Dec 18 22:43:45 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all elements in input array using two-pointers.

    Time complexity: O(n)
      - Iterate over all array elements
    Space complexity: O(1)
      - Sort array in-place
    """

    def sort_parity(self, a):
        """
        Sorts input array with even elements before odd elements.

        :param list[int] a: input array of integers
        :return: array sorted by parity
        :rtype: list[int]
        """
        if not a:
            return list()

        n = len(a)

        r = n - 1
        for l in range(0, n, 1):

            if a[l] % 2 == 1:
                # Found odd left value

                while (a[r] % 2 == 1 and
                       r > l):
                        # Decrement while odd right value before parity index
                        r -= 1

                if r > l:
                    # Swap odd left and even right elements
                    a[l], a[r] = a[r], a[l]

                else:
                    # Complete parity sort
                    return a

        return a

class Solution1:
    """
    Iteration over all elements in input array.

    Time complexity: O(n)
      - Iterate over all array elements
    Space complexity: O(n)
      - Collect all elements in output arrays
    """

    def sort_parity(self, a):
        """
        Sorts input array with even elements before odd elements.

        :param list[int] a: input array of integers
        :return: array sorted by parity
        :rtype: list[int]
        """
        if not a:
            return list()

        e = list()
        o = list()

        n = len(a)

        for i in range(0, n, 1):

            if a[i] % 2 == 0:
                e.append(a[i])

            else:
                o.append(a[i])

        e.extend(o)
        return e

class Solution2:
    """
    Pythonic iteration over all elements in input array.

    Time complexity: O(n)
      - Iterate over all array elements
    Space complexity: O(n)
      - Collect all elements in output arrays
    """

    def sort_parity(self, a):
        """
        Sorts input array with even elements before odd elements.

        :param list[int] a: input array of integers
        :return: array sorted by parity
        :rtype: list[int]
        """
        if not a:
            return list()

        n = len(a)

        # Collect all even elements
        e = [a[i]
             for i
             in range(0, n, 1)
             if a[i] % 2 == 0]

        # Collect all odd elements
        o = [a[i]
             for i
             in range(0, n, 1)
             if a[i] % 2 == 1]

        e.extend(o)
        return e

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: target integer sum
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
        .sort_parity(a)
    print(z)


## END OF FILE