# -*- coding: utf-8 -*-
"""
Leetcode - Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/

Created on Sat Jan 12 23:33:20 2019
@author: Arthur Dysart
"""


# REQUIRED MODULES
import json
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Sort all elements of input array.

    Time complexity: O(n * log(n))
      - Sort all array elements
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def find_largest_perimeter(self, a):
        """
        Determines maximum perimeter from possible triangle side lengths.

        :param list[int] a: array of possible triangle side lengths
        :return: maximum triangle perimeter
        :rtype: int
        """
        if not a:
            return 0

        # Sort input array in decreasing order
        a.sort(reverse = True)

        n = len(a)
        for i in range(0, n - 2, 1):

            if self.is_valid_triangle(a, i):
                # Found maximum valid triangle perimeter
                return sum(a[i:i + 3])

        # Valid triangle perimeter not found
        return 0

    def is_valid_triangle(self, a, i):
        """
        Determines if target and two susequent indicies form a valid triangle.
        Note only sum of the smaller lengths needs to be checked.

        :param list[int] a: array of possible triangle side lengths
        :param int i: target index of largest side length
        :return: True if valid triangle lengths
        :rtype: bool
        """
        return a[i + 1] + a[i + 2] > a[i]

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input coordinates and number of output coordinates
        :rtype: list[list[int]], int
        """
        try:
            x = next(sys_stdin)
            a = json.loads(x)
        except:
            a = ""

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_largest_perimeter(a)
    print(json.dumps(z))


## END OF FILE