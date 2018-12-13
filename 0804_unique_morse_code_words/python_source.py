# -*- coding: utf-8 -*-
"""
Leetcode - Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words

Created on Wed Dec 12 22:37:41 2018
@author: Arthur Dysart
"""


# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Pythonic iteration over all characters in input strings.

    Time complexity: O(n * m)
      - Iterate over all characters in all input strings
    Space complexity: O(m)
      - Store maximum number of characters in concatenation array
    """

    def count_unique_morse_codes(self, a):
        """
        Determines number of unique morse codes from input strings.

        :param list[str] a: array of input strings
        :return: number of unique morse code representations
        :rtype: int
        """
        if not a:
            return 0

        u = set()
        d = self.init_hash_map()

        n = len(a)
        for i in range(0, n, 1):

            t = list()

            for c in a[i]:
                t.append(d[c])

            u.add("".join(t))

        return len(u)

    def init_hash_map(self):
        """
        Initializes hash map of morse code character translations.

        :return: hash map of string character to morse code representation
        :rtype: dict[str: str]
        """
        return {"a": ".-",
                "b": "-...",
                "c": "-.-.",
                "d": "-..",
                "e": ".",
                "f": "..-.",
                "g": "--.",
                "h": "....",
                "i": "..",
                "j": ".---",
                "k": "-.-",
                "l": ".-..",
                "m": "--",
                "n": "-.",
                "o": "---",
                "p": ".--.",
                "q": "--.-",
                "r": ".-.",
                "s": "...",
                "t": "-",
                "u": "..-",
                "v": "...-",
                "w": ".--",
                "x": "-..-",
                "y": "-.--",
                "z": "--.."}

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of input strings
        :rtype: list[str]
        """
        inputs = [x.strip("[]\"\n")
                  for x
                  in sys_stdin]

        if inputs[0] == "":
            a = list()
        else:
            a = [x.strip("\"")
                 for x
                 in inputs[0].split(", ")]

        return a


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a = Input()\
        .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .count_unique_morse_codes(a)
    print(z)


## END OF FILE