# -*- coding: utf-8 -*-
"""
Leetcode - Add Two Numbers
https://leetcode.com/problems/add-two-numbers

Created on Sun Nov 11 20:42:47 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from python_util import ListNode
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Time complexity: O(max(len(o1), len(o2)))
        - Amortized length of longest integer as linked list
    Space complexity: O(max(len(o1), len(o2)))
        - Amortized length of sum as linked list
    """

    def add_two_numbers(self, o1, o2):
        """
        :param ListNode o1: head node for first integer as linked list
        :type o2: ListNode: head node for second integer as linked list
        :return: head node for linked list of sum
        :rtype: ListNode
        """
        # Initialize carry-over digit
        q = 0
        # Initialize header node for output
        o3 = ListNode(None)
        p3 = o3
        
        p1 = o1
        p2 = o2
        while p1 or p2 or q:
            if p1:
                v1 = p1.v
                p1 = p1.c
            else:
                v1 = 0
            if p2:
                v2 = p2.v
                p2 = p2.c
            else:
                v2 = 0
            q, s = divmod(v1 + v2 + q, 10)
            p3.c = ListNode(s)
            p3 = p3.c
        return o3.c


class Solution3:
    """
    Time complexity: O(len(o1) + len(o2))
        - Amortized sum of lengths for both integers as linked list
    Space complexity: O(max(len(o1), len(o2)))
        - Amortized length of sum as linked list
    """

    def add_two_numbers(self, o1, o2):
        """
        Calculates sum of two numbers as linked list.

        :param ListNode o1: head node of first number
        :param ListNode o2: head node of second number
        :return: head node of sum
        :rtype: ListNode
        """
        # Check for empty input
        if (not o1 or
            not o2):
            return ListNode(0)

        # Calculate sum of integers converted from linked lists
        n = self.convert(o1) + self.convert(o2)

        # Transform integer sum into linked list
        return self.revert(n)

    def convert(self, o):
        """
        Transform linked list into integer representation.
        
        :param ListNode o: head node of linked list
        :return: integer representation of linked list
        :rtype: int
        """
        f = 1
        n = 0
        p = o
        while p:
            n += p.v * f
            f *= 10
            p = p.c
        return n

    def revert(self, n):
        """
        Transform integer into linked list representation.
        
        :param int n: integer representation of sum
        :return: linked list representation of sum
        :rtype: ListNode
        """
        if n == 0:
            return ListNode(0)

        o = ListNode(None)
        p = o
        while n > 0:
            n, x = divmod(n, 10)
            p.c = ListNode(x)
            p = p.c

        return o.c


class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: list of ListNodes representing each integer
        :rtype: list[ListNode]
        """
        inputs = [x for x in sys_stdin]
        o1, o2 = [self.transform(s) for s in inputs]
        return o1, o2

    def transform(self, s):
        """
        Transforms input string into linked list.    
        
        :param str s: input string for array 
        :return: head node for linked list
        :rtype: ListNode
        """
        a = [int(x) for x in s.strip("[]\n").split(", ")]
        return ListNode().convert(a)


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    o1, o2 = Input()\
             .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .add_two_numbers(o1, o2)

    # Convert linked list to array
    z = ListNode()\
        .revert(z)
    print(z)


## END OF FILE