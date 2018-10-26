# -*- coding: utf-8 -*-
"""
Leetcode Explore - Find peak element
https://leetcode.com/problems/find-peak-element
Binary search solution

Created on Mon Oct 22 10:51:08 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
class Solution(object):
    def find_peak_element(self, a):
        """
        Searches for any local maxima using binary search.
        
        :type nums: list[int]
        :rtype: int
        """
        if len(a) == 0:
            return 0
        else:
            l = 0
            r = len(a) - 1
            # Executes binary search
            while l < r:
                m = l + (r - l) // 2
                # Determines local maxima
                if (a[m] > a[m+1] and
                    a[m] > a[m-1]):
                    return m
                # Determines direction to maxima
                else:
                    if a[m] > a[m+1]:
                        # Searches left-half
                        r = m - 1
                    else:
                        # Searches right-half
                        l = m + 1
            # Determines if left bound is maxima
            if a[l] >= a[r]:
                return l
            # Determines right bound is maxima
            else:
                return r

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    input = [x.strip("[]\n").split(",") for x in sys_stdin]
    return [int(x) for x in input[0]]


# MAIN MODULE
if __name__ == "__main__":
    a = stdin(sys.stdin)
    
    s = Solution()
    i = s.find_peak_element(a)

    print(i)