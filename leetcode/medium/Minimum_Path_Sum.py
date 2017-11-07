# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 14:29


Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        """
        f(i, j) = min{f(i-1, j), f(i, j-1)} + grid(i, j)
        :param grid:
        :return:
        """
        if not grid:
            return 0

        count = [[1000000 for c in range(len(grid[0]))] for r in range(len(grid))]
        count[0][0] = grid[0][0]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if r > 0 or c > 0:
                    if r > 0:
                        count[r][c] = count[r-1][c] + grid[r][c]
                    if c > 0:
                        count[r][c] = min(count[r][c], count[r][c-1]+grid[r][c])
        # for r in count:
        #     print(r)
        return count[len(grid)-1][len(grid[0])-1]


s = Solution()
g = [
    [1, 2, 1],
    [2, 0, 3],
    [4, 5, 1]
]
print(s.minPathSum(g))