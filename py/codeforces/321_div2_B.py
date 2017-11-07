# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-15 09:02

定义字符串的beauty为字符重复出现的次数的最大值。
给定一个字符串，在不减少beauty的条件下找出其中最短的字串。

Sample test(s)
    input
        5 #字符个数
        1 1 2 2 1
    output
        1 5

    input
        5
        1 2 2 3 1
    output
        2 3

    input
        6
        1 2 2 1 1 2
    output
        1 5

分析：
找出每个字符出现的位置的极左值和极右值[Li, Ri]，保证有一个出现次数最多的字符i的范围[Li, Ri]取到就行


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
        # caution!!!, forget this line in contest
        right[num] = i
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
