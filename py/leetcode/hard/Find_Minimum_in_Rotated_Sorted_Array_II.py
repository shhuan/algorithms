# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-03 18:54

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {integer[]} nums
    # @return {integer}
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
            elif nums[m] > nums[l]:
                # m在分割线的左边
                l = m
            else:
                # 忽略重复的值
                l += 1

        return -1


