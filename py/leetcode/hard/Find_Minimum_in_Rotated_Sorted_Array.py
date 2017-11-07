# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 13:53


Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

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
    def findMin(self, nums):

        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums)-1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]

            m = l + (r-l)//2
            if m == l:
                return min(nums[m], nums[m+1])
            elif nums[m] < nums[l]:
                # m在分割线的右边，最小值在左边，m也可能是
                r = m
            else:
                l = m

        return -1




s = Solution()
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([0]))
print(s.findMin([1, 2, 3, 4, 5]))
print(s.findMin([2, 1]))
print(s.findMin([1, 2, 3, 0]))
print(s.findMin([3, 1, 2]))
