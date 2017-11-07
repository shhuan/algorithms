# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:02


Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]

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
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []

        counts = collections.defaultdict(int)
        for v in candidates:
            counts[v] += 1
        nums = sorted(list(set(candidates)))
        return self.impl(0, nums, counts, target, [])

    def impl(self, index, nums, counts, target, pres):
        if target == 0:
            return [pres]
        elif target < 0 or index >= len(nums) or nums[index] > target:
            return []

        result = []
        for i in range(min(target//nums[index]+1, counts[nums[index]]+1)):
            result.extend(self.impl(index+1, nums, counts, target-nums[index]*i, pres+[nums[index]]*i))

        return result