# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 20:48

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def maxProduct(self, nums):
        groupNums = []
        group = []
        maxMul = -100000000

        # 把数字从0隔开，分成多个组，计算每个组的最大乘积
        for num in nums:
            if num == 0:
                if group:
                    groupNums.append(group)
                    group = []
                maxMul = 0
            else:
                group.append(num)
        groupNums.append(group)

        for group in groupNums:
            maxMul = max(maxMul, self.maxProductInGroup(group))

        return maxMul

    def maxProductInGroup(self, group):
        if not group:
            return 0
        if len(group) == 1:
            return group[0]
        # print(group)

        negativeCount = 0
        firstNegative = -1
        lastNegative = -1

        for index, num in enumerate(group):
            if num < 0:
                negativeCount += 1
                if firstNegative < 0:
                    firstNegative = index
                    lastNegative = index
                else:
                    lastNegative = index
        mulLam = lambda x, y: x*y

        # 如果有偶数个负号，直接把所以得数字做乘法
        if negativeCount & 1 == 0:
            return reduce(mulLam, group)
        # 否则舍弃第一个负号左边的数字或者最后一个负号右边的数字
        else:
            l = reduce(mulLam, group[firstNegative+1:]) if firstNegative+1 < len(group) else 0
            r = reduce(mulLam, group[:lastNegative]) if lastNegative > 0 else 0
            return max(l, r)


s = Solution()
print(s.maxProduct([-2]))
print(s.maxProduct([-2, 0, -1]))
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([12]))
print(s.maxProduct([100, 12, 0, 2, 3, -5, 5, 6, -7, 8, 9, -6]))