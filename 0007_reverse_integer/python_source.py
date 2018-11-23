# -*- coding: utf-8 -*-
"""
Leetcode - Reverse Integer
https://leetcode.com/problems/reverse-integer

Created on Thu Nov 22 15:28:22 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iterative evaluation of all digits in input integer.

    Time complexity: O(n)
        - Iterate over all digits in input integer
    Space complexity: O(1)
        - Update constant pointers
    """

    def reverse_int(self, x):
        """
        Reverses integer digits if output integer below system integer limits.
        
        :param int x: input signed integer to be reversed
        :return: signed integer with reversed digits
        :rtype: int
        """
        # Check for empty input
        if not x:
            return 0

        # Set sign of input integer
        if x < 0:
            s = -1
        else:
            s = 1
        x *= s

        p = 0
        while x:
            x, r = divmod(x, 10)

            if p > self.max_limit(r, s):
                return 0
            else:
                p = p * 10 + r

        return s * p

    def max_limit(self, r, s):
        """
        Determines maximum integer limit to prevent overflow.
        
        :param int r: integer digit for appending to output integer
        :param int s: signed integer representing sign of input integer
        :return: maximum limit for current output integer
        :rtype: int
        """
        if s > 0:
            return (2 ** 31 - 1 - r) // 10
        else:
            return (2 ** 31 - r) // 10

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: integer whose digits will be reversed
        :rtype: int
        """
        inputs = [x.strip("[]\"\n") for x in sys_stdin]
        x = int(inputs[0])
        return x


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    x = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .reverse_int(x)
    print(z)


## END OF FILE