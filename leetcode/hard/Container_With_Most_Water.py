# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-04 08:49

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        """
        选择两条竖线隔板之后他们之间是没有隔板的。
        :param height:
        :return:
        """
        if not height:
            return 0

        # 还是需要用滑动窗口方法
        area, left, right, L = 0, 0, len(height) - 1, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                area = max(area, height[left] * L)
                left += 1
            else:
                area = max(area, height[right] * L)
                right -= 1
            L -= 1

        return area

        # 暴力O(N^2) 超时
        # res = 0
        # for i, j in itertools.combinations(range(len(height)), 2):
        #     # print(i, j)
        #     res = max(res, (j-i) * min(height[i], height[j]))
        # return res


        # 计算出每个位置的最高水位，然后以当前位置作为左边隔板，右边最后一个不小于当前水位
        # 的隔板作为右边隔板，计算出两个隔板之间能够装多少水
        #
        # 当高度是递增序列时候，退化为O(N^2)，因为以每个位置作为最左边的隔板时右边的隔板都是最后一个。
        # 此时超时
        # water = [0] * len(height)
        # wh = 0
        # for i, h in enumerate(height):
        #     wh = max(wh, h)
        #     water[i] = wh
        #
        # wh = 0
        # for i in range(len(height)-1, -1, -1):
        #     wh = max(wh, height[i])
        #     water[i] = min(water[i], wh)
        #
        # res = 0
        # for t in range(2):
        #     pre = 0
        #     while pre < len(water):
        #         nextPre = -1
        #         matched = False
        #         for i in range(pre+1, len(water)):
        #             if water[i] > water[pre]:
        #                 if nextPre < 0:
        #                     nextPre = i
        #             elif water[i] < water[pre]:
        #                 res = max(res, water[pre] * (i - pre - 1))
        #                 matched = True
        #                 break
        #         if not matched:
        #             res = max(res, water[pre] * (len(water) - pre - 1))
        #         if nextPre < 0:
        #             break
        #         pre = nextPre
        #     water = list(reversed(water))
        # return res


    def maxAreaWithWall(self, height):
        """
        每个位置i都有一条高度为heigh[i]的隔板
        :param height:
        :return:
        """
        if not height:
            return 0

        water = [0] * len(height)
        wh = 0
        for i, h in enumerate(height):
            wh = max(wh, h)
            water[i] = wh

        wh = 0
        for i in range(len(height)-1, -1, -1):
            wh = max(wh, height[i])
            water[i] = min(water[i], wh)

        res = 0
        # area = 0
        pre = 0
        wh = water[0]
        # print(water)
        for i in range(1, len(water)):
            h = water[i]
            if h != wh:
                if i - pre > 1:
                    res = max(res, (i-pre)*wh)
                else:
                    res = max(res, min(water[i], water[i-1]))
                wh = h
                pre = i

        res = max(res, (len(water)-1-pre)*wh)
        return res





s = Solution()
print(s.maxArea([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), s.maxArea([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 14)
print(s.maxArea([1, 1]), s.maxArea([1, 1]) == 1)
print(s.maxArea([1, 1, 3, 1, 2, 3]), s.maxArea([1, 1, 3, 1, 2, 3]) == 9)
print(s.maxArea([2, 1]), s.maxArea([2, 1]) == 1)
print(s.maxArea([2, 1, 1, 2, 1, 2]), s.maxArea([2, 1, 1, 2, 1, 2]) == 10)
print(s.maxArea([1]), s.maxArea([1]) == 0)
print(s.maxArea([2, 3]), s.maxArea([2, 3]) == 2)
print(s.maxArea([1, 2, 1]), s.maxArea([1, 2, 1]) == 2)
