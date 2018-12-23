# -*- coding: utf-8 -*-
"""
Leetcode - Complex Number Multiplication
https://leetcode.com/problems/complex-number-multiplication

Created on Fri Dec 21 22:04:39 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    String manipulation of input strings.

    Time complexity: O(n)
      - Iterate over all string characters
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def multiply_complex_nums(self, a, b):
        """
        Calculates returns complex product of input complex numbers.

        :param str a: first complex number
        :param str b: second complex number
        :return: formatted string as product complex number
        :rtype: str
        """
        if (not a or
            not b):
            return ""

        a = self.parse_complex_num(a)
        b = self.parse_complex_num(b)

        # Calculate real and imaginary components of product
        re = a[0] * b[0] - a[1] * b[1]
        im = a[1] * b[0] + a[0] * b[1]

        z = [str(re),
             "+",
             str(im),
             "i"]

        return "".join(z)

    def parse_complex_num(self, x):
        """
        Splits input string into real and complex components.
        
        :param str x: input string as complex number
        :returns: array of integers as real and complex components
        :rtype: list[int]
        """
        return [int(i)
                for i
                in x.rstrip("i").split("+")]

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input strings as complex numbers
        :rtype: tuple[str, str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        a = inputs[0].strip("\"")
        b = inputs[1].strip("\"")

        return a, b


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a, b = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .multiply_complex_nums(a, b)
    print(z)


## END OF FILE