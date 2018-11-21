# -*- coding: utf-8 -*-
"""
Leetcode - Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters

Created on Wed Nov 21 10:35:49 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iterative search of dynamic window over string.

    Time complexity: O(n)
        - Amortized iterate over all elements with two limit pointers
    Space complexity: O(1)
        - Amortized update constant number of pointers
    """

    def find_long_substr_len(self, s):
        """
        Determines length of longest substring with unique characters.

        :param str s: input string
        :return: maximum substring length with unique characters
        :rtype: int
        """
        if not s:
            return 0

        l = 0
        n = len(s)
        p = float("-inf")

        for r in range(n):
            # Calculate target and actual number of unique characters
            t = r - l + 1
            x = len(set(s[l:r + 1]))
            if x == t:
                p = max(p, x)
            else:
                # Increase left limit to remove repeated character
                l += 1

        if p == float("-inf"):
            # No unique characters found
            return 0
        else:
            return p

class Solution2:
    """
    Optimized iterative two-pointer search of increasing substrings.

    Time complexity: O(n ** 2)
        - Amortized iterate over all start-end index pairs
    Space complexity: O(n)
        - Amortized store all string characters in set
    """

    def find_long_substr_len(self, s):
        """
        Determines length of longest substring with unique characters.

        :param str s: input string
        :return: maximum substring length with unique characters
        :rtype: int
        """
        if not s:
            return 0

        # Initialize pointer for maximum substring length
        p = float("-inf")

        n = len(s)
        for i in range(0, n, 1):
            p = self.eval_substring(p, i, n, s)

        if p == float("-inf"):
            # No unique characters found
            return 0
        else:
            return p

    def eval_substring(self, p, i, n, s):
        """
        Determines length of longest substring with unique characters.
        Iterates across substring length until non-unique character found.

        :param str s: input string
        :return: maximum substring length with unique characters
        :rtype: int
        """
        # Initialize set of unique characters
        x = set(s[i])
        for j in range(i, n, 1):
            x.add(s[j])
            t = j - i + 1
            if len(x) == t:
                # Collected characters are unique
                p = max(p, t)
            else:
                # Collected characters are not unique
                return p

        # All substring characters are unique
        return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input string
        :rtype: str
        """
        inputs = [x.strip("[]\"\n") for x in sys_stdin]
        s = inputs[0]
        return s


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    s = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .find_long_substr_len(s)
    print(z)


## END OF FILE