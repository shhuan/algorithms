# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-04 15:10

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        """
        从最外面一圈开始，一圈一圈的旋转。
        :param matrix:
        :return:
        """
        if not matrix:
            return

        n = len(matrix)
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(n//2):
            ltr, ltc, rbr, rbc = i, i, n-i-1, n-i-1
            for t in range(rbr-ltr):
                # 正方形每个边有rbr-ltr个元素
                tmp = matrix[ltr][ltc]
                r, c = ltr, ltc
                for d in delta:
                    while ltr <= r <= rbr and ltc <= c <= rbc:
                        nr = r + d[0]
                        nc = c + d[1]
                        if nr > rbr or nr < ltr or nc > rbc or nc < ltc:
                            break
                        matrix[r][c] = matrix[nr][nc]
                        r, c = nr, nc
                matrix[r][c+1] = tmp

s = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s.rotate(matrix)
for row in matrix:
    print(row)



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
s.rotate(matrix)
for row in matrix:
    print(row)
