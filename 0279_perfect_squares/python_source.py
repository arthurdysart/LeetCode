# -*- coding: utf-8 -*-
"""
Leetcode - Perfect Squares
https://leetcode.com/problems/perfect-squares

Created on Mon Dec 17 20:08:31 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import deque
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all target sum-perfect square possibilities.
    Implements breadth first search (BFS) algorithm.

    Time complexity: O(max(v) * m)
      - Amortized iterate over all target sum-perfect square possibilities
    Space complexity: O(max(v) * m)
      - Amortized store all unique intermediate sums for each tree level
    """

    def find_min_num_squares_sum(self, x):
        """
        Determines minimum number of perfect squares to reach target sum.

        :param int x: input integer as target sum
        :return: minimum number of perfect squares which yield target sum
        :rtype: int
        """
        if x < 1:
            return 0

        # Initialize array of relevant perfect squares
        a = self.init_squares(x)

        n = len(a)

        # Initialize queue and set for intermediate sums
        q = deque([x])
        s = set([x])

        # Initialize pointers for number of level elements and depth counter
        u = len(q)
        v = 1

        while q:

            p = q.popleft()

            for j in range(0, n, 1):

                # Evaluate intermediate sum
                t = p - a[j]

                if t not in s:
                    # Found unencountered intermediate sum
                    # Note: already encountered sums yield minimal level count

                    if t == 0:
                        # Found minimal count to target sum
                        return v

                    elif t < 0:
                        # Subsequent squares greater than intermediate sum
                        break

                    else:
                        # Collect updated intermediate sum
                        s.add(t)
                        q.append(t)

            u -= 1
            if u == 0:
                # Reset number of level elements and increase depth counter
                u = len(q)
                v += 1

        return v

    def init_squares(self, x):
        """
        Initializes array of relevant perfect squares.

        :param int x: target sum
        :return: array of relevant perfect squares
        :rtype: list[int]
        """
        n = int(x ** 0.5) + 1

        return [i ** 2
                for i
                in range(1, n, 1)]

class Solution2:
    """
    Iteration over all integers up to square root of target sum.
    Implements tabulation (bottom-up) dynamic programming.

    Time complexity: O(n * m)
      - Amortized iterate over all target sum-perfect square pairs
    Space complexity: O(n)
      - Update cache array for intermediate perfect square sum counts
    """

    def find_min_num_squares_sum(self, x):
        """
        Determines minimum number of perfect squares to reach target sum.

        :param int x: input integer as target sum
        :return: minimum number of perfect squares which yield target sum
        :rtype: int
        """
        if x < 1:
            return 0

        n = int(x ** 0.5) + 1

        # Initialize array of perfect squares
        a = [i ** 2
             for i
             in range(1, n, 1)]

        # Initialize cache array
        c = [float("inf")
             if i > 0
             else 0
             for i
             in range(0, x + 1, 1)]

        for i in range(1, x + 1, 1):
            for j in range(1, n, 1):
                # Iterate over all target sum "i" and squares "j" combinations

                if a[j - 1] <= i:
                    # Evaluate count by including and excluding target square
                    c[i] = min(1 + c[i - a[j - 1]],
                               c[i])

                if a[j - 1] >= i:
                    # Greater perfect squares are greater than target sum
                    break

        if c[x] == float("inf"):
            return 0
        else:
            return c[x]

class Solution1:
    """
    Iteration over all integers up to square root of target sum.
    Implements tabulation (bottom-up) dynamic programming.

    Time complexity: O(n * m)
      - Amortized iterate over all target sum-perfect square pairs
    Space complexity: O(n)
      - Update cache array for intermediate perfect square sum counts
    """

    def find_min_num_squares_sum(self, x):
        """
        Determines minimum number of perfect squares to reach target sum.

        :param int x: input integer as target sum
        :return: minimum number of perfect squares which yield target sum
        :rtype: int
        """
        if x < 1:
            return 0

        n = int(x ** 0.5) + 1

        # Initialize cache array
        c = [float("inf")
             if i > 0
             else 0
             for i
             in range(0, x + 1, 1)]

        for i in range(1, x + 1, 1):
            for j in range(1, n, 1):
                # Iterate over all target sum "i" and squares "j" combinations

                if j ** 2 <= i:
                    # Evaluate count by including and excluding target square
                    c[i] = min(1 + c[i - j ** 2],
                               c[i])

                if j ** 2 >= i:
                    # Greater perfect squares are greater than target sum
                    break

        if c[x] == float("inf"):
            return 0
        else:
            return c[x]

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: target integer sum
        :rtype: tup[int, int]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            x = 0
        else:
            x = int(inputs[0])

        return x


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    x = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_min_num_squares_sum(x)
    print(z)


## END OF FILE