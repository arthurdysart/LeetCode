# -*- coding: utf-8 -*-
"""
Leetcode - Two Sum II
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

Created on Sun Nov 18 20:39:12 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    One-pointer with binary search of sorted array.

    Time complexity: O(n)
        - Amortized iterate over all elements in array
    Space complexity: O(1)
        - Constant pointer evaluation
    """

    def two_sum(self, a, x):
        """
        Determines indicies of elements whose sum equals target "x".

        :param list[int] a: sorted array of integers
        :type int x: target integer sum
        :return: list of indicies (base index 1) of target values
        :rtype: list[int]
        """
        if not a:
            return [-1, -1]

        n = len(a)
        for i in range(n):
            t = x - a[i]
            
            j = self.find_target(t, i, n, a)
            if j != 0:
                return [i + 1, j + 1]

        return [-1, -1]

    def find_target(self, t, i, n, a):
        """
        Searches for target "t" by binary search of right-section array.

        :param int t: target integer for two sum
        :param int i: lower limit of binary search range
        :param int n: length of input array
        :param list[int] a: sorted array of integers
        :return: integer representing index of target element
        :rtype: int
        """
        if (not a or
            not n):
            return 0

        # Execute binary search
        l = i + 1
        r = n - 1
        while l <= r:
            m = l + (r - l) // 2
            if a[m] == t:
                # Target element found
                return m
            elif a[m] < t:
                # Target element in right-half
                l = m + 1
            else:
                # Target element in left-half
                r = m - 1

        return 0

class Solution2:
    """
    One-pointer unitary search of sorted array (with memoization).

    Time complexity: O(n)
        - Amortized iterate over all elements in array
    Space complexity: O(1)
        - Constant pointer evaluation
    """

    def two_sum(self, a, x):
        """
        Determines indicies of elements whose sum equals target "x".

        :param list[int] a: sorted array of integers
        :type int x: target integer sum
        :return: list of indicies (base index 1) of target values
        :rtype: list[int]
        """
        if not a:
            return [-1, -1]

        c = {}
        n = len(a)
        for j in range(n):
            # Set target element
            t = x - a[j]
            if t in c:
                # Complimentary element found
                i = c[t]
                return [i + 1, j + 1]
            else:
                # Add visited integer to dictionary
                c[a[j]] = j

        return [-1, -1]



class Solution3:
    """
    Two-pointer unitary search of sorted array.

    Time complexity: O(n)
        - Amortized iterate over all elements in array
    Space complexity: O(1)
        - Constant pointer evaluation
    """

    def two_sum(self, a, x):
        """
        Determines indicies of elements whose sum equals target "x".

        :param list[int] a: sorted array of integers
        :type int x: target integer sum
        :return: list of indicies (base index 1) of target values
        :rtype: list[int]
        """
        if not a:
            return [-1, -1]

        n = len(a)
        l = 0
        r = n - 1
        # Perform two-pointer search
        while l < r:
            # Set current sum
            t = a[l] + a[r]
            if t == x:
                # Target indicies found
                return [l + 1, r + 1]
            if t > x:
                r -= 1
            else:
                l += 1

        # Target indicies not found        
        return [-1, -1]

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: sorted array of integers and target integer sum
        :rtype: tuple[list[int], int]
        """
        inputs = [x.strip("[]\n") for x in sys_stdin]
        a = [int(x.strip())
             for x
             in inputs[0].split(",")]
        x = int(inputs[1])
        return a, x


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a, x = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .two_sum(a, x)
    print(z)


## END OF FILE