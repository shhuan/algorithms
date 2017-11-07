# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:54

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

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
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        pg = [[0 for c in range(len(obstacleGrid[0]))] for c in range(len(obstacleGrid))]
        pg[0][0] = 1

        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[r])):
                if obstacleGrid[r][c] == 0:
                    if c < len(obstacleGrid[r])-1 and obstacleGrid[r][c+1] == 0:
                        pg[r][c+1] += pg[r][c]
                    if r < len(obstacleGrid)-1 and obstacleGrid[r+1][c] == 0:
                        pg[r+1][c] += pg[r][c]
        return pg[len(obstacleGrid)-1][len(obstacleGrid[-1])-1]