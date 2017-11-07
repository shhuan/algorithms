
# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/4 21:51

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).


值得注意的题目
"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        nums = [1]
        a, b, c = 0, 0, 0
        while len(nums) < n:
            next_val = min(nums[a] * 2, nums[b] * 3, nums[c] * 5)
            nums.append(next_val)
            # 三个if，而不能是elif 否则会出现重复的数字
            if next_val == nums[a] * 2:
                a += 1
            if next_val == nums[b] * 3:
                b += 1
            if next_val == nums[c] * 5:
                c += 1
        return nums[-1]

s = Solution()
for i in range(20):
    print(s.nthUglyNumber(i))