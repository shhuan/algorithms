# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 15:27

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import copy
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if not num:
            return []

        return self.impl(0, num)


    def impl(self, index, nums):
        if index >= len(nums)-1:
            return [copy.copy(nums)]

        ret = []
        for i in range(index, len(nums)):
            if self.canSwap(nums, index, i):
                nums[index], nums[i] = nums[i], nums[index]
                ret.extend(self.impl(index+1, nums))
                nums[index], nums[i] = nums[i], nums[index]

        return ret

    def canSwap(self, nums, i1, i2):
        """
        如果要交换nums[i1], nums[i2]，如果nums[i1]已经和nums[j]交换过了，就不应该再交换nums[i2]
        i1 <= j < i2 and nums[j] == nums[i2]

        :param nums:
        :param i1:
        :param i2:
        :return:
        """
        if i2 > i1:
            for i in range(i1, i2):
                if nums[i] == nums[i2]:
                    return False
        return True

s = Solution()
print(s.permuteUnique([1, 1, 2]))