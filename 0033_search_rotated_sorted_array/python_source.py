# -*- coding: utf-8 -*-
"""
Leetcode Explore - Search in rotated sorted array
https://leetcode.com/problems/search-in-rotated-sorted-array
Binary search solution

Created on Sun Oct 21 21:51:28 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
class Solution:
    def search(self, a, x):
        """
        Finds index of target value in sorted-then-pivoted array.
        
        :type a: list[int]
        :type x: int
        :rtype: int
        """
        # Edge case of empty array
        if not a:
            return -1

        l = 0
        r = len(a) - 1
        while l <= r:
            # Performs binary search
            m = l + (r - l) // 2
            if a[m] == x:
                return m
            elif a[l] <= a[m]:
                # Left-half retains ascending sort
                if (x >= a[l] and
                    x <= a[m]):
                    # Searches left-half
                    r = m - 1
                else:
                    # Searches right-half
                    l = m + 1
            else:
                # Right-half retains ascending sort
                if (x >= a[m] and
                    x <= a[r]):
                    # Searches right-half
                    l = m + 1
                else:
                    # Searches left-half
                    r = m - 1
        # Determines target not in array
        return -1

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip("[]\n") for x in sys_stdin]
    a = [int(x) for x in inputs[0].split(",")]
    x = int(inputs[1][0])
    return a, x


# MAIN MODULE
if __name__ == "__main__":
    a, x = stdin(sys.stdin)

    s = Solution()
    i = s.search(a, x)

    print(i)