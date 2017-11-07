# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:55

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def uniquePaths(self, m, n):
        if n == 0 or m== 0:
            return 0
        if m == 1 or m == 1:
            return 1

        g = [[0 for c in range(n)] for c in range(m)]
        g[0][0] = 1
        for r in range(m):
            for c in range(n):
                if c+1 <= n-1:
                    g[r][c+1] += g[r][c]
                if r+1 <= m-1:
                    g[r+1][c] += g[r][c]

        return g[m-1][n-1]