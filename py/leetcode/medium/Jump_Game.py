# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:00


Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

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
    # @return {boolean}
    def canJump(self, nums):
        if not nums or len(nums) <= 1:
            return True

        right = nums[0]
        left = 0
        while left < right:
            if right >= len(nums)-1:
                return True
            nr = right
            for i in range(left, right+1):
                nr = max(nr, i+nums[i])
            left = right
            right = nr
        return False