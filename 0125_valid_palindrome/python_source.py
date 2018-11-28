# -*- coding: utf-8 -*-
"""
Leetcode - Valid palindrome
https://leetcode.com/problems/valid-palindrome

Created on Sat Nov  3 15:47:03 2018
Updated on Tue Nov 27 23:42:28 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over character indicies in string.

    Time complexity: O(n)
      - Amortized iterate over all characters in string
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def is_palindrome(self, s):
        """
        Determines whether alphanumeric characters comprise a valid palindrome.

        :param str s: input string
        :return: True if relevant string characters are valid palindrome
        :rtype: bool
        """
        if not s:
            return True

        l = 0
        r = len(s) - 1

        while l < r:

            # Move pointers to next valid characters
            l, r = self.eval_next_char(l, r, s)

            if (l == len(s) - 1 and
                r == 0):
                # No valid characters found
                return True

            elif s[l].lower() != s[r].lower():
                # Invalid palindrome
                return False

            else:
                l += 1
                r -= 1

        # Valid palindrome
        return True

    def eval_next_char(self, l, r, s):
        """
        Moves index pointers to next alphanumeric character.

        :param int l: pointer to left-most target index
        :param int r: pointer to right-most target index
        :param str s: input string
        :return: updated index pointers
        :rtype: tuple[int, int]
        """
        while (not s[l].isalnum() and
               l < len(s) - 1):
            l += 1

        while (not s[r].isalnum() and
               r > 0):
            r -= 1

        return l, r

class Solution2:
    """
    Iteration over character indicies in string.

    Time complexity: O(n)
      - Amortized iterate over all characters in string
    Space complexity: O(1)
      - Update constant number of pointers
    """

    def is_palindrome(self, s):
        """
        Determines whether alphanumeric characters comprise a valid palindrome.

        :param str s: input string
        :return: True if relevant string characters are valid palindrome
        :rtype: bool
        """
        if not s:
            return True

        l = 0
        r = len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].upper() != s[r].upper():
                return False
            else:
                l += 1
                r -= 1
        return True

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of strings
        :rtype: list[str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        s = inputs[0]

        return s


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    s = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .is_palindrome(s)
    print(z)


## END OF FILE