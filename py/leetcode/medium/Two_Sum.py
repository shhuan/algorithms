# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 21:05



Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""
__author__ = 'huash'

import sys
import os
import collections


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
        # O(n)
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i+1]
            else:
                buff_dict[target - nums[i]] = i+1



s = Solution()
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([0,4,3,0], 0))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([-1,-2,-3,-4,-5], -8))
print(s.twoSum([2, 7, 11, 15], 9))