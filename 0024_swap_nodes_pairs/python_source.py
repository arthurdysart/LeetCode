# -*- coding: utf-8 -*-
"""
Leetcode - Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs

Created on Fri Nov 23 21:02:56 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from python_util import ListNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all elements of linked list.

    Time complexity: O(n)
        - Iterate over all nodes of linked list
    Space complexity: O(1)
        - Update constant number of pointers
    """

    def swap_pairs(self, o):
        """
        Exchange location of each pair of nodes in linked list.
        
        :param ListNode o: head node for linked list
        :return: updated head node for linked list
        :rtype: ListNode
        """
        if not o:
            return None

        # Create pre-head node
        h = ListNode(None)
        h.c = o

        l = h
        m = h.c
        r = h.c.c
        p = 0

        while r:
            if p % 2 == 0:
                # Save old pointers
                x = l.c
                y = m.c
                z = r.c

                # Set new pointers
                l.c = y
                m.c = z
                r.c = x

                # Reset pointer order
                m, r = r, m

            l = l.c
            m = m.c
            r = r.c

            p += 1

        return h.c

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: head node of linked list
        :rtype: ListNode object
        """
        inputs = [x.strip("[]\n") for x in sys_stdin]
        a = [int(x) for x in inputs[0].split(",")]
        o = ListNode()\
            .convert(a)
        return o


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    o = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .swap_pairs(o)

    # Convert linked list to array
    z = ListNode()\
        .revert(z)
    print(z)


## END OF FILE