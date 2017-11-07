# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 15:47

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
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]



s = Solution()

image = [
    [1, 2, 3],
    [2, 9, 11],
    [6, 7, 8],
]

s.rotate(image)

for r in image:
    print(r)