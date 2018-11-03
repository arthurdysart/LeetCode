# -*- coding: utf-8 -*-
"""
Leetcode - Remove linked list elements
https://leetcode.com/problems/remove-linked-list-elements
One pointer (forwarding) solution

Created on Sat Nov  3 14:02:15 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys
from collections import deque


# FUNCTION DEFINITIONS
class List_Node:
    def __init__(self, v, next=None):
        """
        Initializes node of linked-list.
        """
        self.val = v
        self.next = next

class Solution:
    def remove_elements(self, head, x):
        """
        Removes linked-list nodes with values equal to target "x".
        
        :type head: List_Node
        :type val: int
        :rtype: List_Node
        """
        # Initialize pointer for linked-list start
        list_start = List_Node(None)
        list_start.next = head

        # Initialize pointers for previous and current node
        prev = list_start
        current = list_start.next

        while current is not None:
            if current.val == x:
                # Removes current node by passing over from previous node
                prev.next = current.next
                current = prev.next
            else:
                # Increments pointers
                current = current.next
                prev = prev.next
        return list_start.next

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    # Inputs casts linked list elements and target as integers
    inputs = [x.strip("[]\n").split(",") for x in sys_stdin]
    a = deque([int(x) for x in inputs[0]])
    x = int(inputs[1][0])
    
    # Determines if empty list
    if not a:
        return List_Node(None)
    else:
        # Sets head node of linked list and current node pointer
        head = List_Node(a.popleft())
        current = head
        # Creates linked list nodes with edges
        while a:
            next = List_Node(a.popleft())
            current.next = next
            current = current.next
    return head, x


if __name__ == "__main__":
    # Imports standard input
    head, x = stdin(sys.stdin)

    # Evaluates solution
    s = Solution()
    r = s.remove_elements(head, x)

    while r is not None:
        print(r.val)
        r = r.next