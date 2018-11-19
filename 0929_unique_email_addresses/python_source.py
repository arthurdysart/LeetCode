# -*- coding: utf-8 -*-
"""
Leetcode - Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses

Created on Mon Nov 19 18:01:33 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Traverse all elements of array

    Time complexity: O(n)
        - Iterate over all string elements
    Space complexity: O(n)
        - Amortized store all unique strings
    """

    def count_unique_emails(self, a):
        """
        Determines number of unique emails in input array.

        :param list[str] a: array of input emails
        :return: number of unique target emails
        :rtype: int
        """
        if not a:
            return 0

        s = set()

        n = len(a)
        for i in range(n):
            l, r = a[i].split("@")
            l = l.replace(".","").split("+")[0]
            m = "@".join([l, r])
            s.add(m)
        
        return len(s)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of input emails
        :rtype: int
        """
        inputs = [x.strip("[]\n") for x in sys_stdin]
        a = [x.strip("\"")
             for x
             in inputs[0].split("\",\"")]
        return a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    a = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .count_unique_emails(a)
    print(z)


## END OF FILE