# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/4 19:07

"""

N = int(input())

nums = []
for i in range(N):
    nums.append(input())

snums = set(nums)
if len(snums) > 2:
    print('NO')
else:
    lsnums = list(snums)
    if nums.count(lsnums[0]) == len(nums) // 2:
        print('YES')
        print(lsnums[0], lsnums[1])
    else:
        print('NO')

