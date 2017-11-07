# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-03 18:19

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        l = 0
        r = len(nums)
        while l < r:
            if nums[l] < nums[r-1]:
                return self.binary_search(nums, l, r, target)
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] >= nums[l]:
                    if nums[r-1] < target:
                        r = mid
                    else:
                        l = mid + 1
                else:
                    r = mid
            else:
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    if nums[l] > target:
                        l = mid + 1
                    else:
                        r = mid

        return -1
    def binary_search(self, nums, start, end, tartget):
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == tartget:
                return mid
            elif nums[mid] > tartget:
                end = mid
            else:
                start = mid + 1
        return -1


    def search2(self, nums, target):
        """
        关键是确定出递增的没有分割线的一段
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                # mid在分割线的左边，low和mid之间的元素是递增的
                if nums[low] <= target <= nums[mid]:
                    # target位于low和mid之间
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # mid位于分割线的右边，mid和high之间的元素是递增的
                if nums[mid] <= target <= nums[high]:
                    # target位于mid和high之间
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


s = Solution()
print(s.search([], 1))


nums = [4, 5, 6, 7, 0, 1, 2]
print(s.search(nums, -1))
for num in nums:
    print(s.search(nums, num))

nums = [7, 8, 1, 2, 3, 4, 5, 6]
for num in nums:
    print(s.search(nums, num))
