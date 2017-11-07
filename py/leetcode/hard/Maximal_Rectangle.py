# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-03 17:53


Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.


"""
__author__ = 'huash'

import sys
import os



class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        """
        使用一个数组纪录以当前行每个位置的最高高度，然后使用之前的Largest_Rectangle_in_Histogram
        里面的算法计算最大面积，遍历完每一行之后即可得到最大面积
        :param matrix:
        :return:
        """

        if not matrix:
            return 0

        height = [0] * len(matrix[0])
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == '0':
                    height[c] = 0
                else:
                    height[c] += 1
            res = max(res, self.largestRectangleArea(height))

        return res



    def largestRectangleArea(self, height):
        if not height:
            return 0

        res = 0
        s = []
        for i in range(len(height)):
            if not s or height[s[-1]] <= height[i]:
                s.append(i)
            else:
                while s and height[s[-1]] > height[i]:
                    tp = s.pop()
                    area = height[tp] * (i if not s else i-s[-1]-1)
                    res = max(res, area)
                s.append(i)

        while s:
            tp = s.pop()
            area = height[tp] * (len(height) if not s else len(height)-s[-1]-1)
            res = max(res, area)

        return res




s = Solution()
m = [
    '1111',
    '1001',
    '1111',
    '0010',
    '0111'
]
print(s.maximalRectangle(m) == 4)

m = [
    '01010',
    '11111',
    '01110',
    '01110',
    '11111',
    '11110',
    '01010',
    '00000'
]
print(s.maximalRectangle(m) == 15)

m = ["01"]
print(s.maximalRectangle(m) == 1)