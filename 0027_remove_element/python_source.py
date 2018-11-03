# -*- coding: utf-8 -*-
"""
Leetcode - Remove element
https://leetcode.com/problems/remove-element
One pointer (forwarding) solution

Created on Fri Nov  2 22:17:01 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    def remove_element(self, a, x):
        """
        Deletes elements with value "x" from array "a".
        
        :type a: list[int]
        :type x: int
        :rtype: int
        """
        if len(a) < 1:
            return 0
        else:
            r = 0
            while r < len(a):
                if a[r] == x:
                    del a[r]
                else:
                    r += 1
            return len(a)

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip("[]\n").split(",") for x in sys_stdin]
    a = [int(x) for x in inputs[0]]
    x = int(inputs[1][0])
    return a, x


if __name__ == "__main__":
    # Imports standard input
    a, x = stdin(sys.stdin)

    # Evaluates solution
    s = Solution()
    r = s.remove_element(a, x)
    print(r)