# -*- coding: utf-8 -*-
"""
Leetcode - Sum Of Square Numbers
https://leetcode.com/problems/sum-of-square-numbers

Created on Mon Dec 17 19:11:05 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all integers up to square root of target sum.

    Time complexity: O(n)
      - Amortized iterate over all integers in range
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def is_square_sum(self, x):
        """
        Determines whether input integer is a valid square sum.

        :param int x: target input integer
        :return: True if target integer is a valid square sum
        :rtype: bool
        """
        if not x:
            return True

        n = int(x ** 0.5) + 1

        for i in range(0, n, 1):

            # Calculate compliment of target integer
            t = x - i ** 2

            if (t ** 0.5) % 1 == 0:
                # Found integer pair with matching target sum
                return True

        # Found no integer pairs
        return False

class Solution1:
    """
    Iteration over all integer pair combinations.

    Time complexity: O(n ** 2)
      - Amortized iterate over all integer pairs
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def is_square_sum(self, x):
        """
        Determines whether input integer is a valid square sum.

        :param int x: target input integer
        :return: True if target integer is a valid square sum
        :rtype: bool
        """
        if not x:
            return True

        n = int(x ** 0.5) + 1

        for i in range(0, n, 1):
            for j in range(0, n, 1):

                if i ** 2 + j ** 2 == x:
                    # Found integer pair which sum to target integer
                    return True

        # Found no integer pairs
        return False

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: target integer sum
        :rtype: tup[int, int]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            x = 0
        else:
            x = int(inputs[0])

        return x


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    x = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_square_sum(x)
    print(z)


## END OF FILE