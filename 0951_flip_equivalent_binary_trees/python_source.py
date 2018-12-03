# -*- coding: utf-8 -*-
"""
Leetcode - Flip Equivalent Binary Trees
https://leetcode.com/problems/flip-equivalent-binary-trees/

Created on Sun Dec  2 19:46:25 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from python_util import TreeNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Recursive depth-first traversal (DFT) of two binary trees.
    Time complexity: O(min(len(n), len(m)))
        - Amortized traverse all nodes of smallest input tree
    Space complexity: O(min(len(n), len(m)))
        - Amortized evaluate until end of smallest input tree
    """

    def is_flip_valid(self, o1, o2):
        """
        Determines whether binary trees are equivalent with or without flip.

        :param TreeNode o1: root node of first binary tree
        :param TreeNode o2: root node of second binary tree
        :return: True if binary trees are flip equivalent
        :rtype: bool
        """
        # Check if empty nodes
        if (not o1 and
            not o2):
            return True
        # Check if unbalanced nodes
        elif (not o1 or
              not o2):
            return False


        # Check if unequal node values
        if o1.v != o2.v:
            return False

        # Check if no children for both nodes
        elif ((not o1.cl and not o1.cr) and
              (not o2.cl and not o2.cr)):
            return True

        # Check if two children for both nodes
        elif ((o1.cl and o1.cr) and
              (o2.cl and o2.cr)):

            # Evaluate either unflipped or flipped children
            return ((self.is_flip_valid(o1.cl, o2.cl) and
                     self.is_flip_valid(o1.cr, o2.cr)) or
                    (self.is_flip_valid(o1.cl, o2.cr) and
                     self.is_flip_valid(o1.cr, o2.cl)))

        # Check if flipped singular child
        elif ((o1.cl and not o1.cr) and
              (o2.cr and not o2.cl)):
            return self.is_flip_valid(o1.cl, o2.cr)

        elif ((o1.cr and not o1.cl) and
              (o2.cl and not o2.cr)):
            return self.is_flip_valid(o1.cr, o2.cl)

        # Check if unflipped singular child
        elif ((o1.cl and not o1.cr) and
              (o2.cl and not o2.cr)):
            return self.is_flip_valid(o1.cl, o2.cl)

        elif ((o1.cr and not o1.cl) and
              (o2.cr and not o2.cl)):
            return self.is_flip_valid(o1.cr, o2.cr)

        # Found unbalanced children
        else:
            return False

class Solution2:
    """
    Recursive depth-first traversal (DFT) of two binary trees.
    Time complexity: O(min(len(n), len(m)))
        - Amortized traverse all nodes of smallest input tree
    Space complexity: O(min(len(n), len(m)))
        - Amortized evaluate until end of smallest input tree
    """

    def is_flip_valid(self, o1, o2):
        """
        Determines whether binary trees are equivalent with or without flip.

        :param TreeNode o1: root node of first binary tree
        :param TreeNode o2: root node of second binary tree
        :return: True if binary trees are flip equivalent
        :rtype: bool
        """
        # Check if empty nodes
        if not o1 and not o2:
            return True
        # Check if unbalanced nodes
        elif not o1 or not o2:
            return False
        
        # Check node values
        if o1.v != o2.v:
            return False
        
        # Check if no children for both nodes
        if ((not o1.cl and not o1.cr) and
            (not o2.cl and not o2.cr)):
            return True

        # Check if two children for both nodes
        elif ((o1.cl and o1.cr) and
            (o2.cl and o2.cr)):

            # Check if no flip required
            if ((o1.cl.v == o2.cl.v) and
                (o1.cr.v == o2.cr.v)):
                return (self.is_flip_valid(o1.cl, o2.cl) and
                        self.is_flip_valid(o1.cr, o2.cr))

            # Check if flip required
            elif ((o1.cl.v == o2.cr.v) and
                  (o1.cr.v == o2.cl.v)):
                return (self.is_flip_valid(o1.cl, o2.cr) and
                        self.is_flip_valid(o1.cr, o2.cl))

            # Found unequal children
            else:
                return False

        # Check if flipped children for both nodes 
        elif ((o1.cl and not o1.cr) and
              (o2.cr and not o2.cl)):
            return self.is_flip_valid(o1.cl, o2.cr)
        elif ((o1.cr and not o1.cl) and
              (o2.cl and not o2.cr)):
            return self.is_flip_valid(o1.cr, o2.cl)

        # Check if no flip required for both nodes 
        elif ((o1.cl and not o1.cr) and
              (o2.cl and not o2.cr)):
            return self.is_flip_valid(o1.cl, o2.cl)
        elif ((o1.cr and not o1.cl) and
              (o2.cr and not o2.cl)):
            return self.is_flip_valid(o1.cr, o2.cr)

        # Found nodes with unbalanced children
        else:
            return False

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: head nodes of two binary trees
        :rtype: tup[TreeNode, TreeNode]
        """
        inputs = [x for x in sys_stdin]

        a1 = [self.cast(x.strip())
              for x
              in inputs[0].strip("[]\n").split(",")]
        o1 = TreeNode().convert(a1)

        a2 = [self.cast(x.strip())
              for x
              in inputs[0].strip("[]\n").split(",")]
        o2 = TreeNode().convert(a2)

        return o1, o2

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
    o1, o2 = Input()\
             .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .is_flip_valid(o1, o2)
    print(z)


## END OF FILE