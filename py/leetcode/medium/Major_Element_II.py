# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 09:02

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.

Hint:

How many majority elements could it possibly have?
Do you have a better hint? Suggest it!
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        """
        每次去除3个不一样的数字，最后剩下的数字中一定包含出现次数超过1/3的数字。

        1. 假设出现次数超过1/3的数字是X，假设最后剩下的数字中不包含它，那么即使前面
        每次去掉的三个数字中都包含一个X，它出现的次数也只有N//3，与题意矛盾。

        2. 最后最多剩下2个数字， 再分别遍历一次
        :param nums:
        :return:
        """

        counts = collections.defaultdict(int)
        for v in nums:
            counts[v] += 1
            if len(counts.keys()) == 3:
                rmks = []
                for k in counts.keys():
                    counts[k] -= 1
                    if counts[k] == 0:
                        rmks.append(k)
                for k in rmks:
                    counts.pop(k)

        return list(filter(lambda x: nums.count(x) > len(nums) // 3, counts.keys()))


    def majorityElement2(self, nums):
        """
        Very fast, but not O(1) space
        :param nums:
        :return:
        """
        counts = collections.defaultdict(int)
        for v in nums:
            counts[v] += 1
        return list(filter(lambda x: counts[x] > len(nums) // 3, counts.keys()))


s = Solution()
print(s.majorityElement([]))
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([1, 2, 3, 2, 2, 2, 2, 4, 5, 6, 7, 8, 9, 10]))

print(s.majorityElement2([]))
print(s.majorityElement2([3, 2, 3]))
print(s.majorityElement2([1, 2, 3, 2, 2, 2, 2, 4, 5, 6, 7, 8, 9, 10]))