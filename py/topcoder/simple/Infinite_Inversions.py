
# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-07 12:56
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


N = int(input())

nums = {}

for n in range(N):
    i, j = map(int, input().split(' '))
    if i not in nums:
        nums[i] = i
    if j not in nums:
        nums[j] = j
    nums[i], nums[j] = nums[j], nums[i]


indices = sorted(nums.keys())

res = 0
for i, index in enumerate(indices):
    if nums[index] < index:
        res += index - nums[index]
        for j in range(i):
            preIndex = indices[j]
            if preIndex in range(nums[index], index) and nums[preIndex] <= nums[index]:
                res -= 1
            elif preIndex in range(nums[index]) and nums[preIndex] > nums[index]:
                res += 1
    elif nums[index] > index:
        res += nums[index] - index
        for j in range(i+1, len(indices)):
            preIndex = indices[j]
            if preIndex in range(index, nums[index]) and nums[preIndex] >= nums[index]:
                res -= 1
            elif nums[preIndex] < nums[index] < preIndex:
                res += 1

print(nums)

print(res)

