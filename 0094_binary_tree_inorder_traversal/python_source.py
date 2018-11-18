# -*- coding: utf-8 -*-
"""
Leetcode - Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal

Created on Wed Nov 14 22:48:26 2018
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

    def inorder_traversal(self, o):
        """
        Determines node values by inorder traversal.
        
        :param TreeNode o: head node of binary tree
        :return: list of node values by inorder traversal
        :rtype: List[int]
        """
        if not o:
            return list()
        
        q = deque([TreeNode(None)])
        l = list()
        
        p = o
        while q:
            # Find limiting left-node
            p, q = self.find_left_limit(p, q)
            
            # Save value of parent-node
            if p.v:
                l.append(p.v)

            # Move pointer to right-node
            p = p.cr
        return l

    def find_left_limit(self, p, q):
        """
        Determines left-most node in current tree path.
        
        :param TreeNode p: pointer to current node
        :param deque q: stack for parent nodes
        :return: updated pointer and node stack
        :rtype: tuple[TreeNode, deque]
        """
        while p:
            q.append(p)
            p = p.cl
        p = q.pop()
        return p, q


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
        .inorder_traversal(o)
    print(z)


## END OF FILE