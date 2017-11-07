"""

created by huash06 at 2015-07-14

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools

N = int(input())
nums = [int(x) for x in input().split()]

count = collections.defaultdict(int)
left = {}
right = {}
for i, num in enumerate(nums):
    count[num] += 1
    if num not in left:
        left[num] = i
    else:
        right[num] = i

beauty = max(count.values())

res = len(nums)
l = 1
r = len(nums)
for v in filter(lambda x: count[x] == beauty, count.keys()):
    if right[v] - left[v] < res:
        res = right[v] - left[v] + 1
        l = left[v] + 1
        r = right[v] + 1

print(l, r)