# -*- coding: utf-8 -*-
"""
Leetcode - Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal

Created on Wed Nov 14 17:53:39 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import deque
from python_util import TreeNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Depth first traversal of binary tree.
    Time complexity: O(n)
        - Amortized traverse all nodes
    Space complexity: O(n)
        - Amortized append all node values
    """

    def preorder_traversal(self, o):
        """
        Determine preorder traversal of binary tree.

        :param TreeNode o: root node of binary tree
        :return: array of values by preorder traveral
        :rtype: list[int]
        """
        if not o:
            return list()

        l = list()
        q = deque([o])
        
        while q:
            p = q.pop()
            if p.cr:
                q.append(p.cr)
            if p.cl:
                q.append(p.cl)
            if p.v:
                l.append(p.v)
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
        .preorder_traversal(o)
    print(z)


## END OF FILE