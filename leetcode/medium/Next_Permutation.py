# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 21:45

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        """
        当前序列中，从尾端往前寻找两个相邻的元素，前一个记A[i]，后一个记为A[ii]，且A[i] < A[ii]。
        然后从尾端找另外一个元素A[j]，如果A[i] < A[j]， 则对调第i和第j个元素，并将A[ii:]颠倒顺序。
        :param num:
        :return:
        """
        if not num:
            return

        for ii in range(len(num)-1, 0, -1):
            i = ii - 1
            if num[i] < num[ii]:
                j = len(num) - 1
                while j >= 0 and num[i] >= num[j]:
                    j -= 1
                if j > 0:
                    num[i], num[j] = num[j], num[i]
                    num[ii:] = num[-1:ii-len(num)-1:-1]
                    return
        num[:] = num[-1:-len(num)-1:-1]


s = Solution()
nums = [1, 2, 3, 4]
s.nextPermutation(nums)
print(nums)

nums = [3, 2, 1]
s.nextPermutation(nums)
print(nums)

nums = [1, 1, 5]
s.nextPermutation(nums)
print(nums)


nums = [3, 2, 1]
s.nextPermutation(nums)
print(nums)
