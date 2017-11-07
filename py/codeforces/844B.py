# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 09:55

"""

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append([int(x) for x in input().split()])

ans = 0

for row in A:
    a = row.count(0)
    b = M-a
    ans += 2**a-1
    ans += 2**b-1

for col in [[A[r][c] for r in range(N)] for c in range(M)]:
    a = col.count(0)
    b = N-a
    ans += 2**a-1
    ans += 2**b-1

print(ans - M*N)