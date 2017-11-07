# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 22:33

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.


把每一行连接起来成为一个一维数组，是严格递增的，所以直接利用二叉查找即可
"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix)*len(matrix[0])

        while left < right:
            mid = left + (right - left)//2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid
        return False

s = Solution()
m = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(s.searchMatrix(m, 3))
print(s.searchMatrix(m, 12))
print(s.searchMatrix([[1, 1]], 0))