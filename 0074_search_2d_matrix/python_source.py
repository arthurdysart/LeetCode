# -*- coding: utf-8 -*-
"""
Leetcode - Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix

Created on Sat Nov 24 12:41:49 2018
@author: Arthur Dysart
"""

# REQUIRED MODULES
import sys


# FUNCTION DEFINITIONS
class Solution:
    """
    Successive binary search of 2 1D arrays.

    Time complexity: O(log(n * m))
      - Execute binary search on first-elements then target row of 2D array
    Space complexity: O(1)
      - Update constant pointers
    """

    def search_matrix(self, a, x):
        """
        Determines whether target element exists in 2D array.

        :param list[list[int]] a: input 2D array of sorted integers
        :param int x: target integer to find in array
        :return: True if target element found in array
        :rtype: bool
        """
        if (not a or
            not a[0]):
            return False
        
        n = len(a)
        m = len(a[0])

        if x < a[0][0]:
            return False
        else:
            i = self.find_row_index(a, x, n)

        if x > a[i][-1]:
            return False
        else:
            return self.is_target_present(a[i], x, m)
        
    def find_row_index(self, a, x, n):
        """
        Determines row of 2D array which may contain target integer.

        :param list[int] b: index of first elements of each row in 2D array
        :param int x: target integer to find in array
        :return: index of row which may contain target integer
        :rtype: int
        """
        if not a:
            return False
        
        l = 0
        r = n - 1
        while l < r:
            m = l + (r - l) // 2
            if a[m][0] == x:
                return m
            elif a[m][0] > x:
                r = m
            else:
                l = m + 1
        
        if a[l][0] <= x:
            return l
        else:
            return l - 1
    
    def is_target_present(self, a, x, m):
        """
        Determines whether target element in specified row of 2D array.

        :param list[int] a: row of 2D array which may contain target integer
        :param int x: target integer to find in array
        :return: True if target element found in array
        :rtype: bool
        """
        l = 0
        r = m - 1
        while l <= r:
            m = l + (r - l) // 2
            if a[m] == x:
                return True
            elif a[m] > x:
                r = m - 1
            else:
                l = m + 1

        return False

class Solution2:
    """
    Successive binary search of 2 1D arrays.

    Time complexity: O(n)
      - Create index array, then binary search on two arrays
    Space complexity: O(1)
      - Update constant pointers
    """

    def search_matrix(self, a, x):
        """
        Determines whether target element exists in 2D array.

        :param list[list[int]] a: input 2D array of sorted integers
        :param int x: target integer to find in array
        :return: True if target element found in array
        :rtype: bool
        """
        if (not a or
            not a[0]):
            return False

        n = len(a)
        b = [a[r][0] for r in range(n)]

        if x < b[0]:
            return False
        else:
            i = self.find_row_index(b, x)

        if x > a[i][-1]:
            return False
        else:
            return self.is_target_present(a[i], x)

    def find_row_index(self, b, x):
        """
        Determines row of 2D array which may contain target integer.

        :param list[int] b: index of first elements of each row in 2D array
        :param int x: target integer to find in array
        :return: index of row which may contain target integer
        :rtype: int
        """
        if not b:
            return False

        l = 0
        r = len(b) - 1
        while l < r:
            # Execute binary search
            m = l + (r - l) // 2
            if b[m] == x:
                return m
            elif b[m] > x:
                r = m
            else:
                l = m + 1

        if b[l] <= x:
            return l
        else:
            return l - 1

    def is_target_present(self, a, x):
        """
        Determines whether target element in specified row of 2D array.

        :param list[int] a: row of 2D array which may contain target integer
        :param int x: target integer to find in array
        :return: True if target element found in array
        :rtype: bool
        """
        if not a:
            return False

        l = 0
        r = len(a) - 1
        while l <= r:
            # Execute binary search
            m = l + (r - l) // 2
            if a[m] == x:
                return True
            elif a[m] > x:
                r = m - 1
            else:
                l = m + 1

        return False

class Input:

    def stdin(self, sys_stdin):
        """
        Imports standard input.

        :param _io.TextIOWrapper sys_stdin: standard input
        :return: input 2D array of integer values and target integer
        :rtype: tuple[list[list[int]], int]
        """
        inputs = [x.strip("[]\n").split("],[")
                  for x
                  in sys_stdin]

        if inputs[0][0] == "":
            a = list([list()])
        else:
            a = [list(map(int,x.split(",")))
                 for x
                 in inputs[0]]

        x = int(inputs[1][0])

        return a, x


if __name__ == "__main__":
    # Imports standard input
    a, x = Input()\
           .stdin(sys.stdin)

    # Evaluates solution
    z = Solution()\
        .search_matrix(a, x)
    print(z)