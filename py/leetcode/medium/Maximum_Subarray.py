# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:01

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.

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
    def maxSubArray(self, nums):
        if not nums:
            return 0
        if len(nums) <= 1:
            return nums[0]

        ret = -1000000
        subsum = 0
        for num in nums:
            subsum += num
            ret = max(ret, subsum)
            if subsum <= 0:
                subsum = 0
        return max(ret, subsum) if subsum > 0 else ret