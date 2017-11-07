# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:05

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if not nums or len(nums) <= 1:
            return 0

        jumps = 1
        left = 0
        right = nums[0]
        while right < len(nums)-1:
            nextright = 0
            for i in range(left, right+1):
                nextright = max(nextright, i+nums[i])
            left = right
            right = nextright
            jumps += 1
        return jumps