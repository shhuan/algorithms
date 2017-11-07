# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:01

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

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
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di = 0
        dir = delta[di]

        result = []
        row = 0
        col = 0
        l = 0
        r = len(matrix[0])
        u = 0
        d = len(matrix)

        i = 0
        j = 0
        while l < r and u < d:
            while i in range(u, d) and j in range(l, r):
                result.append(matrix[i][j])
                i += dir[0]
                j += dir[1]
            i -= dir[0]
            j -= dir[1]
            if di == 0:
                u += 1
            elif di == 1:
                r -= 1
            elif di == 2:
                d -= 1
            elif di == 3:
                l += 1
            di = (di + 1) % 4
            dir = delta[di]
            i += dir[0]
            j += dir[1]

        return result