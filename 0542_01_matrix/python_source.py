# -*- coding: utf-8 -*-
"""
Leetcode - 01 Matrix
https://leetcode.com/problems/01-matrix

Created on Fri Nov 23 15:31:32 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
from collections import deque
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iterative breadth first search (BFS) across all elements in 2D array.
    
    Time complexity: O(n * m)
      - Amortized iterate over all rows and columns
    Space complexity: O(n * m)
      - Amortized store all values in queue
    """

    def update_matrix(self, a):
        """
        Determines minimum distance to value "0" for all elements in 2D array.

        :param list[list[int]] a: input 2D array with elements
        :return: updated 2D array containing minimum distances from value "0"
        :rtype: list[list[int]]
        """
        if not a:
            return 0

        n = len(a)
        m = len(a[0])

        for i in range(0, n, 1):
            # Iterate over rows
            for j in range(0, m, 1):
                # Iterate over columns
                if a[i][j] != 0:
                    a = self.update_element(i, j, n, m, a)
        return a

    def update_element(self, i, j, n, m, a):
        """
        Determines minimum distance to value "0" specified element.
        Implements breadth-first search algorithm (clockwise priority).

        :param int i: row index of target element in 2D array
        :param int j: column index of target element in 2D array
        :param int n: total rows in 2D array
        :param int m: total columns in 2D array
        :param list[list[int]] a: input 2D array with elements
        :return: updated 2D array with minimum distance from value "0"
        :rtype: list[list[str]]
        """
        p = (i, j)
        # Initialize v
        v = set([p])
        q = deque([p])

        d = 0
        c = 0
        t = len(q)
        while q:
            x, y = q.popleft()

            if a[x][y] == 0:
                # Update with distance since nearest "0" found
                a[i][j] = d
                return a

            if x != 0:
                # Search UP one cell
                p = (x - 1, y)
                q, v = self.traverse_breadth(p, q, v)
            if x != n - 1:
                # Search DOWN one cell
                p = (x + 1, y)
                q, v = self.traverse_breadth(p, q, v)
            if y != 0:
                # Search LEFT one cell
                p = (x, y - 1)
                q, v = self.traverse_breadth(p, q, v)
            if y != m - 1:
                # Search RIGHT one cell
                p = (x, y + 1)
                q, v = self.traverse_breadth(p, q, v)

            c += 1
            if c == t:
                # Increment cell distance and reset level counters
                d += 1
                c = 0
                t = len(q)

        # No neighboring value "0" found
        a[i][j] = float("inf")
        return a

    def traverse_breadth(self, p, q, v):
        """
        Updates search queue and visited set if target "p" not yet visited.
        Implements breadth first traversal algorithm.

        :param tuple[int, int] p: coordinates of target in 2D array
        :param deque[tuple[int, int]] q: search queue
        :param set[tuple[int, int]] v: visited coordinates set
        :return: updated search queue and visited set
        :rtype: tuple[deque[tuple[int, int]], set[tuple[int, int]]]
        """
        if p not in v:
            q.append(p)
            v.add(p)
        return q, v

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.
    
        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input 2D array of integer values
        :rtype: int
        """
        inputs = [x.strip("[]\n").split("],[")
                  for x
                  in sys_stdin]

        a = [list(map(int,x.split(",")))
             for x
             in inputs[0]]
        return a


if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .update_matrix(a)
    print(z)