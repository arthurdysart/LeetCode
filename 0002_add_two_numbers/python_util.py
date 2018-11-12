# -*- coding: utf-8 -*-
"""
Leetcode utility module
Created on Sun Nov 11 21:12:31 2018
@author: Arthur Dysart

Miscellaneous functions and classes for Leetcode exercises.
"""


## MODULE DEFINITIONS
class ListNode:
    """
    Manage ListNode objects for linked lists.
    """

    def __init__(self, x=None):
        """
        Constructor for ListNode objects.

        :param (int or None) x: integer value for node
        :param ListNode c: pointer to child ListNode
        :return: None
        :rtype: None
        """
        self.v = x
        self.c = None
        return None

    def convert(self, a):
        """
        Transforms array to linked list representation.

        :param list[int] a: input array
        :return: head node for linked list representation
        :rtype: ListNode object
        """
        # Check for empty or incorrect type input
        if (not a or
            not isinstance(a, list)):
            return ListNode(None)

        # Set header node and pointer
        o = ListNode(None)
        p = o

        n = len(a)
        for i in range(n):
            p.c = ListNode(a[i])
            p = p.c
        return o.c

    def revert(self, o):
        """
        Transforms linked list to array representation.

        :param ListNode o: input head node for linked list
        :return: array representation of linked list
        :rtype: list[int]
        """
        # Check for empty or incorrect type input
        if (not o or
            not isinstance(o, ListNode)):
            return list()

        a = list()

        p = o
        while p:
            a.append(p.v)
            p = p.c
        return a


## MAIN MODULE
if __name__ == "__main__":
    pass


## END OF FILE