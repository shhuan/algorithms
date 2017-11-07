# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/4 19:27

"""


N = int(input())
S = input()


lowerStrs = []
lstr = ''
for i,v in enumerate(S):
    if ord('a') <= ord(v) <= ord('z'):
        lstr += v
    else:
        if lstr:
            lowerStrs.append(lstr)
        lstr = ''
if lstr:
    lowerStrs.append(lstr)

res = 0
for lstr in lowerStrs:
    res = max(res, len(set(lstr)))

print(res)
