
# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/4 22:05


Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return 0

        xor = 0
        for v in nums:
            xor ^= v

        b = 1
        while xor & 1 == 0:
            xor >>= 1
            b <<= 1

        nums1 = []
        nums2 = []
        for v in nums:
            if v & b == 0:
                nums1.append(v)
            else:
                nums2.append(v)

        num1, num2 = 0, 0
        for v in nums1:
            num1 ^= v
        for v in nums2:
            num2 ^= v

        return num1, num2


s = Solution()
print(s.singleNumber([1, 2, 1, 3, 2, 5]))