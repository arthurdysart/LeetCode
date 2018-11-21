# -*- coding: utf-8 -*-
"""
Leetcode - Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum

Created on Tue Nov 20 13:45:34 2018
@author: Arthur Dysart
"""


## REQUIRED MODULES
import sys


## MODULE DEFINITIONS
class Solution:
    """
    Iterative dynamic window search over array of incremental cumulative sums.

    Time complexity: O(n)
        - Amortized iterate over all elements with two limit pointers
    Space complexity: O(1)
        - Amortized update constant number of pointers
    """

    def find_min_sub_len(self, x, a):
        """
        Determines minimum subarray length to meet or exceed target sum.

        :param int x: target integer sum
        :param list[int] a: array of input positive integers
        :return: minimum number of elements required for target sum
        :rtype: int
        """
        if not a:
            return 0

        # Initialize minimum subarray length, running sum, and left limit
        p = float("inf")
        s = 0
        l = 0

        n = len(a)
        for r in range(0, n, 1):
            # Add right element to running sum
            s += a[r]
            # Check whether running sum is equal to or greater than target sum
            while s >= x:
                # Calculate and evaluate length of target subarray
                w = r - l + 1
                p = min(p, w)
                # Remove left value from running sum, then increment limit
                s -= a[l]
                l += 1
                
        if p == float("inf"):
            # No subarray sum found
            return 0
        else:
            return p

class Solution2:
    """
    Iterative binary search over array of incremental cumulative sums.

    Time complexity: O(n * log(n))
        - Amortized iterate over array with binary search for cumulative sum
    Space complexity: O(n)
        - Amortized store array of incremental cumulative sums
    """

    def find_min_sub_len(self, x, a):
        """
        Determines minimum subarray length to meet or exceed target sum.

        :param int x: target integer sum
        :param list[int] a: array of input positive integers
        :return: minimum number of elements required for target sum
        :rtype: int
        """
        if not a:
            return 0
        
        n = len(a)
        # Initialize array of incremental cumulative sums
        s = [0]
        for i in range(n):
            s.append(s[-1] + a[i])

        # Initialize minimum subarray length
        p = float("inf")

        m = len(s)
        for i in range(m):
            t = s[i] + x
            if t <= s[-1]:
                j = self.find_target_sum(i, t, s)
                p = min(p, j - i)

        if p == float("inf"):
            # No subarray sum found
            return 0
        else:
            return p

    def find_target_sum(self, i, t, s):
        """
        Determines index of target cumulative sum using binary search.
        Note incremental cumulative sum is sorted in ascending order
        because all elements of array "a" are positive integers.

        :param int t: target cumulative sum
        :param list[int] s: array of incremental cumulative sums
        :return: index of 
        :rtype: int
        """
        if not s:
            return -1

        l = i
        r = len(s) -1
        while l <= r:
            m = l + (r - l) // 2
            if s[m] == t:
                return m
            elif s[m] < t:
                l = m + 1
            else:
                r = m - 1
        return l

class Solution3:
    """
    Simplified dynamic programming (tabulation, bottom-up) algorithm.

    Time complexity: O(n ** 2)
        - Amortized iterate over all start index and sublength combinations
    Space complexity: O(n)
        - Amortized store sum combinations for current sublength
    """

    def find_min_sub_len(self, x, a):
        """
        Determines minimum subarray length to meet or exceed target sum.

        :param int n: target integer sum
        :param list[int] a: array of input positive integers
        :return: minimum number of elements required for target sum
        :rtype: int
        """
        if not a:
            return 0

        n = len(a)
        # Check initial array
        for i in range(0, n, 1):
            if a[i] >= x:
                return 1

        # Initialize cache for subarray sums and pointer for previous cache
        c = [None for i in range(0, n, 1)]
        p = a

        # Iterate over length of subarray (rows)
        for i in range(1, n, 1):
            # Iterate over index in main array (columns)
            for j in range(0, n - i, 1):
                # Calculate sum for subarray
                s = p[j] + a[i + j]

                if s >= x:
                    # Subarray found
                    return i + 1
                else:
                    c[j] = s
            p = c

        # No subarray sum found
        return 0

class Solution4:
    """
    Routine dynamic programming (tabulation, bottom-up) algorithm.

    Time complexity: O(n ** 2)
        - Amortized iterate over all start index and sublength combinations
    Space complexity: O(n ** 2)
        - Amortized store sum for all start index and sublength combinations
    """

    def find_min_sub_len(self, x, a):
        """
        Determines minimum subarray length to meet or exceed target sum.

        :param int n: target integer sum
        :param list[int] a: array of input positive integers
        :return: minimum number of elements required for target sum
        :rtype: int
        """
        if not a:
            return 0

        n = len(a)
        # Initialize cache for subarray sums
        c = [[None] * (n - i) for i in range(0, n, 1)]

        # Populate first row
        for j in range(0, n, 1):
            if a[j] >= x:
                return 1
            else:
                c[0][j] = a[j]

        # Iterate over length of subarray (rows)
        for i in range(1, n, 1):
            # Iterate over index in main array (columns)
            for j in range(0, n - i, 1):
                # Calculate sum for subarray
                s = c[i - 1][j] + c[0][i + j]

                if s >= x:
                    # Subarray found
                    return i + 1
                else:
                    c[i][j] = s

        # No subarray sum found
        return 0

class Solution5:
    """
    Iterative brute-force solution.

    Time complexity: O(n ** 2)
        - Amortized iterate over all start index and sublength combinations
    Space complexity: O(1)
        - Update constant number of pointers
    """

    def find_min_sub_len(self, x, a):
        """
        Determines minimum subarray length to meet or exceed target sum.

        :param int n: target integer sum
        :param list[int] a: array of input positive integers
        :return: minimum number of elements required for target sum
        :rtype: int
        """
        if not a:
            return 0

        # Initialize pointer for minimial subarray length
        p = float("inf")

        n = len(a)        
        for i in range(0, n, 1):
            s = 0
            for j in range(i, n, 1):
                s += a[j]
                if s >= x:
                    # Minimum target sum found
                    p = min(p, j - i + 1)

        if p == float("inf"):
            return 0
        else:
            return p

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: array of input positive integers and target sum
        :rtype: tuple[int, list[int]]
        """
        inputs = [x.strip("[]\n") for x in sys_stdin]
        a = [int(x.strip())
             for x
             in inputs[0].split(",")]
        x = int(inputs[1])
        return x, a


## MAIN MODULE
if __name__ == "__main__":
    # Import exercise parameters
    x, a = Input()\
           .stdin(sys.stdin)

    # Evaluate solution
    z = Solution()\
        .find_min_sub_len(x, a)
    print(z)


## END OF FILE