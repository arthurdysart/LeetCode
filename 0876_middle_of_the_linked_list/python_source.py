# -*- coding: utf-8 -*-
"""
Leetcode - Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Created on Mon Jan 14 14:31:35 2019
@author: Arthur Dysart
"""


## REQUIRED MODULES
from python_util import ListNode
import json
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Depth first traversal of single-linked list.

    Time complexity: O(n)
        - Traverse all nodes
    Space complexity: O(1)
        - Update constant number of pointers
    """

    def find_middle_node(self, o):
        """
        Determines middle node in linked list.

        :param ListNode o: head node of linked list
        :return: middle node in linked list
        :rtype: ListNode
        """
        if not o:
            return None

        # Initialize counter for number of nodes
        n = 0

        p = o
        while p:
            # Set next target node and increment number of nodes
            p = p.c
            n += 1

        p = o
        for i in range(0, n // 2, 1):
            # Iterate until middle node
            p = p.c
        
        return p


class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: head node of linked list
        :rtype: ListNode
        """
        try:
            x = next(sys_stdin)
            a = json.loads(x)
        except:
            a = []

        o = ListNode().convert(a)

        return o

class Output:
    
    def stdout(self, o):
        """
        Converts input linked list to array.
        
        :param ListNode o: head node of linked list
        :return: array representing linked list elements
        :rtype: list[int]
        """
        if not o:
            return None
        
        return ListNode().revert(o)

## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    o = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .find_middle_node(o)
    
    z = Output()\
        .stdout(z)
    print(z)


## END OF FILE