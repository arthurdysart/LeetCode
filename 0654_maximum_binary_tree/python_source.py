# -*- coding: utf-8 -*-
"""
Leetcode - Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree

Created on Thu Nov 22 20:32:01 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from python_util import TreeNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Recursive iteration over all values of input array.

    Time complexity: O(n ** 2)
        - Amortized recursively iterate over sorted array
    Space complexity: O(n)
        - Store all array values as TreeNode objects
    """

    def create_max_binary_tree(self, a):
        """
        Recursively builds binary tree nodes from maximum value of array.
        Maximum array value determined by linear one-pointer search.
        
        :param list[int] a: input array of integer values
        :return: Root node of maximum binary tree
        :rtype: TreeNode object
        """
        if not a:
            return TreeNode(None)

        if len(a) == 1:
            return TreeNode(a[0])
        else:
            m = self.find_index_max(a)

            o = TreeNode(a[m])
            o.cl = self.create_max_binary_tree(a[:m])
            o.cr = self.create_max_binary_tree(a[m + 1:])

            return o

    def find_index_max(self, a):
        """
        Determines maximum array value by linear one-pointer search.
        
        :param list[int] a: input array of integer values
        :return: index of maximum array value
        :rtype: int
        """
        if not a:
            return -1

        m = 0
        n = len(a)
        for i in range(n):
            if a[i] > a[m]:
                m = i
        return m

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of input integer values
        :rtype: list[int or None]
        """
        inputs = [x.strip("[]\"\n") for x in sys_stdin]
        a = [self.cast(x)
             for x
             in inputs[0].split(",")]
        return a

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
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .create_max_binary_tree(a)

    # Convert solution to array
    z = TreeNode()\
        .revert(z)
    print(z)


## END OF FILE