# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/17 06:34

"""

N = int(input())
A = [int(x) for x in input().split()]
# N = 200000
# A = [random.randint(1, 100000) for _ in range(N)]

A = [x+i+1 for i,x in enumerate(A)]

maxl = [(0, 0)] * (N+1)
maxr = [(0, 0)] * (N+1)

for i, v in enumerate(A):
    if v > maxl[i][0]:
        maxl[i+1] = (v, i)
    else:
        maxl[i+1] = maxl[i]
for i in range(N-1, -1, -1):
    v = A[i]
    if v > maxr[i+1][0]:
        maxr[i] = (v, i)
    else:
        maxr[i] = maxr[i+1]


ans = [max(A)]
m = A.index(ans[0])
d = 0
# A[k] += N, A[k+1] += 1, A[k+2] += 2, ...
# => A[k] += 1, ...
k = N-1
while k > 0:
    if k > m:
        ans += [ans[-1]+i for i in range(1, k-m+1)]
        d += k - m
        k = m
    elif k < m:
        ans += [ans[-1]+i for i in range(1, N-len(ans)+1)]
        break
    else:
        d += 1
        k -= 1

        # a = [x + d if i < N - d else x - (N - d) for i, x in enumerate(A)]
        # x = max(a)
        # m = a.index(x)

        vl, il = maxl[N-d]
        vr, ir = maxr[N-d]

        if vl+d > vr-(N-d):
            x = vl+d
            m = il
        else:
            x = vr-(N-d)
            m = ir

        ans.append(x)

print(' '.join(map(str, ans)))

