# -*- coding: utf-8 -*-
"""
Leetcode - Heaters
https://leetcode.com/problems/heaters/

Created on Sun Dec  2 23:55:00 2018
Updated on Mon Dec  3 15:07:11 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# MODULE DEFINITIONS
class Solution:
    """
    Iteration and binary search over input arrays.

    Time complexity: O(len(n) + len(m))
      - Amortized iterate over all elements of both input arrays
    Space complexity: O(1)
      - Update constant pointers with modified "heater" array in-place
    """

    def find_heating_radius(self, h, q):
        """
        Determines minimum required heating radius to reach all houses.

        :param list[int] h: array of house positions
        :param list[int] q: array of heater positions
        :return: minimum required heating radius
        :rtype: int
        """
        if (not h or
            not q):
            return 0

        # Modify house and heater position arrays
        h.sort()
        q = self.mod_heaters(q)

        # Initialize pointers for heater index and heating radius
        j = 0
        p = float("-inf")

        n = len(h)
        for i in range(0, n, 1):

            while q[j] < h[i]:
                # Increase heater index until after target house
                j += 1

            # Evaluate minimum heating distance for target house
            d = min(h[i] - q[j - 1],
                    q[j] - h[i])

            # Evaluate maximum required heating radius
            p = max(p, d)

        if p == float("-inf"):
            return 0
        else:
            return p

    def mod_heaters(self, q):
        """
        Appends infinite position limits to input heater position array.
        
        :param list[int] q: array of heater positions
        :return: modified array of heater positions
        :rtype: list[int and float]
        """
        q.append(float("-inf"))
        q.append(float("inf"))
        q.sort()
        return q

class Solution2:
    """
    Iteration and binary search over input arrays.

    Time complexity: O(n * log(n))
      - Iterate over "house" array with binary search of "heater" array
    Space complexity: O(1)
      - Update constant pointers with modified "heater" array in-place
    """

    def find_heating_radius(self, h, q):
        """
        Determines minimum required heating radius to reach all houses.

        :param list[int] h: array of house positions
        :param list[int] q: array of heater positions
        :return: minimum required heating radius
        :rtype: int
        """
        if (not h or
            not q):
            return 0

        # Initialize modified heater array and radius pointer
        q = self.mod_heaters(q)
        p = float("-inf")

        for i in h:
            # For each house, find minimum required heating distance
            t = self.find_min_dist(i, q)
            p = max(t, p)

        if p == float("-inf"):
            return 0
        else:
            return p

    def mod_heaters(self, q):
        """
        Appends infinite position limits to input heater position array.
        
        :param list[int] q: array of heater positions
        :return: modified array of heater positions
        :rtype: list[int and float]
        """
        q.append(float("-inf"))
        q.append(float("inf"))
        q.sort()
        return q

    def find_min_dist(self, i, q):
        """
        Determines minimum distance between target house and nearest heater(s).
        Interpolates binary search algorithm (right-limit bias).

        :param int h: target house position
        :param list[int and float] q: modified array of heater positions
        :return: minimum heating distance
        :rtype: int
        """
        if not q:
            return float("inf")

        l = 0
        r = len(q) - 1        
        while l < r:
            # Execute binary search
            m = l + (r - l) // 2

            if q[m] == i:
                # Ignore target house which contains heater
                return float("-inf")
            elif q[m] < i:
                l = m + 1
            else:
                r = m

        # Evaluate minimum heating distance from nearest heaters
        return min(i - q[l - 1],
                   q[l] - i)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input arrays of integers
        :rtype: tup[list[int], list[int]]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        a = self.cast_int_arr(inputs[0])
        q = self.cast_int_arr(inputs[1])

        return a, q

    def cast_int_arr(self, s):
        """
        Converts string to array of integers.

        :param str s: input string
        :return: array of integers
        :rtype: list[int]
        """
        if s == "":
            a = list()
        else:
            a = [int(x)
                 for x
                 in s.split(",")]
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a, q = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .find_heating_radius(a, q)
    print(z)


## END OF FILE