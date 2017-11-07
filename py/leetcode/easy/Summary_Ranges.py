# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 13:45

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []

        ret = []
        l, r = 0, 1
        while r < len(nums):
            if nums[r] == nums[r - 1] + 1:
                r += 1
            else:
                ret.append(self.getRange(nums[l], nums[r - 1]))
                l = r
                r += 1
        ret.append(self.getRange(nums[l], nums[-1]))
        return ret


    def getRange(self, l, r):
        if l < r:
            return '{}->{}'.format(l, r)
        else:
            return '{}'.format(l)


s = Solution()
print(s.summaryRanges([0, 1, 2, 4, 5, 7]))