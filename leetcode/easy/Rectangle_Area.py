# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 13:52

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.



两个正方形的面积-重叠的面积

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        areaA = (C - A) * (D - B)
        areaB = (G - E) * (H - F)
        l = max(0, min(C, G) - max(A, E))
        h = max(0, min(D, H) - max(B, F))
        return areaA + areaB - l * h


s = Solution()
print(s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2), 6)
print(s.computeArea(-2, -2, 2, 2, -2, -2, 2, 2), 16)
print(s.computeArea(0, 0, 0, 0, -1, -1, 1, 1), 4)