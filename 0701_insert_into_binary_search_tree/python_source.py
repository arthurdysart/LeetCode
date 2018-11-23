# -*- coding: utf-8 -*-
"""
Leetcode - Insert into a Binary Search Tree
https://leetcode.com/problems/insert-into-a-binary-search-tree

Created on Thu Nov 22 21:18:47 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from python_util import TreeNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Recursive iteration over all values of input array.

    Time complexity: O(log(n))
        - Recursively traverse binary search tree
    Space complexity: O(1)
        - Add leaf node with new value to binary search tree
    """

    def insert_into_bst(self, o, x):
        """
        Insert target value into binary search tree.

        :param TreeNode o: root node of binary search tree
        :param int x: target value to insert into binary search tree
        :return: root node of entire binary search tree
        :rtype: TreeNode object
        """
        if not o:
            return TreeNode(x)

        if x > o.v:
            # Search right since target is greater than node value
            if o.cr is None:
                o.cr = TreeNode(x)
            elif o.cr.v is None:
                o.cr = TreeNode(x)
            else:
                self.insert_into_bst(o.cr, x)
        else:
            # Search left since target is less than node value
            if o.cl is None:
                o.cl = TreeNode(x)
            elif o.cl.v is None:
                o.cl = TreeNode(x)
            else:
                self.insert_into_bst(o.cl, x)

        return o

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: root node of binary tree
        :rtype: TreeNode object
        """
        inputs = [x.strip("[]\"\n") for x in sys_stdin]
        a = [self.cast(x)
             for x
             in inputs[0].split(",")]
        o = TreeNode()\
            .convert(a)
        x = int(inputs[1])
        return o, x

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
    o, x = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .insert_into_bst(o, x)

    # Convert solution to array
    z = TreeNode()\
        .revert(z)
    print(z)


## END OF FILE