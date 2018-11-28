# -*- coding: utf-8 -*-
"""
Leetcode - Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency

Created on Tue Nov 27 21:34:19 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import defaultdict
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over string characters and sorted character-frequency tuples.

    Time complexity: O(n + k * log(k))
      - Average sort all character-frequency pairs and iterate over string
    Space complexity: O(n)
      - Create new array and dictionary of all string characters
    """

    def frequency_sort(self, s):
        """
        Sorts string using "frequency sort" algorithm.

        :param str s: string to be sorted
        :return: characters ordered by descending freqeuency
        :rtype: str
        """
        if not s:
            return ""

        # Count frequencies of all characters
        t = self.count_char_freq(s)

        a = list()
        # Order characters by frequency
        for c, f in t:
            for i in range(0, f, 1):
                a.append(c)
        
        return "".join(a)

    def count_char_freq(self, s):
        """
        """
        d = defaultdict(int)

        # Count frequencies of all characters
        for c in s:
            d[c] += 1

        # Sort all character-frequency pairs in descending order
        t = sorted(d.items(),
                   key = lambda x: (x[1], -1 * x[0]),
                   reverse = True)
        return t

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: target integer
        :rtype: int
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        s = inputs[0]

        return s


if __name__ == "__main__":
    # Imports standard input
    s = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .frequency_sort(s)
    print(z)