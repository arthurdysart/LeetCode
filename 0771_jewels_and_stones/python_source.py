# -*- coding: utf-8 -*-
"""
Leetcode - Jewels and Stones
https://leetcode.com/problems/jewels-and-stones

Created on Thu Nov 22 10:59:49 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iterative search of dynamic window over string.

    Time complexity: O(n)
        - Iterate over all elements in string "s"
    Space complexity: O(m)
        - Store all elements in string "j"
    """

    def count_jewels_in_stones(self, j, s):
        """
        Determines number of stones that are also jewels.

        :param str j: all characters representing jewels
        :param str s: all characters representing stones (potential jewels)
        :return: number of stones that are jewels
        :rtype: int
        """
        if (not j or
            not s):
            return 0

        # Convert to set for single-pass search
        j = set(j)

        p = 0
        for c in s:
            if c in j:
                p += 1
        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: strings representing jewels and stones (potential jewels)
        :rtype: str
        """
        inputs = [x.strip("[]\"\n") for x in sys_stdin]
        j = inputs[0]
        s = inputs[1]
        return j, s


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    j, s = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .count_jewels_in_stones(j, s)
    print(z)


## END OF FILE