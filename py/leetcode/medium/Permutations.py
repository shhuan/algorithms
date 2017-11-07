# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:02

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

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
    def permute(self, num):
        if not num:
            return []

        return self.impl(0, num)


    def impl(self, index, nums):
        if index >= len(nums)-1:
            return [copy.deepcopy(nums)]

        ret = []
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            ret.extend(self.impl(index+1, nums))
            nums[index], nums[i] = nums[i], nums[index]

        return ret