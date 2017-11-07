# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/3 18:36


Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections
import bisect

class Solution(object):
    def searchMatrix2(self, matrix, target):
        """
        268ms
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        maxRowIndex = bisect.bisect_right([row[0] for row in matrix], target)
        maxColIndex = bisect.bisect_right(matrix[0], target)

        for ri in range(maxRowIndex):
            row = matrix[ri]
            if self.binary_search(row, 0, maxColIndex, target) != -1:
                return True
        return False


    def searchMatrix3(self, matrix, target):
        """
        152ms
        一行一行的进行二叉查找
        如果第一个元素比target大，结束查找并返回False
        每一行查找的有边界是上一行的最后一个小于target的元素的下标
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return False

        maxColIndex = len(matrix[0])
        for row in matrix:
            if row[0] > target:
                return False
            maxColIndex = bisect.bisect_right(row, target, 0, maxColIndex)
            if maxColIndex > 0 and row[maxColIndex-1] == target:
                return True

        return False

    def searchMatrix(self, matrix, target):
        """
        140ms O(m+n)
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return False

        rowCount = len(matrix)
        colCount = len(matrix[0])
        ri = 0
        ci = colCount - 1
        while ri < rowCount and ci >= 0:
            if matrix[ri][ci] == target:
                return True
            elif matrix[ri][ci] < target:
                ri += 1
            else:
                ci -= 1

        return False



    def binary_search(self, nums, left, right, val):
        """
        search val in nums[lefr: right], doesn't contain nums[right]
        :param nums:
        :param left:
        :param right:
        :param val:
        :return:
        """

        if not nums or left >= right or len(nums) < right:
            return -1

        while left < right:
            mid = left + (right -  left) // 2
            if nums[mid] == val:
                return mid
            elif nums[mid] > val:
                right = mid
            else:
                left = mid + 1

        return -1

s = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(s.searchMatrix(matrix, 5))
print(s.searchMatrix(matrix, 20))


matrix = [[-1, 3]]
print(s.searchMatrix(matrix, 3))

matrix = [[-5]]
print(s.searchMatrix(matrix, -5))