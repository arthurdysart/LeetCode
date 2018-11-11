# -*- coding: utf-8 -*-
"""
Leetcode - Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst

Created on Sun Nov 11 01:05:48 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import deque
from python_util import Node
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Modified breadth first traversal (BFT) of binary search tree (BST)
    Time complexity: O(n)
        - Amortized if all nodes in queue
    Space complexity: O(n)
        - Amortized if all nodes in queue
    """

    def sum_bst_range(self, o, l, r):
        """
        Calculates sum for BST elements if within range inclusive.

        :param Node o: root Node object for BST
        :param int l: lower limit for sum, inclusive
        :param int r: upper limit for sum, inclusive
        :return: sum of all BST element values within range
        :rtype: int
        """
        if o is None:
            return 0

        # Initialize sum and node queue
        s = 0
        q = deque([o])
        while q:
            p = q.popleft()
            x = p.v
            if x is None:
                # Node value is empty
                continue
            elif (x > l and
                  x < r):
                # Node value within range
                s += x
                if p.cl is not None:
                    q.append(p.cl)
                if p.cr is not None:
                    q.append(p.cr)
            elif x <= l:
                # Node value below range
                if x == l:
                    s += x
                if p.cr is not None:
                    q.append(p.cr)
            else:
                # Node value above range
                if x == r:
                    s += x
                if p.cl is not None:
                    q.append(p.cl)
        return s


class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.
        
        :param _io.TextIOWrapper sys_stdin: standard input
        :return: characteristic factor for spiral matrix
        :rtype: int
        """
        inputs = [x for x in sys_stdin]
        a = [self.cast(x)
             for x
             in inputs[0].strip("[]\n").split(",")]
        l = int(inputs[1])
        r = int(inputs[2])
        return a, l, r

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
    a, l, r = Input()\
              .stdin(sys.stdin)
    
    # Convert BST array to tree
    o = Node()\
        .convert(a)

    # Evaluate solution
    r = Solution()\
        .sum_bst_range(o, l, r)
    print(r)


## END OF FILE