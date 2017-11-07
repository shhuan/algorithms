# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 11:46

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import math
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        """
        假设数组nums的最终排列是a1, a2, a3, ... , an, a1是原始数组中的第几个数字呢？
        由于a2, a3, ..., an共有(n-1)!种排列，所以a1是原始数组中的第k/(n-1)!个数字。
        同理可以求出a2, a3, ... , an
        :param n:
        :param k:
        :return:
        """
        if n < 1:
            return ''
        if n == 1:
            return '1'

        nums = [_ for _ in range(1, n+1)]
        length = n
        result = ''
        fact = math.factorial(length)
        while length > 1:
            fact //= length
            index = (k-1)//fact
            num = nums[index]
            result += str(num)
            # 需要把用过的数字移出去
            nums.remove(num)
            length -= 1
            k -= index * fact
        result += str(nums[0])
        return result

s = Solution()
for i in range(1, 7):
    print(s.getPermutation(3, i))
