# -*- coding: utf-8 -*-
"""
Leetcode - Number of Islands
https://leetcode.com/problems/number-of-islands
Recursive depth-first-search solution

Created on Sat Nov 10 16:29:52 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Time complexity: O(r * c)
      - Iterate over all rows and columns
    Space complexity: O(1)
      - In-place recursive depth-first-search
    """

    def count_islands(self, a):
        """
        Counts number of islands in 2D array "a".

        :type a: list[list[str]]
        :rtype: int
        """
        if not a:
            return 0

        r = len(a)
        c = len(a[0])

        # Initialize counter for islands
        p = 0

        # Iterate over rows
        for i in range(0, r):
            # Iterate over columns
            for j in range(0, c):
                if a[i][j] == "1":
                    p += 1
                    a = self.erase_island(a, i, j, r, c)
        return p

    def erase_island(self, a, i, j, r, c):
        """
        Sets all connected island cells to water cells using
        recursive depth-first-search.

        :type a: list[list[str]]
        :type i: int
        :type j: int
        :type r: int
        :type c: int
        :rtype: list[list[str]]
        """
        if i != 0:
            # Search UP one cell
            if a[i - 1][j] == "1":
                a[i - 1][j] = "0"
                a = self.erase_island(a, i - 1, j, r, c)
        if i != r - 1:
            # Search DOWN one cell
            if a[i + 1][j] == "1":
                a[i + 1][j] = "0"
                a = self.erase_island(a, i + 1, j, r, c)
        if j != 0:
            # Search LEFT one cell
            if a[i][j - 1] == "1":
                a[i][j - 1] = "0"
                a = self.erase_island(a, i, j - 1, r, c)
        if j != c - 1:
            # Search RIGHT one cell
            if a[i][j + 1] == "1":
                a[i][j + 1] = "0"
                a = self.erase_island(a, i, j + 1, r, c)
        return a

def stdin(sys_stdin):
    """
    Imports standard input.
    
    :param _io.TextIOWrapper sys_stdin: standard input
    :return: characteristic factor for spiral matrix
    :rtype: int
    """
    inputs = [x.strip("[]").split("],[") for x in sys_stdin]
    a = [x.strip("\"").split("\",\"") for x in inputs[0]]
    return a


if __name__ == "__main__":
    # Imports standard input
    a = stdin(sys.stdin)

    # Evaluates solution
    r = Solution()\
        .count_islands(a)
    print(r)