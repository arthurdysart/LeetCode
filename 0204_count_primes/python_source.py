# -*- coding: utf-8 -*-
"""
Leetcode - Count Primes
https://leetcode.com/problems/count-primes

Created on Mon Nov 19 00:19:14 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Traverse array using the "Sieve of Eratosthenes" Algorithm.

    Time complexity: O(n * log(log(n)))
        - Iterate all integers up to n ** 0.5 and multiples below n
    Space complexity: O(n)
        - Requires array of size n
    """

    def count_primes(self, n):
        """
        Determines number of prime integers below input value.
        Using the "Sieve of Eratosthenes" Algorithm, all integers
        which are multiples of primes are excluded as candidates
        in subsequent evaluations.

        :param int n: maximum value for prime range (exclusive)
        :return: number of prime integers below input value
        :rtype: int
        """
        # No primes found below 2
        if n <= 2:
            return 0

        # Creates array of candidate integers
        a = self.create_candidates(n)

        # Tests integers up to the square root of input value
        m = int(n ** 0.5) + 1
        for i in range(3, m):
            # Evaluate non-primes only from prime integers
            if a[i] == 1:
                # Initialize factor value
                j = 2
                while i * j < n:
                    # Set all multiples of primes as non-primes
                    a[i * j] = 0
                    j += 1

        return sum(a)

    def create_candidates(self, n):
        """
        Determines candidates for prime integers below input value.

        :param int n: maximum value for prime range (exclusive)
        :return: array of all integers below input value
        :rtype: list[int]
        """
        a = [1
             # Excludes integers 0 and 1
             if (i > 1 and
                 # Excludes even integers
                 i % 2 == 1)
             else 0
             for i
             in range(n)]
        a[2] = 1
        return a

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: maximum value for prime range (exclusive)
        :rtype: int
        """
        inputs = [x.strip("\n") for x in sys_stdin]
        n = int(inputs[0])
        return n


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    n = Input()\
        .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .count_primes(n)
    print(z)


## END OF FILE