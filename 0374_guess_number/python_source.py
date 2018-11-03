# -*- coding: utf-8 -*-
"""
Leetcode - Number guessing
https://leetcode.com/problems/guess-number-higher-or-lower
Binary search solution

Created on Sun Oct 21 15:50:50 2018
@author: Arthur Dysart
"""

# IMPORTED LIBRARIES
import sys


# FUNCTION DEFINITIONS
def guess(m, x):
    """
    Determines accuracy of individual guess "m" relative to target "s".

    :type m: int
    :type x: int
    :rtype: int
    """
    if m == x:
        return 0
    elif m > x:
        return -1
    else:
        return 1

class Solution(object):
    def guess_number(self, n, x):
        """
        Determines guessed integer using binary search.
    
        :type n: int
        :type x: int
        :rtype: int
        """
        # Checks for valid input
        if n <= 0:
            return 0
        else:
            l = 1
            r = n
            # Executes binary search
            while l <= r:
                m = l + (r - l) // 2
                g = guess(m, x)
                # Determines if target found
                if g == 0:
                    return m
                # Searches right-half
                elif g == 1:
                    l = m + 1
                # Searches left-half
                else:
                    r = m - 1
            # Target not found
            return 0

def stdin(sys_stdin):
    """
    Imports standard input.
    
    :type sys_stdin: list
    :rtype: list
    """
    return [int(x) for x in sys_stdin]


if __name__ == "__main__":
    n, x = stdin(sys.stdin)
    
    s = Solution()
    i = s.guess_number(n, x)
    
    print(i)