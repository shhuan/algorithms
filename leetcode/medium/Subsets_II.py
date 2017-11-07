# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:45

Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if not S:
            return []

        wc = collections.defaultdict(int)
        for num in S:
            wc[num] += 1

        return self.impl(0, sorted(list(set(S))), wc, [])


    def impl(self, index, nums, words, pres):
        if index >= len(nums):
            return [pres]
        result = []
        for i in range(words[nums[index]]+1):
            cmb = self.impl(index+1, nums, words, pres+[nums[index]]*i)
            result.extend(cmb)
        return result
