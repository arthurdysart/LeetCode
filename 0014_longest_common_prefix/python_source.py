# -*- coding: utf-8 -*-
"""
Leetcode - Longest common prefix
https://leetcode.com/problems/longest-common-prefix
Iterative solution

Created on Sat Nov  3 15:29:06 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    def longest_common_prefix(self, a):
        """
        Determines the longest common prefix among words in array "a".
        :type a: List[str]
        :rtype: str
        """
        if not a:
            return ""
        else:
            # Finds shortest word
            m = min(a, key=len)

            for n in range(len(m)):
                c = {s[n] for s in a}
                if len(c) > 1:
                    return m[:n]
            return m

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    return [x.strip("[]\n").split(",") for x in sys_stdin][0]


if __name__ == "__main__":
    # Imports standard input
    a = stdin(sys.stdin)
    
    # Evaluates solution
    s = Solution()
    r = s.longest_common_prefix(a)
    print(r)