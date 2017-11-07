# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 11:44

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that
he will not get too much attention. This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, the security system for
these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # 选定一个房子不偷， 其他房子就和House Robber I的情形一样了
        ret = 0
        for i in range(len(nums)):
            ret = max(ret, self.robI(nums[i + 1:] + nums[:i]))

        return ret


    def robI(self, num):
        i = 0
        e = 0
        for v in num:
            tmp = i
            i = e + v
            e = max(tmp, e)
        return max(i, e)


s = Solution()

print(s.rob([2, 1, 1, 2]), 3)

print(s.rob([1, 4, 7, 5]))

print(s.rob([1, 4, 7]))

print(s.rob([1, 4]))

print(s.rob([7]))

print(s.rob([1, 4, 7, 3, 2, 5, 6]))