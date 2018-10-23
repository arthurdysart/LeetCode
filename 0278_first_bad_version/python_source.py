# -*- coding: utf-8 -*-
"""
Leetcode Explore - Binary search (first bad version)
https://leetcode.com/problems/first-bad-version/

Created on Sun Oct 21 17:02:27 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
def is_bad_version(m, x):
    """
    Evaluates version quality.
    
    :type m: int
    :type x: int
    :rtype: bool
    """
    if m >= x:
        return True
    else:
        return False

class Solution(object):
    def first_bad_version(self, n, x):
        """
        Determines first failed version relative to target version "x".

        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        else:
            l = 1
            r = n
            while l < r:
                m = l + (r - l)//2
                # Executes binary search
                if (is_bad_version(m, x) == True and
                    is_bad_version(m-1, x) == False):
                    return m
                elif is_bad_version(m-1, x) == True:
                    r = m - 1
                else:
                    l = m + 1
            
            if (is_bad_version(l, x) == True):
                return l
            if (is_bad_version(l, x) == False and
                is_bad_version(r, x) == True):
                return r
            return -1

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    return [int(x.strip()) for x in sys_stdin]


# MAIN MODULE
if __name__ == "__main__":
    n, x = stdin(sys.stdin)

    s = Solution()
    i = s.first_bad_version(n, x)

    print(i)