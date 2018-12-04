# -*- coding: utf-8 -*-
"""
Leetcode - Degree of an Array
https://leetcode.com/problems/degree-of-an-array

Created on Mon Dec  3 16:04:11 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import defaultdict
import sys


# MODULE DEFINITIONS
class Solution:
    """
    Iteration over all array elements.

    Time complexity: O(n * m)
      - Amortized iterate over array during search for target element limits
    Space complexity: O(n)
      - Amortized store all elements in element frequency hash map
    """

    def find_shortest_subarray(self, a):
        """
        Determines minimum length of subarray with degree equal to input array.

        :param list[int] a: input array of integers
        :return: minimum subarray length
        :rtype: int
        """
        if not a:
            return 0

        n = len(a)
        p = float("inf")

        # Determine degree of array
        c, d = self.find_arr_degree(n, a)

        # If unit degree, minimum subarray length is 1
        if d == 1:
            return 1

        for v, f in c.items():
            if f == d:
                # For target element, find minimum subarray length
                p = self.find_subarr_len(v, p, n, a)

        if p == float("inf"):
            return 0
        else:
            return p

    def find_arr_degree(self, n, a):
        """
        Determines array degree and counts all element frequencies.

        :param int n: length of input array
        :param list[int] a: input array of integers
        :return: hash map of element frequencies and array degree
        :rtype: tup[dict[int: int], int]
        """
        if not a:
            return 0

        c = defaultdict(int)
        d = float("-inf")

        for i in range(0, n, 1):
            c[a[i]] += 1
            d = max(d, c[a[i]])

        return c, d
    
    def find_subarr_len(self, v, p, n, a):
        """
        Determines minimum length of valid subarray with target element.

        :param int v: target element
        :param int p: pointer for minimum subarray length
        :param int n: length of input array
        :param list[int] a: input array of integers
        :return: updated pointer for minimum subarray length
        :rtype: int
        """
        l = 0
        r = n - 1

        while (l < n - 1 and
               a[l] != v):
            l += 1

        while (r > l and
               a[r] != v):
            r -= 1

        p = min(r - l + 1,
                p)
        
        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of integers
        :rtype: list[int]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = list()
        else:
            a = [int(x)
                 for x
                 in inputs[0].split(",")]
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_shortest_subarray(a)
    print(z)


## END OF FILE