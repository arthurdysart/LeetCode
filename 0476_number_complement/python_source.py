# -*- coding: utf-8 -*-
"""
Leetcode - Number Complement
https://leetcode.com/problems/number-complement

Created on Sun Nov 25 20:13:47 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from math import log
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Evaluation of binary and decimal conversions.

    Time complexity: O(log(n))
      - Create binary integer from string characters
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def find_complement(self, x):
        """
        Determines complement integer of input integer by binary inversion.

        :param int x: target integer to convert into complement
        :return: complement integer of target integer
        :rtype: int
        """
        if x == 0:
            return 1

        # Determine binary representation of executor
        n = int(log(x, 2)) + 1
        y = "".join("1" for i in range(n))
        # Convert executor to decimal integer
        y = int(y, 2)

        # Determine complement using XOR operator
        return x ^ y

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: target integer
        :rtype: int
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        x = int(inputs[0])

        return x


if __name__ == "__main__":
    # Imports standard input
    x = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_complement(x)
    print(z)