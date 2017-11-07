# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 22:10

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

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
    # @return nothing (void), do not return anything, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        """
        把后设置的0和本来就是的0区分开就可以了
        :param matrix:
        :return:
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    for rr in range(len(matrix)):
                        if rr != r and matrix[rr][c] != 0:
                            matrix[rr][c] = -100000
                    for cc in range(len(matrix[r])):
                        if cc != c and matrix[r][cc] != 0:
                            matrix[r][cc] = -100000
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == -100000:
                    matrix[r][c] = 0

    def setZeroes2(self, matrix):
        """
        或者使用第一行，第一列记录哪些行和列需要置0
        :param matrix:
        :return:
        """
        firstRowZero = matrix[0].count(0) > 0
        firstColZero = len(list(filter(lambda x: x[0] == 0, matrix))) > 0

        # 记录哪些行列需要置0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # 把这些行列都置为0，注意从1开始
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(1, len(matrix)):
                    matrix[r][c] = 0
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(1, len(matrix[r])):
                    matrix[r][c] = 0
        # 第一行、第一列是否需要置0
        if firstRowZero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if firstColZero:
            for r in range(len(matrix)):
                matrix[r][0] = 0




s = Solution()
m = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
for r in m:
    print(r)
print()
s.setZeroes2(m)
for r in m:
    print(r)