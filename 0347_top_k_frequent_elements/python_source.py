# -*- coding: utf-8 -*-
"""
Leetcode - Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements

Created on Wed Nov 28 16:26:12 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import defaultdict
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over array of elements and hash map of element frequencies.

    Time complexity: O(n)
      - Amortized traverse all array elements and hash map items
    Space complexity: O(n)
      - Amortized collect all items in hash map with unit frequency
    """

    def top_k_freqent(self, a, k):
        """
        Reports the "k" top most frequent elements within input array.

        :param list[int] a: input array of integers
        :param int k: number of elements to report
        :return: array of top "k" most frequent elements
        :rtype: list[int]
        """
        if not a:
            return list()

        d = defaultdict(int)
        p = float("-inf")

        # Count all elements in array
        n = len(a)
        for i in range(0, n, 1):
            d[a[i]] += 1
            p = max(p, d[a[i]])

        # Create list of top "k" most frequent elements
        t = self.get_top_elements(p, k, d)
        return t

    def get_top_elements(self, p, k, d):
        """
        Collects top "k" top most frequent elements in output array.

        :param int p: target frequency to determine top elements
        :param int k: number of elements to report
        :param dict[int: int] d: hash map of elements and their frequencies
        :return: array of most frequent elements
        :rtype: list[int]
        """
        t = list()
        while len(t) < k:
            for e, f in d.items():
                if f == p:
                    t.append(e)
                if len(t) == k:
                    return t
            # Decrease target frequency
            p -= 1
        return t


class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of integers and number of elements
        :rtype: tuple[list[int], int]
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
        
        k = int(inputs[1])

        return a, k


if __name__ == "__main__":
    # Imports standard input
    a, k = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .top_k_freqent(a, k)
    print(z)