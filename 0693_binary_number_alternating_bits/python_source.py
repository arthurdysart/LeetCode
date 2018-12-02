# -*- coding: utf-8 -*-
"""
Leetcode - Binary Number with Alternating Bits
https://leetcode.com/problems/binary-number-with-alternating-bits

Created on Sun Dec  2 14:39:53 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Evaluation of bitwise manipulations using XOR, RIGHT SHIFT, and AND.

    Time complexity: O(1)
      - Evaluate constant number of expressions
    Space complexity: O(1)
      - Update constant number of pointers
    """
    def is_binary_alt_bit(self, n):
        """
        Determines whether target integer has alternating bits in binary.
        Note valid integers belong to [Lichtenberg sequence](oeis.org/A000975).

        :param int n: target integer
        :return: True if target integer has alternating bits in binary
        :rtype: bool
        """
        if n < 2:
            return True

        # If alternating bits (binary), yield all 1 bits (binary)
        x = n ^ (n >> 1)

        # If all 1 bits (binary), yield 0
        y = x & (x + 1)

        # Returns True if 0
        return not bool(y)

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

        n = int(inputs[0])
        
        return n


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    n = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_binary_alt_bit(n)
    print(z)


## END OF FILE