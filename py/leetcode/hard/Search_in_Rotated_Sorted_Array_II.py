# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-04 13:15

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        """

        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return False

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return True

            if nums[low] < nums[mid]:
                # mid在分割线的左边，low和mid之间的元素是递增的
                if nums[low] <= target <= nums[mid]:
                    # target位于low和mid之间
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] > nums[mid]:
                # mid位于分割线的右边，mid和high之间的元素是递增的
                if nums[mid] <= target <= nums[high]:
                    # target位于mid和high之间
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # 忽略相同的元素
                low += 1

                # 以下不会起到加速的作用
                # while low < high and nums[low] == nums[mid]:
                #     low += 1
                # while low < high and nums[high] == nums[mid]:
                #     high -= 1

        return False



s = Solution()
print(s.search([1], 0))
print(s.search(	[1, 3, 1, 1, 1], 3))
# nums = [4, 4, 4, 5, 6, 7, 0, 1, 2, 4]
# # print(s.search(nums, -1))
# for num in nums:
#     print(s.search(nums, num))
#
# print('')
# nums = [7, 8, 1, 2, 3, 4, 5, 6, 6]
# for num in nums:
#     print(s.search(nums, num))
