# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 15:10


Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        MAX_LEN = 10000000
        ret = MAX_LEN
        l = 0
        r = 0
        count = 0
        while r < len(nums):
            count += nums[r]
            if count >= s:
                while count - nums[l] >= s and l < r:
                    count -= nums[l]
                    l += 1
                ret = min(ret, r - l + 1)
                if ret == 1:
                    return 1
            r += 1
        return 0 if ret == MAX_LEN else ret


s = Solution()
print(s.minSubArrayLen(7, [2, 7, 1, 2, 4, 3]))
print(s.minSubArrayLen(3, [1, 1]))