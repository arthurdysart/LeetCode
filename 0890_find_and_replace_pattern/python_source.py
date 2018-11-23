# -*- coding: utf-8 -*-
"""
Leetcode - Find and Replace Pattern
https://leetcode.com/problems/find-and-replace-pattern

Created on Fri Nov 23 00:18:48 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
from collections import defaultdict
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iteration over character pairs for each string in input array.

    Time complexity: O(len(s) * n)
        - Amortized iterate over all characters for all input strings
    Space complexity: O(n)
        - Amortized append all strings from input array
    """

    def find_replace_pattern(self, a, p):
        """
        Determine strings in array that follow specified character pattern.

        :param list[str] a: input array of strings
        :param str p: target character pattern to match each input string
        :return: array of strings which match target character pattern
        :rtype: list[str]
        """
        if not a:
            return list()
        
        t = list()
        for s in a:
            if self.is_pattern_match(s, p):
                t.append(s)
        return t
    
    def is_pattern_match(self, s, p):
        """
        Determines whether input string matches target character pattern.

        :param str s: input string
        :param str p: target character pattern to match input string
        :return: True if input string matches target character pattern
        :rtype: bool
        """
        d = defaultdict(str)

        for k, v in zip(p, s):
            if d[k] == "":
                # Character has not been mapped
                d[k] = v
            elif d[k] != v:
                # Mapped character does not match pattern
                return False
 
        if len(set(d.keys())) == len(set(d.values())):
            # All mapped pattern-character pairs are unique
            return True
        else:
            # String character is mapped to different pattern characters
            return False

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of input strings and target character pattern
        :rtype: tuple[list[str], str]
        """
        inputs = [x.strip("[]\"\n") for x in sys_stdin]
        a = [x
             for x
             in inputs[0].split("\",\"")]
        p = inputs[1]
        return a, p


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a, p = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .find_replace_pattern(a, p)
    print(z)


## END OF FILE