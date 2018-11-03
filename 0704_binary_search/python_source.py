# -*- coding: utf-8 -*-
"""
Leetcode - Binary search introduction
https://leetcode.com/problems/binary-search
Binary search solution

Created on Sun Oct 21 16:21:01 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution(object):
    def search(self, a, x):
        """
        Determines index of target "x" in sorted array "a".

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(a) == 0:
            return -1
        else:
            l = 0
            r = len(a) - 1
            # Executes binary search
            while l <= r:
                m = l + (r - l) // 2
                # Determines if target found
                if a[m] == x:
                    return m
                # Determines if left-half has target
                elif a[m] < x:
                    l = m + 1
                # Determines if right-half has target
                else:
                    r = m - 1
            # Target not found
            return -1

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip("[]\n").split(",") for x in sys_stdin]
    a = [int(x) for x in inputs[0]]
    x = int(inputs[1][0])
    return a, x


# MAIN MODULE
if __name__ == "__main__":
    a, x = stdin(sys.stdin)

    s = Solution()
    i = s.search(a, x)

    print(i)