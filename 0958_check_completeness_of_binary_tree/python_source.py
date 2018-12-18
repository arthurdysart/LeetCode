# -*- coding: utf-8 -*-
"""
Leetcode - Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree

Created on Mon Dec 17 22:14:06 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import deque
from python_util import TreeNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Recursive breadth-first traversal (DFT) of binary tree.

    Time complexity: O(n)
        - Amortized traverse all nodes in binary tree
    Space complexity: O(n)
        - Amortized collect all nodes after deepest tree level
    """

    def is_complete_tree(self, o):
        """
        Determines whether input binary tree is complete.

        :type TreeNode o: head node of binary tree
        :return: True if input binary tree is complete
        :rtype: bool
        """
        if not o:
            return True

        q = deque([o])

        while (q[0] and
               q[0].v):
            # Iterate until first empty node
            p = q.popleft()

            q.append(p.cl)
            q.append(p.cr)

        # True if only empty nodes in queue elements
        return not any(q)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: head node of binary tree
        :rtype: tup[TreeNode, TreeNode]
        """
        inputs = [x for x in sys_stdin]

        if inputs[0] == "":
            a = list()
        else:
            a = [self.cast(x.strip())
                 for x
                 in inputs[0].strip("[]\n").split(",")]
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
        .is_complete_tree(o)
    print(z)


## END OF FILE