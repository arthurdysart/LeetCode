# -*- coding: utf-8 -*-
"""
Leetcode - Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

Created on Sat Nov 17 14:34:43 2018
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
        - Requires constant pointers
    """
    
    def maximize_profit(self, a):
        """
        Maximize profit by identifying purchase and sell date.

        :param list[int] a: array of stock prices
        :return: maximum profit from stock transactions
        :rtype: int
        """
        if len(a) < 2:
            return 0

        p = 0
        l = None
        r = None
        n = len(a)
        for i in range(n - 1):
            if l is None:
                # Evaluate purchase on current day
                if a[i] < a[i + 1]:
                    l = a[i]

            if (l is not None and
                r is None):
                # When purchase completed, evaluate sell on current day
                if a[i] > a[i + 1]:
                    r = a[i]

            if (l is not None and
                r is not None):
                # Calculate profit, reset pointers
                p += r - l
                l = None
                r = None

        if (l is not None and
            r is None):
            # Determine if last day price greater than purchase price
            if a[n - 1] > l:
                # Calculate profit
                p += a[n - 1] - l

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of stock prices
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
        .maximize_profit(a)
    print(z)


## END OF FILE