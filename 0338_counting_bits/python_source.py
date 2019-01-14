# -*- coding: utf-8 -*-
"""
Leetcode - Counting Bits
https://leetcode.com/problems/counting-bits/

Updated on Mon Jan 14 13:40:37 2019
Created on Fri Jan 11 11:38:01 2019
@author: Arthur Dysart
"""


# REQUIRED MODULES
import json
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all elements in array.

    Time complexity: O(n)
      - Iterate over all integers in range
    Space complexity: O(n)
      - Collect number of "1" digits for each integer
    """

    def count_bits_range(self, n):
        """
        Evaluates number of "1" integers in binary form of input integer range.

        :param int n: maximum limit of target range (inclusive)
        :return: array of number of "1" integers of binary representations
        :rtype: list[int]
        """
        if not n:
            return [0]

        t = [0]

        for i in range(1, n + 1, 1):

            # Determines right-shifted integer and its number of "1" digits
            j = i // 2
            x = t[j]

            # Determines digit value of unit place value in binary form
            y = i % 2

            # Calculates number of "1" digits in target integer "i"
            # Note: sum of (1) right-shifted integer and (2) unit place value
            r = x + y
            t.append(r)

        return t

class Solution1:
    """
    Iteration over all elements in array.
    Implements tabulation algorithm (bottom-up dynamic programming).

    Time complexity: O(n)
      - Iterate over all integers in range
    Space complexity: O(n)
      - Collect number of "1" digits for each integer in cache array
    """

    def count_bits_range(self, n):
        """
        Evaluates number of "1" integers in binary form of input integer range.

        :param int n: maximum limit of target range (inclusive)
        :return: array of number of "1" integers of binary representations
        :rtype: list[int]
        """
        if not n:
            return [0]

        # Initialize cache array
        c = [0
             for n
             in range(0, n + 1, 1)]

        # Initialize reference count pointer
        p = 0

        for i in range(1, n + 1, 1):

            if p == i // 2:
                # Restart reference count pointer
                p = i

            # Set target count as increment of reference count
            c[i] = 1 + c[i - p]

        return c

class Solution2:
    """
    Iteration over all elements in array.

    Time complexity: O(n * log(n))
      - Iterate over all integers and their binary representations
    Space complexity: O(n)
      - Collect number of "1" digits for each integer
    """

    def count_bits_range(self, n):
        """
        Evaluates number of "1" integers in binary form of input integer range.

        :param int n: maximum limit of target range (inclusive)
        :return: array of number of "1" integers of binary representations
        :rtype: list[int]
        """
        if not n:
            return [0]
        
        return [self.eval_unit_bits(i)
                for i
                in range(0, n + 1, 1)]

    def eval_unit_bits(self, i):
        """
        Evaluates number of "1" integers in binary form of input integer.

        :param int i: input integer
        :return: number of "1" characters in input integer
        :rtype: int
        """
        if i < 1:
            return 0

        return sum(1 for c
                   in bin(i)[2:]
                   if c == "1")

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input integer
        :rtype: int
        """
        n = next(sys_stdin)

        return json.loads(n)


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution1()\
        .count_bits_range(a)
    print(json.dumps(z))


## END OF FILE