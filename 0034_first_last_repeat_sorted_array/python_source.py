# -*- coding: utf-8 -*-
"""
Leetcode Explore - Binary search (first and last position of element in sorted Array)
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Created on Mon Oct 22 18:33:31 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
def find_start(a, x):
    """
    Determines pointer to starting index.

    :type nums: list[int]
    :type a: int
    :rtype: int
    """
    l = 0
    r = len(a) - 1
    # Executes binary search
    while (l + 1) < r:
        m = l + (r - l) // 2
        # Determines first appearance of target
        if (a[m] == x and
            a[m-1] != x):
            return m
        # Determines if target in right-half
        elif a[m] < x:
            l = m + 1
        # Determines if target in left-half
        else:
            r = m
    # Determines target start at left index
    if a[l] == x:
        return l
    # Determines target start at right index
    elif a[r] == x:
        return r
    # Target not found in array
    return -1

def find_end(a, x):
    """
    Determines pointer to end index.

    :type nums: list[int]
    :type a: int
    :rtype: int
    """
    l = 0
    r = len(a) - 1
    # Executes binary search
    while (l + 1) < r:
        m = l + (r - l) // 2
        # Determines first appearance of target
        if (a[m] == x and
            a[m+1] != x):
            return m
        # Determines if target in left-half
        elif a[m] > x:
            r = m
        # Determines if target in right-half
        else:
            l = m + 1
    # Determines target start at right index
    if a[r] == x:
        return r
    # Determines target start at left index
    else:
        return l

class Solution(object):
    def searchRange(self, a, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Checks edge case of empty list
        if len(a) < 1:
            return [-1, -1]
        else:
            # Determines lower limit (and if element exists)
            lim_low = find_start(a, x)
            # Edge case if target not found
            if lim_low == -1:
                return [-1, -1]
            # Determines upper limit
            else:
                lim_high = find_end(a, x)
            return [lim_low, lim_high]

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