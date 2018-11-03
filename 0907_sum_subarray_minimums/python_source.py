# -*- coding: utf-8 -*-
"""
Leetcode - Sum of subarray minimums
https://leetcode.com/problems/sum-of-subarray-minimums
Dynamic programming (tabulation) solution

Created on Thu Oct 25 10:09:55 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution(object):
    def sum_subarray_mins(self, a):
        """
        Sums total of minimum values for each subarray from array "a".
        
        :type arr: list[int]
        :rtype: int
        """
        n = len(a) + 1
        t = [[0] * n for x in range(n)]
        # Prepopulate seed elements
        for x in range(n-1):
            t[x][x+1] = a[x:x+1][0]
        # iterate over list
        for i in range(n)[::-1]:
            for j in range(n):
                if i < j-1:
                    t[i][j] = min(t[i+1][j], t[i][j-1])
        return sum(t[i][j] for i in range(n) for j in range(n) if i < j)

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip("[]\n").split(",") for x in sys_stdin]
    return [int(x) for x in inputs[0]]


if __name__ == "__main__":
    # Imports standard input
    a = stdin(sys.stdin)

    # Evaluates solution
    s = Solution()
    r = s.sum_subarray_mins(a)
    print(r)