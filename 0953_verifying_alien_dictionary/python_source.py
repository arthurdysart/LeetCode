# -*- coding: utf-8 -*-
"""
Leetcode - Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary

Created on Sat Dec  8 23:25:43 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over character indicies in input strings.

    Time complexity: O(max(k, n * m))
      - Amortized iterate over lexographic order and input array strings
    Space complexity: O(k)
      - Collect all characters in lexographic order string using hash map
    """

    def is_alien_sorted(self, a, x):
        """
        Determines whether input strings follow specified lexographic order.

        :param list[str] a: input array of ordered strings
        :param str x: string representing target lexographic order
        :return: True if input array is sorted by target lexographic order
        :rtype: bool
        """
        if (not a or
            not x):
            return False

        # Initialize hash map for lexographic order
        d = {c: i for (i, c) in enumerate(x, 1)}
        d[""] = 0

        # Set max target word indicies and max character length
        n = len(a) - 1
        m = max(len(s) for s in a)

        j = 0
        while j < m:
            for i in range(n, 0, -1):

                # Retrieve comparison character for target word
                if j >= len(a[i]):
                    u = ""
                else:
                    u = a[i][j]

                # Retrieve comparison character for previous word    
                if j >= len(a[i - 1]):
                    v = ""
                else:
                    v = a[i - 1][j]
                
                if d[u] > d[v]:
                    # Found lexographic order and remove target word
                    a[i] = a[i - 1]

                elif u == v:
                    # Continue in sequence as currently same
                    continue

                else:
                    # Found non-lexographic order
                    return False

            # Move to next target character index
            j += 1

        # All words identical or in lexographic order
        return True

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input array of ordered strings and target string
        :rtype: tup[list[str], str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = list()
        else:
            a = [str(x).strip("\"")
                 for x
                 in inputs[0].split("\",\"")]

        x = inputs[1]

        return a, x


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a, x = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_alien_sorted(a, x)
    print(z)


## END OF FILE