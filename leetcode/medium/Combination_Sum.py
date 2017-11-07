# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:59


Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        nums = sorted(candidates)

        return self.impl(0, nums, target, [])


    def impl(self, index, nums, target, pres):
        if target == 0:
            return [pres]
        elif target < 0 or index >= len(nums):
            return []

        result = []
        for i in range(target//nums[index]+1):
            result.extend(self.impl(index+1, nums, target-nums[index]*i, pres+[nums[index]]*i))

        return result