# -*- coding: utf-8 -*-
"""
Leetcode - Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal

Created on Sat Nov 17 12:58:51 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import deque
from python_util import TreeNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Depth first traversal of binary tree (2 stacks, 1 pointer).
    Time complexity: O(n)
        - Amortized traverse all nodes
    Space complexity: O(n)
        - Amortized append all node values
    """

    def postorder_traversal(self, o):
        """
        Determine postorder traversal of binary tree.

        :param TreeNode o: root node of binary tree
        :return: array of values by postorder traveral
        :rtype: list[int]
        """
        if not o:
            return list()

        l = deque()
        q = deque([o])

        while q:
            p = q.pop()

            if p.v is not None:
                l.append(p.v)

            if p.cl:
                q.append(p.cl)
            if p.cr:
                q.append(p.cr)

        return list(reversed(l))

class Solution2:
    """
    Depth first traversal of binary tree (1 stack, 1 list, 1 set, 1 pointer).
    Time complexity: O(n)
        - Amortized traverse all nodes
    Space complexity: O(n)
        - Amortized append all node values
    """

    def postorder_traversal(self, o):
        """
        Determine postorder traversal of binary tree.

        :param TreeNode o: root node of binary tree
        :return: array of values by postorder traveral
        :rtype: list[int]
        """
        if not o:
            return list()

        s = set()
        l = list()
        q = deque([o])

        while q:
            p = q.pop()

            if p.cl or p.cr:
                # Check whether children in set
                if p.cl in s or p.cr in s:
                    # Append to list and set of visited nodes
                    if p.v is not None:
                        l.append(p.v)
                    s.add(p)
                else:
                    # Append parent, right child, and left child nodes to stack
                    q.append(p)
                    if p.cr:
                        q.append(p.cr)
                    if p.cl:
                        q.append(p.cl)
            else:
                # Append to list and set of visited nodes
                if p.v is not None:
                    l.append(p.v)
                s.add(p)

        return l

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: head node of binary tree
        :rtype: TreeNode
        """
        a = [x for x in sys_stdin]
        a = [self.cast(x.strip())
             for x
             in a[0].strip("[]\n").split(",")]
        o = TreeNode().convert(a)
        return o

    def cast(self, x):
        """
        Converts string values to integer or None values.

        :param str x: string input parameter
        :return: converted integer or None value
        :rtype: int or None
        """
        if x.lower() == "null":
            return None
        else:
            return int(x)


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    o = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .postorder_traversal(o)
    print(z)


## END OF FILE