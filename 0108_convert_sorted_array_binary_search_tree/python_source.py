# -*- coding: utf-8 -*-
"""
Leetcode - Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Created on Thu Jan 17 13:49:17 2019
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import deque
from python_util import TreeNode
import json
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Binary traversal and breadth-first search of sorted array.

    Time complexity: O(n)
        - Traverse all nodes
    Space complexity: O(n)
        - Create TreeNode objects for each element in sorted list
    """

    def sorted_arr_to_bst(self, a):
        """
        Creates binary search tree from input sorted list.

        :param list[int] a: sorted array of integers
        :return: binary search tree representing input sorted array
        :rtype: TreeNode
        """
        if not a:
            return None

        l = 0
        r = len(a)

        return self.convert_arr(a, l, r)

    def convert_arr(self, a, l, r):
        """
        Recursively converts target subarray into tree node and children nodes.

        :param list[int] a: sorted array of integers
        :param int l: pointer to starting index of target subarray (inclusive)
        :param int r: pointer to end index of target subarray (exculsive)
        :return: binary search tree representing input sorted subarray
        :rtype: TreeNode
        """
        if l == r:
            return None

        m = l + (r - l) // 2

        p = TreeNode(a[m])

        p.cl = self.convert_arr(a, l, m)
        p.cr = self.convert_arr(a, m + 1, r)

        return p
        
class Solution2:
    """
    Binary traversal and breadth-first search of sorted array.

    Time complexity: O(n)
        - Traverse all nodes
    Space complexity: O(n)
        - Create TreeNode objects for each element in sorted list
    """

    def sorted_arr_to_bst(self, a):
        """
        Creates binary search tree from input sorted list.

        :param list[int] a: sorted array of integers
        :return: binary search tree representing input sorted array
        :rtype: TreeNode
        """
        if not a:
            return None

        n = len(a)

        t = n // 2

        p = TreeNode(a[t])

        p.cl = self.sorted_arr_to_bst(a[:t])
        p.cr = self.sorted_arr_to_bst(a[t + 1:])

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input sorted array of integers
        :rtype: ListNode
        """
        try:
            x = next(sys_stdin)
            a = json.loads(x)
        except:
            a = []

        return a

class Output:

    def stdout(self, o):
        """
        Converts input binary search tree to array.

        :param ListNode o: head node of linked list
        :return: array representing binary search tree
        :rtype: list[int]
        """
        if not o:
            return None

        return TreeNode().revert(o)

    def transform_bst(self, o):
        """
        Converts binary search tree into array representation.

        :param TreeNode o: root node of binary search tree
        :return: array representation of binary search tree
        :rtype: list[int]
        """
        if not o:
            return []
        
        r = []
        
        q = deque([o])
        
        while q:

            p = q.popleft()

            if p:
                r.append(p.v)
            else:
                r.append(None)

            if (p and
                p.cl):
                q.append(p.cl)

            if (p and
                p.cr):
                q.append(p.cr)

        return r

## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    o = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .sorted_arr_to_bst(o)

    z = Output()\
        .transform_bst(z)
    print(z)


## END OF FILE