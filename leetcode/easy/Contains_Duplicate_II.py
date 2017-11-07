# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-07 16:10

Given an array of integers and an integer k, find out whether there there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if not nums:
            return False

        if k >= len(nums) - 1:
            return len(nums) != len(set(nums))

        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False


s = Solution()

print(s.containsNearbyDuplicate([1, 2, 3, 4, 2, 5, 6, 7], 2))
print(s.containsNearbyDuplicate([1, 2, 3, 4, 2, 5, 6, 7], 4))
print(s.containsNearbyDuplicate([1, 2, 3, 4, 2, 5, 6, 7], 3))
