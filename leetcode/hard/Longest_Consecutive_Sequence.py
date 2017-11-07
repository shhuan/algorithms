# -*- coding: utf-8 -*-

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""
__author__ = 'huash'

import sys
import os
import collections
import math
import itertools

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = set(nums)
        maxLen = 0

        while nums:
            num = nums.pop()
            count = 1
            r = num + 1
            while r in nums:
                count += 1
                nums.remove(r)
                r += 1
            l = num - 1
            while l in nums:
                count += 1
                nums.remove(l)
                l -= 1
            maxLen = max(maxLen, count)
        return maxLen

s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))