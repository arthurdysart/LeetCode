# -*- coding: utf-8 -*-
"""
Leetcode - Remove duplicates from sorted array
https://leetcode.com/problems/remove-duplicates-from-sorted-array
Two pointers (forwarding) solution

Created on Fri Nov  2 21:57:17 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    def remove_duplicates(self, a):
        """
        Deletes elements from array "a" if identical to other elements.

        :type a: list[int]
        :rtype: int
        """
        # Checks for unitary or empty array
        if len(a) < 2:
            return len(a)
        # Executes two pointer fowarding
        else:
            l = 0
            r = 1
            while r < len(a):
                if a[l] == a[r]:
                    del a[r]
                else:
                    l += 1
                    r += 1
            return len(a)

def stdin(sys_stdin):
    """
    Imports standard input.
    """
    inputs = [x.strip("[]\n").split(",") for x in sys_stdin]
    return [int(x) for x in inputs[0]]


if __name__ == "__main__":
    # Imports standard input
    a = stdin(sys.stdin)

    # Evaluates solution
    s = Solution()
    r = s.remove_duplicates(a)
    print(r)