# -*- coding: utf-8 -*-
"""
Leetcode - Intersection of two arrays
https://leetcode.com/problems/intersection-of-two-arrays
Binary search solution

Created on Sun Oct 28 15:41:45 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
def find_element(x, u):
    """
    Searches for element "x" in array "u".
    
    :type x: int
    :type u: list[int]
    :rtype: bool
    """
    l = 0
    r = len(u) - 1
    while l <= r:
        m = l + (r - l) // 2
        if u[m] == x:
            return True
        elif u[m] < x:
            l = m + 1
        else:
            r = m - 1
    return False

class Solution(object):
    def intersection(self, a, b):
        """
        Determines common elements in arrays "a" and "b".

        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        # Checks for empty arrays
        if (len(a) < 1 or
            len(b) < 1):
            return [-1]

        # Assign smaller array "u" and larger array "v"
        if len(a) < len(b):
            u = list(set(a))
            v = list(set(b))
        else:
            u = list(set(b))
            v = list(set(a))

        # Sorts smaller array "u"
        u.sort()

        # Search smaller array "u" for elements of larger array "v"
        r = [x for x in v if find_element(x, u)]
        return r

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip("[]\n").split(",") for x in sys_stdin]
    a = [int(x) for x in inputs[0]]
    b = [int(x) for x in inputs[1]]
    return a, b


# MAIN MODULE
if __name__ == "__main__":
    a, b = stdin(sys.stdin)

    s = Solution()
    r = s.intersection(a, b)

    print(r)