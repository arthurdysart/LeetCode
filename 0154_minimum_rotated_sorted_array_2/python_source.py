# -*- coding: utf-8 -*-
"""
Leetcode - Minimum in rotated sorted array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
Binary search solution

Created on Sun Oct 28 15:12:36 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
class Solution(object):
    def find_min(self, a):
        """
        Determines minimum in rotated sorted array using binary search.

        :type a: List[int]
        :rtype: int
        """
        # Determines if empty list
        if len(a) < 1:
            return -1
        else:
            l = 0
            r = len(a) - 1
            # Executes binary search
            while l < r:
                m = l + (r - l) // 2
                # Determines if element a[m] is least element
                if (a[m] < a[m-1] and
                    a[m] < a[m+1]):
                    return a[m]
                # Searches right-half if contains smaller
                elif a[m] > a[r]:
                    l = m + 1
                # Searches left-half since contains smaller
                else:
                    if a[m] == a[r]:
                        r = r - 1
                    else:
                        r = m
            if a[r] <= a[l]:
                return a[r]
            elif a[l] < a[r]:
                return a[l]
            return -1

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip("[]\n").split(",") for x in sys_stdin]
    return [int(x) for x in inputs[0]]


# MAIN MODULE
if __name__ == "__main__":
    a = stdin(sys.stdin)

    s = Solution()
    x = s.find_min(a)

    print(x)