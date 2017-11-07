# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/4 01:08

"""



n, a, b, c, d, start, l = map(int, input().split())

A = []
for i in range(n):
    A.append([int(x) for x in input().split()])


sm = [0] * (n+1)
ps = [0] * (n+1)
fs = [0] * (n+1)
sm[0] = start
X = 0
for i in range(1, n+1):
    if A[i-1][1] == 1:
        sm[i] = sm[i-1] + a
        ps[i] = ps[i-1] + 1
        fs[i] = fs[i-1]
    else:
        sm[i] = sm[i-1] - b
        ps[i] = ps[i-1]
        fs[i] = fs[i-1] + 1
    X = min(X, sm[i])

ts = [x[0] for x in A]

if X >= 0:
    print(ts[-1] + 1)
    exit(0)


for si, s in enumerate(ts):
    # update timerange [ti, ti+l)

    ti = bisect.bisect_left(ts, s+l)
    ti -= 1
    if 0 <= ti < n:
        t = ts[ti]
        if s <= t < s+l:
            p = ps[ti+1]-ps[si]
            f = fs[ti+1]-fs[si]
            diff = p*(c-a) + f*(b-d)
            if diff >= abs(X):
                print(s)
                exit(0)

print(-1)










