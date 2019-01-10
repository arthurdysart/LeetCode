# -*- coding: utf-8 -*-
"""
Leetcode - Keys and Rooms
https://leetcode.com/problems/keys-and-rooms

Created on Thu Jan 10 10:25:47 2019
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import deque
import json
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Depth first traversal over all index-value sequences.

    Time complexity: O(n)
      - Amortized traverse all array elements
    Space complexity: O(n)
      - Collect elements in visited array
    """

    def is_complete_visit(self, a):
        """
        Determines whether all rooms can be visited, beginning with room 0.

        :param list[list[int]] a: input array of rooms with keys
        :return: True if all rooms can be visited
        :rtype: bool
        """
        if not a:
            return True

        n = len(a)
        v = [False
             if x > 0
             else True
             for x in
             range(0, n, 1)]

        q = deque(a[0])

        while q:

            p = q.pop()

            # Set target room index as visited
            v[p] = True

            for i in a[p]:

                if not v[i]:
                    # Collect value if room index not visited
                    q.append(i)

        # Evalaute whether all room indicies are visited
        return all(v)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of integer arrays
        :rtype: list[list[int]]
        """
        inputs = [x for x in sys_stdin]

        if (inputs and
            inputs[0]):
            a = json.loads(inputs[0])
        else:
            a = ""

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_complete_visit(a)
    print(z)


## END OF FILE