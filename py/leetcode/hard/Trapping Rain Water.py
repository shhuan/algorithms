# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-03 21:02

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if not height:
            return 0
        water = [0]*len(height)
        h = 0
        # 从左往右计算每个坑的最高水位
        for i in range(len(height)):
            if height[i] > h:
                h = height[i]
            water[i] = h
        h = 0
        # 从右往左计算每个坑的最高水位
        for i in range(len(height)-1, -1, -1):
            if height[i] > h:
                h = height[i]
            water[i] = min(water[i], h)

        res = 0
        # 累加每个坑的水量
        for i in range(len(height)):
            res += max(0, water[i] - height[i])

        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))