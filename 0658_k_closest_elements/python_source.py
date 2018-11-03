# -*- coding: utf-8 -*-
"""
Leetcode - Find k closest elements
https://leetcode.com/problems/find-k-closest-elements
Binary search solution

Created on Sat Oct 27 22:16:25 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution(object):
    def find_closest_elements(self, a, k, x):
        """
        Finds elements in array "a" with values closest to target "x".
        
        :type a: list[int]
        :type k: int
        :type x: int
        :rtype: list[int]
        """
        if (len(a) < 1 or
            len(a) < k):
            return [-1]
        else:
            l = 0
            r = len(a) - k
            # Executes binary search
            while l < r:
                m = l + (r - l) // 2
                if abs(x - a[m]) > abs(x - a[m+k]):
                    l = m + 1
                else:
                    r = m
            return a[l:l+k]

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip("[]\n").split(",") for x in sys_stdin]
    a = [int(x) for x in inputs[0]]
    k = int(inputs[1][0])
    x = int(inputs[2][0])
    return a, k, x


if __name__ == "__main__":
    # Imports standard input
    a, k, x = stdin(sys.stdin)

    # Evaluates solution
    s = Solution()
    r = s.find_closest_elements(a, k, x)
    print(r)