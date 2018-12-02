# -*- coding: utf-8 -*-
"""
Leetcode - Array Nesting
https://leetcode.com/problems/array-nesting

Created on Sun Dec  2 15:42:26 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over all elements and nesting cycles.

    Time complexity: O(n)
      - Amortized traverse all array indicies
    Space complexity: O(1)
      - Update input array in-place
    """
    def find_max_nested_array_len(self, a):
        """
        Determines the maximum nesting cycle distance of input array.

        :param list[int] a: input array of integers
        :return: maximum nesting cycle distance
        :rtype: int
        """
        if not a:
            return 0

        p = float("-inf")

        n = len(a)
        for i in range(0, n, 1):
            d = self.eval_nesting(i, a)
            p = max(p, d)

        if p == float("-inf"):
            return 0
        else:
            return p

    def eval_nesting(self, i, a):
        """
        Evaluates nesting distance for target start index.

        :param int i: target start index for nesting cycle
        :param list[int] a: input array of integers
        :return: running cycle distance
        :rtype: int
        """
        j = i
        d = 0

        while a[j] != i:
            d += 1

            if a[j] < 0:
                # Found visited cycle
                return d
            else:
                # Move to next nested value
                a[j] *= -1
                j = -1 * a[j]

        # Found end of unvisited cycle
        a[j] *= -1
        return d + 1

class Solution2:
    """
    Iteration over all elements and nesting cycles.

    Time complexity: O(n)
      - Amortized traverse all array indicies
    Space complexity: O(n)
      - Amortized collect all array indicies
    """
    def find_max_nested_array_len(self, a):
        """
        Determines the maximum nesting cycle distance of input array.

        :param list[int] a: input array of integers
        :return: maximum nesting cycle distance
        :rtype: int
        """
        if not a:
            return 0

        c = set()
        p = float("-inf")

        n = len(a)
        for i in range(0, n, 1):
            d, c = self.eval_nesting(i, c, a)
            p = max(p, d)

        if p == float("-inf"):
            return 0
        else:
            return p

    def eval_nesting(self, i, c, a):
        """
        Evaluates nesting distance for target start index.

        :param int i: target start index for nesting cycle
        :param dict[tup[int, int]] c: hash map of known indicies
        :param list[int] a: input array of integers
        :return: running cycle distance and updated hash map
        :rtype: tup[int, dict[tup[int, int]]]
        """
        j = i
        d = 0

        while a[j] != i:
            d += 1

            if a[j] in c:
                # Found visited cycle
                return d, c
            else:
                # Move to next nested value
                c.add(j)
                j = a[j]

        # Found end of unvisited cycle
        c.add(j)
        return d + 1, c

class Solution3:
    """
    Iteration over all elements and nesting cycles.

    Time complexity: O(n ** 2)
      - Amortized traverse all nesting cycles for each target index
    Space complexity: O(n ** 2)
      - Amortized collect all start-end indicies and nesting distance
    """

    def find_max_nested_array_len(self, a):
        """
        Determines the maximum nesting cycle distance of input array.

        :param list[int] a: input array of integers
        :return: maximum nesting cycle distance
        :rtype: int
        """
        if not a:
            return 0

        c = dict()
        p = float("-inf")

        n = len(a)
        for i in range(0, n, 1):
            d, c = self.eval_nesting(i, c, a)
            p = max(p, d)

        if p == float("-inf"):
            return 0
        else:
            return p

    def eval_nesting(self, i, c, a):
        """
        Evaluates maximum nesting distance for target start index.

        :param int i: target start index for nesting cycle
        :param dict[tup[int, int]] c: hash map of start-end index distances
        :param list[int] a: input array of integers
        :return: maximum nesting cycle distance and updated hash map
        :rtype: tup[int, dict[tup[int, int]]]
        """
        j = i
        d = 0

        while a[j] != i:
            if (j, i) in c:
                # Found previous evaluation
                d += c[(j, i)]
                return d, c
            else:
                # Move to next nested value
                d += 1
                c[(i, a[j])] = d
                j = a[j]
        
        # Found target value
        d += 1
        c[(i, a[j])] = d
        return d, c

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of integers
        :rtype: list[int]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = []
        else:
            a = [int(x)
                 for x
                 in inputs[0].split(",")]
        
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_max_nested_array_len(a)
    print(z)


## END OF FILE