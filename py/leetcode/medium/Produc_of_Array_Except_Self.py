# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/3 19:39

Given an array of n integers where n > 1, nums,
return an array output such that output[i] is
equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for the purpose of space complexity analysis.)

"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution(object):
    def productExceptSelf(self, nums):
        """
        不使用除法
        176ms, Your runtime beats 85.97% of python coders.

        使用了O(N)的空间，

        分别计算出前i项目的乘积，和后i项的乘积。
        在此基础上计算

        直接两边遍历实际上可以省掉两个数组
        184ms
        Your runtime beats 70.75% of python coders.
        :param nums:
        :return:
        """
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        N = len(nums)
        # frontProduct = [1] * (N + 1)
        # tailProduct = [1] * (N + 1)
        #
        # product = 1
        # for i, v in enumerate(nums):
        #     product *= v
        #     frontProduct[i + 1] = product
        #
        # product = 1
        # for i, v in enumerate(reversed(nums)):
        #     product *= v
        #     tailProduct[i + 1] = product
        #
        # result = [0] * N
        # for i in range(N):
        #     result[i] = frontProduct[i] * tailProduct[N - i - 1]
        #
        # return result

        result = [1] * N
        product = 1
        for i in range(N):
            result[i] = product
            product *= nums[i]
        product = 1
        for i in range(N-1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return result

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))