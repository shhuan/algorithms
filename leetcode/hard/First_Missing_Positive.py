
# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 15:48

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import math

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        """
        分别计算1到n位数的个数
        :param nums:
        :return:
        """
        if not nums:
            return 1
        nums = list(filter(lambda x: x > 0, set(nums)))
        if not nums:
            return 1
        maxNum = max(nums)
        bits = int(math.log10(maxNum)) + 1
        for bit in range(1, bits+1):
            bitNums = list(filter(lambda x: 10**(bit-1) <= x < 10**bit, nums))
            if not bitNums:
                return 10**(bit-1)
            if len(bitNums) < 9*(10**(bit-1)):
                bitNums = sorted(bitNums)
                if bitNums[0] != 10**(bit-1):
                    return 10**(bit-1)
                i = 1
                while i < len(bitNums):
                    if bitNums[i] != bitNums[i-1]+1:
                        return bitNums[i-1]+1
                    i += 1
                return bitNums[i-1]+1
        return maxNum+1




# print(math.log10(3))
# print(math.log10(111))
# print(10**1)
# print(list(filter(lambda x: x<10**2, [0, 1, 2])))
s = Solution()
print(s.firstMissingPositive([0,2,2,1,1]))
print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([1000, -1]))
print(s.firstMissingPositive([1, 2, 3, 4, 10]))
print(s.firstMissingPositive([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]))
print(s.firstMissingPositive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13]))
print(s.firstMissingPositive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))