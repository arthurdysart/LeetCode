# -*- coding: utf-8 -*-
"""
Leetcode - Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view
Created on Mon Nov 12 17:33:00 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import deque
from python_util import TreeNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Breadth first traversal of binary tree.
    Time complexity: O(n)
        - Amortized traverse all nodes
    Space complexity: O(n)
        - Amortized append all node values
    """

    def right_side_view(self, o):
        """
        Determine all right-most nodes of binary tree.
        
        :param TreeNode o: root node of binary tree
        :return: array of right-most element values
        :rtype: list[int]
        """
        if not o:
            return list()

        # Initialize output list and queue
        l = list()
        q = deque([o])

        c = 0
        t = 1
        while q:
            # Extract node and increment counter
            p = q.popleft()
            c += 1

            # Add children of current node
            if p.cl:
                q.append(p.cl)
            if p.cr:
                q.append(p.cr)

            if c == t:
                # For right-most node: add value, reset counter & target
                l.append(p.v)
                c = 0
                t = len(q)

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
        a = [self.cast(x)
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
        .right_side_view(o)
    print(z)


## END OF FILE