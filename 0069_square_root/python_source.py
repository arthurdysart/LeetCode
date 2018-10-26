# -*- coding: utf-8 -*-
"""
Leetcode Explore - Square root
https://leetcode.com/problems/sqrtx
Binary search solution

Created on Thu Oct 18 09:24:30 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
class Solution(object):
    def square_root(self, n):
        """
        Iteratively searches for integer solution to square-root of target "x".
        Integer estimate of sqrt(x) must satisfy: m**2 <= x < (m+1)**2
        
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        else:
            l = 0
            r = n
            while l <= r:
                # Sets pointer "m" and next pointer "n"
                m = l + (r - l) // 2
                low = m * m
                high = (m + 1) * (m + 1)
                if (n >= low and
                    n < high):
                    # Target "x" is between m^2 and (m+1)^2
                    return m
                elif n < low:
                    # Target "x" is less than m^2
                    r = m - 1
                else:
                    # Target "x" is greater than m^2
                    l = m + 1
            # Target not found
            return -1

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    return [int(x) for x in sys_stdin][0]


# MAIN MODULE
if __name__ == "__main__":
    n = stdin(sys.stdin)

    s = Solution()
    x = s.square_root(n)

    print(x)