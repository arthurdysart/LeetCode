# -*- coding: utf-8 -*-
"""
Leetcode - Array of Doubled Pairs
https://leetcode.com/problems/array-of-doubled-pairs

Created on Sat Dec  8 23:56:50 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import defaultdict
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all array elements.

    Time complexity: O(n * log n)
      - Sort input array and iterate over all array elements
    Space complexity: O(n)
      - Collect all array elements and their counts using hash map
    """

    def is_double_pair_arr(self, a):
        """
        Determines whether input array can be double-pair sorted.
        Array elements should follow "a[2 * i + 1] = 2 * a[2 * i]".

        :param list[str] a: input array of integers
        :return: True if input array can be double-pair sorted
        :rtype: bool
        """
        if not a:
            return True

        a.sort()

        n = len(a)
        c = self.init_counter(n, a)

        for i in range(0, n, 1):

            if (c[a[i]] > 0 and
                a[i] < 0):
                # Found unpaired negative element

                if c[a[i] / 2] > 0:
                    # Reduce counters for target and compliment element
                    c[a[i]] -= 1
                    c[a[i] / 2] -= 1

                else:
                    # Compliment not found
                    return False

            elif (c[a[i]] > 0 and
                  a[i] > 0):
                # Found unpaired positive element

                if c[a[i] * 2] > 0:
                    # Reduce counters for target and compliment element
                    c[a[i]] -= 1
                    c[a[i] * 2] -= 1
 
                else:
                    # Compliment not found
                    return False

            elif a[i] == 0:
                # Found zero

                if c[0] > 1:
                    # Reduce counter for zeroes
                    c[0] -= 2

                else:
                    # Compliment not found
                    return False

        # Found all elements paried
        return True

    def init_counter(self, n, a):
        """
        Initialize counter for all array elements.
        
        :param int n: total number of elements in array
        :param list[int] a: input array of integers
        :return: hash map of all array elements and their counts
        :rtype: dict[int: int]
        """
        c = defaultdict(int)
 
        for i in range(0, n, 1):
            c[a[i]] += 1

        return c

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
        .is_double_pair_arr(a)
    print(z)


## END OF FILE