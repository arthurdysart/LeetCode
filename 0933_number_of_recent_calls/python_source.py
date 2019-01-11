# -*- coding: utf-8 -*-
"""
Leetcode - Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls

Created on Fri Jan 11 10:43:44 2019
@author: Arthur Dysart
"""


# REQUIRED MODULES
from collections import deque
import json
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Iteration over all input array elements.

    Time complexity: O(n)
      - Amortized iterate over all input array elements
    Space complexity: O(n)
      - Collect elements in output queue
    """

    def eval_ping_counter(self, a, x):
        """
        Evaluates number of ping calls relative to most recent ping request.
        Requires subclass "Recent_Counter".
    
        :param list[str] a: input array of ping calls
        :param list[int] x: input array of ping times
        :return: array of number of recent ping requests
        :rtype: list[int]
        """
        if (not a and
            not x):
            return []

        # Initialize ping counter object and output array
        o = self.Recent_Counter()
        t = ["null"]

        n = len(a)
        for i in range(1, n, 1):

            if a[i] == "ping":
                # Evaluate ping request
                r = o.ping(x[i][0])
                t.append(r)

        return t

    class Recent_Counter:
        """
        Class for ping request storage and evaluation.
        """

        def __init__(self):
            """
            Initialize ping request queue ordered by increasing age.
            """
            self.q = deque()

        def ping(self, t):
            """
            Collects input ping request and removes old ping requests.

            :param int t: input integer representing time of ping rest
            :return: number of recent ping requests
            :rtype: int
            """
            if not t:
                return 0

            # Set pointer to object queue and append most recent ping request
            q = self.q
            q.append(t)

            # Collect target ping request
            p = q[0]

            while p < t - 3000:
                # Remove targest ping request because too old
                q.popleft()
                p = q[0]

            # Determine number of recent ping requests
            return len(q)

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: arrays of input strings and integers
        :rtype: list[list[str], list[int]]
        """
        return [json.loads(x)
                for x
                in sys_stdin]


## MAIN MODULE
if __name__ == "__main__":
    # Imports standard input
    a, x = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .eval_ping_counter(a, x)
    print(json.dumps(z))


## END OF FILE