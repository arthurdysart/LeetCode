# -*- coding: utf-8 -*-
"""
Leetcode - Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array

Created on Sun Nov 18 17:24:12 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Traverse all elements of array.

    Time complexity: O(n)
        - Traverse all array values
    Space complexity: O(1)
        - Constant evaluation of current array pointers
    """

    def is_mountain_array(self, a):
        """
        Determines whether input array is valid mountain array.

        :param list[int] a: array of elevation values
        :return: True if valid mountain array
        :rtype: bool
        """
        n = len(a)
        if n < 3:
            return False
        # Invalidate monotonic slopes
        elif (a[0] > a[1] or
              a[n - 2] < a[n - 1]):
            return False

        p = None
        for i in range(0, n - 1):

            # Search for local maxima
            if p is None:
                if a[i] > a[i + 1]:
                    p = i
                if a[i] == a[i + 1]:
                    return False

            # Confirm maxima as global maxima
            else:
                if a[i] <= a[i + 1]:
                    return False

        return True

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of elevation values
        :rtype: list[int]
        """
        inputs = [x.strip("[]\n") for x in sys_stdin]
        a = [int(x.strip())
             for x
             in inputs[0].split(",")]
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .is_mountain_array(a)
    print(z)


## END OF FILE