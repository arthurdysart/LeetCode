# -*- coding: utf-8 -*-
"""
Leetcode - Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square

Created on Fri Nov 23 20:18:24 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Binary search for target element.
    
    Time complexity: O(log(n))
      - Iteratively search half array with binary search
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def is_perfect_square(self, n):
        """
        Determines whether target integer is a perfect square.
        :param int n: target integer
        :return: True if target integer is a perfect square
        :rtype: bool
        """
        if n == 0:
            return False

        l = 1
        r = n - 1
        while l <= r:
            # Execute binary search
            m = l + (r - l) // 2
            if m * m == n:
                return True
            elif m * m > n:
                r = m - 1
            else:
                l = m + 1

        if l * l == n:
            return True
        else:
            return False

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.
    
        :param _io.TextIOWrapper sys_stdin: standard input
        :return: target integer
        :rtype: int
        """
        inputs = [x.strip("[]\n")
                  for x
                  in sys_stdin]
        n = int(inputs[0])
        return n


if __name__ == "__main__":
    # Imports standard input
    n = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_perfect_square(n)
    print(z)