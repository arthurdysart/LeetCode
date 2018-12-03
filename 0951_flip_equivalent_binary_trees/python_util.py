# -*- coding: utf-8 -*-
"""
Leetcode utility module
Created on Sun Nov 11 11:50:34 2018
@author: Arthur Dysart

Miscellaneous functions and classes for Leetcode exercises.
"""


## REQUIRED MODULES
from collections import deque


## MODULE DEFINITIONS
class TreeNode:
    """
    Manage Node objects for binary trees.
    """

    def __init__(self, x=None):
        """
        Constructor for TreeNode objects.

        :param (int or None) v: integer value for node
        :param TreeNode cl: pointer to left-side child node
        :param TreeNode cr: pointer to right-side child node
        :return: None
        :rtype: None
        """
        self.v = x
        self.cl = None
        self.cr = None
        return None

    def convert(self, a):
        """
        Transforms BST from array to tree representation.

        :param list[int or None] a: input BST array
        :return: head node for BST tree representation
        :rtype: TreeNode object
        """
        # Check for empty or incorrect type input
        if (not a or
            not isinstance(a, list)):
            return TreeNode(None)
        # Set head node
        o = TreeNode(a[0])

        q = deque([o])

        i = 0
        n = len(a)
        while q:
            p = q.popleft()
            if 2 * i + 1 < n:
                p.cl = TreeNode(a[2 * i + 1])
                q.append(p.cl)
            if 2 * i + 2 < n:
                p.cr = TreeNode(a[2 * i + 2])
                q.append(p.cr)
            i += 1
        return o

    def revert(self, o):
        """
        Transforms BST from tree to array representation.

        :param TreeNode o: input head node for BST tree representation
        :return: array for BST array representation
        :rtype: list[int or None]
        """
        # Check for empty or incorrect type input
        if (not o or
            not isinstance(o, TreeNode)):
            return list()

        a = list()
        q = deque([o])

        i = 0
        while q:
            p = q.popleft()
            a.append(p.v)
            if p.cl is not None:
                q.append(p.cl)
            if p.cr is not None:
                q.append(p.cr)
            i += 1
        return a


## MAIN MODULE
if __name__ == "__main__":
    pass


## END OF FILE