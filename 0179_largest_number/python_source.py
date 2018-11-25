# -*- coding: utf-8 -*-
"""
Leetcode - Minimum Increment to Make Array Unique
https://leetcode.com/problems/minimum-increment-to-make-array-unique

Created on Sun Nov 25 17:04:16 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over array interpolating insertion sort algorithm.

    Time complexity: O(n ** 2)
      - Amortized traverse and sort all array elements
    Space complexity: O(1)
      - Amortized sort array in-place and update constant pointers
    """

    def find_largest_number(self, a):
        """
        Determine largest integer from array element concatenation.

        :param list[int] a: input array of integers
        :return: string representing largest possible integer
        :rtype: str
        """
        if not a:
            return ""

        n = len(a)
        a = [str(x) for x in a]

        for i in range(1, n, 1):
            self.insert_pivot(i, a)
        
        # Concatenate to string and remove leading zeroes
        s = "".join(a)\
            .lstrip("0")

        if len(s) == 0:
            return "0"
        else:
            return s

    def insert_pivot(self, i, a):
        """
        Insert pivot into array to maximize concatenated string value.
        Interpolates "insertion sort" algorithm.
        
        :param int i: index of pivot value
        :param list[int] a: input array of integers
        :return: None (array sorted in-place)
        :rtype: None
        """
        if not a:
            return ""

        # Set pivot value
        p = a[i]

        for j in range(i - 1, -1, -1):
            # Concatenate trailing with pivot
            u = "".join([a[j], p])
            # Concatenate leading with pivot
            v = "".join([p, a[j]])
            if u > v:
                a[j + 1] = p
                return None
            else:
                a[j + 1] = a[j]

        # Insert pivot at array start
        a[0] = p
        return None

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
            a = []
        else:
            a = [int(x)
                 for x
                 in inputs[0].split(",")]

        return a


if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_largest_number(a)
    print(z)