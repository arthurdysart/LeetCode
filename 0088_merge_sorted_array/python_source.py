# -*- coding: utf-8 -*-
"""
Leetcode - Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Created on Mon Jan 14 14:05:13 2019
@author: Arthur Dysart
"""


# REQUIRED MODULES
import json
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iterative traversal of first input array.

    Time complexity: O(n + m)
      - Amortized traverse first and second list elements
    Space complexity: O(1)
      - Update first array in-place
    """

    def merge_sort_arr(self, a, m, b, n):
        """
        Combines and sorts elements from both input arrays in-place.

        :param list[int] a: first array of integer values
        :param int m: number of elements in first array
        :param list[int] b: second array of integer values
        :param int n: number of elements in second array
        :return: None
        :rtype: None
        """
        if not b:
            return None

        while (m > 0 and
               n > 0):
            # Iterate while remaining indicies in both arrays

            if a[m - 1] < b[n - 1]:
                # Insert target value and shifted values into first array
                a[m:] = [b[n - 1]] + a[m:-1]

                # Decrement counter for first array                
                n -= 1

            else:
                # Decrement counter for second array
                m -= 1

        if n > 0:
            # Insert remaining elements before first array elements
            a[:] = b[:n] + a[:-n]

        return None

class Solution1:
    """
    Iterative traversal of first input array.

    Time complexity: O(n + m)
      - Amortized traverse first and second list elements
    Space complexity: O(1)
      - Update first array in-place
    """

    def merge_sort_arr(self, a, m, b, n):
        """
        Combines and sorts elements from both input arrays in-place.

        :param list[int] a: first array of integer values
        :param int m: number of elements in first array
        :param list[int] b: second array of integer values
        :param int n: number of elements in second array
        :return: None
        :rtype: None
        """
        if not b:
            return None

        i = 0
        j = 0

        while m > 0 and n > 0:

            if a[i] > b[j]:
                # Insert target element into first array
                self.insert_shift_arr(i, j, a, b)

                # Update index pointer and counter for second array
                j += 1
                n -= 1

            else:
                # Update counter for first array
                m -= 1

            # Increment index pointer for first array
            i += 1

        while n > 0:

            # Insert target element into first array
            a[i] = b[j]

            # Update counter for second array
            n -= 1

            # Increment index pointers for both arrays
            i += 1
            j += 1

        return None

    def insert_shift_arr(self, i, j, a, b):
        """
        Combines and sorts elements from both input arrays in-place.

        :param int i: target index in first array
        :param int j: target index in second array
        :param list[int] a: first array of integer values
        :param list[int] b: second array of integer values
        :return: None
        :rtype: None
        """
        p = b[j]

        for x in range(i, len(a), 1):
            a[x], p = p, a[x]

        return None

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input arrays and their number of elements
        :rtype: list[int], int, list[int], int
        """
        return [json.loads(x)
                for x 
                in sys_stdin]


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a, m, b, n = Input()\
                 .stdin(sys.stdin)

    # Evaluates solution
    Solution()\
    .merge_sort_arr(a, m, b, n)

    print(json.dumps(a))


## END OF FILE