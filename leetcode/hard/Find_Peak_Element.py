# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:21

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        """
        和二叉查找一样，首先选取中间的元素，如果它比两边的元素大直接返回。
        如果它比左边的元素小，左边一定存在一个极大值。
        同理适用于右边的元素
        :param nums:
        :return:
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        l = 1
        r = len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m] < nums[m-1]:
                r = m
            else:
                l = m + 1
        return -1



s = Solution()
print(s.findPeakElement([1]))
print(s.findPeakElement([2, 1]))
print(s.findPeakElement([1, 2, 3, 2, 1]))
print(s.findPeakElement([1, 2, 1]))