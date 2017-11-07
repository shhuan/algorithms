# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/5 19:26

"""

# N = int(input())
# A = [int(x) for x in input().split()]

N = 100000
A = [random.randint(1, 10**5) for i in range(N)]

t0 = time.time()
MAXN = 100005
steps = collections.defaultdict(int)
count = collections.defaultdict(int)
for i,x in enumerate(A):
    c = 0
    while x > 0:
        y = x
        cc = c

        while y < MAXN:
            if count[y]==i:
                steps[y] += cc
                count[y] += 1
            y <<= 1
            cc += 1
        x >>= 1
        c += 1

print(min([steps[i] for i in steps.keys() if count[i] == N]))

print(time.time()-t0)