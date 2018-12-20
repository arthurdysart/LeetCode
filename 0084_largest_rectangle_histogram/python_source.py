# -*- coding: utf-8 -*-
"""
Leetcode - Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram

Updated on Thu Dec 20 15:49:28 2018
Created on Thu Nov 15 19:51:56 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import deque
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all array elements.
    Interpolates greedy algorithm.
    
    Reference: https://www.youtube.com/watch?v=VNbkzsnllsU

    Time complexity: O(n)
        - Iterate over all array indicies and collected index-height pairs
    Space complexity: O(n)
        - Amortized collect all array elements and indicies in stacks
    """

    def largest_rectangle_area(self, a):
        """
        Determines area of maximum rectangle in histogram.

        :param list[int] a: list of height values in histogram
        :return: area of maximum rectangle
        :rtype: int
        """
        if not a:
            return 0

        p = deque()
        q = deque()

        t = float("-inf")
        m = float("-inf")

        n = len(a)
        for i in range(0, n, 1):

            if (not q
                or a[i] > q[-1]):

                p.append(i)
                q.append(a[i])

            elif a[i] < q[-1]:

                while (q and
                       a[i] < q[-1]):

                    x = p.pop()
                    y = q.pop()

                    t, m = self.eval_rectangle_area(i, t, m, x, y)

                p.append(x)
                q.append(a[i])

        while q:

            x = p.pop()
            y = q.pop()

            t, m = self.eval_rectangle_area(n, t, m, x, y)

        if m == float("-inf"):
            return 0
        else:
            return m

    def eval_rectangle_area(self, i, t, m, x, y):
        """
        Calculates maximum area of target rectangle in histogram.

        :param int i: target index
        :param int or float t: local maximum of target rectangle area
        :param int or float m: global maximum of target rectangle area
        :param int x: last-collected start index
        :param int y: last-collected histogram height
        :return: updated local and global maximima
        :rtype: tuple[int or float, int or float]
        """
        t = max(y * (i - x),
                t)

        m = max(t,
                m)

        return t, m

class Solution1:
    """
    Dynamic programming (tabulation) solution.

    Time complexity: O(n ** 2)
        - Iterate over all index-sublength pairs
    Space complexity: O(n ** 2)
        - Complete tabulation procedure
    """

    def largest_rectangle_area(self, a):
        """
        Calculates area of maximum rectangle in histrogram.

        :param list[int] a: list of height values in histogram
        :return: area of maximum rectangle
        :rtype: int
        """
        if not a:
            return 0
        elif len(a) < 2:
            return a[0] * 1
        else:
            c = {}
            p = max(a)
            n = len(a)

            # Solve first row
            for j in range(0, n):
                c[(1, j)] = a[j]
                p = max(a[j] * 1, p)

            # Calculate minimum height for subproblems
            for i in range(2, n + 1):
                for j in range(0, n - i + 1):
                    c[(i, j)] = min(c[(i - 1, j)],
                                    c[(i - 1, j + 1)])
    
                    # Calculate target area
                    t = c[(i, j)] * i
                    p = max(p, t)

        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of histogram heights
        :rtype: list[int]
        """
        inputs = [x.strip("[]\n").split(",")
                  for x
                  in sys_stdin]
        return [int(x) for x in inputs[0]]


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .largest_rectangle_area(a)
    print(z)


## END OF FILE