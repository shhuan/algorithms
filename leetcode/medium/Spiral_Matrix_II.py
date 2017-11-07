# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:56


Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n <= 0:
            return []

        ret = [[0 for c in range(n)] for r in range(n)]
        left = 0
        right = n
        up = 0
        down = n

        r = 0
        c = 0
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di = 0
        dir = delta[di]
        num = 1

        while left < right and up < down:
            while left <= c < right and up <= r < down:
                ret[r][c] = num
                num += 1
                r += dir[0]
                c += dir[1]
            r -= dir[0]
            c -= dir[1]
            if di == 0:
                up += 1
            elif di == 1:
                right -= 1
            elif di == 2:
                down -= 1
            elif di == 3:
                left += 1
            di = (di + 1) % 4
            dir = delta[di]
            r += dir[0]
            c += dir[1]
        return ret