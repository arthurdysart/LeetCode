# -*- coding: utf-8 -*-
"""
Leetcode - Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted

Created on Sun Nov 18 16:47:00 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Traverse all indicies in each string.

    Time complexity: O(n * m)
        - Amortized traverse all string characters
    Space complexity: O(1)
        - Update constant pointer value
    """
    
    def count_min_deletions(self, a):
        """
        Determines number of word indicies not in alphabetical order.

        :param list[str] a: array of identical-length strings
        :return: number of word indicies not in alphabetical order
        :rtype: int
        """

        p = 0
        n = len(a)
        m = len(a[0])
        # Iterate over each character (array column)
        for i in range(m):
            if self.is_non_alpha_order(i, n, a):
                p += 1
        return p

    def is_non_alpha_order(self, i, n, a):
        """
        Evaluates whether character index is not in alphabetical order.

        :param int i: index of target character
        :param int n: max length of each word (number of rows)
        :param list[str] a: array of identical-length words
        :return: True if character index is not in alphabetical order
        :rtype: bool
        """
        # Iterate over each word (array row)
        for j in range(n - 1):
            if a[j][i].lower() > a[j + 1][i].lower():
                # Increase counter because non-alphabetical order
                return True
        return False

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of words
        :rtype: list[str]
        """
        inputs = [x.strip("[]\"\n") for x in sys_stdin]
        a = inputs[0].split("\", \"")
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .count_min_deletions(a)
    print(z)


## END OF FILE