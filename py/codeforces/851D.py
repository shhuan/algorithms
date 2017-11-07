# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 19:15

"""

N, X, Y = map(int, input().split())
A = [int(x) for x in input().split()]

A.sort()

def cnt(l, r):
    a = bisect.bisect_right(A, l)
    b = bisect.bisect_left(A, r)
    return b-a+1

left = [0] * (N+1)
for i in range(1, N+1):
    left[i] = left[i-1] + A[i-1]

def sum(l, r):
    print(l, r)
    return left[r] - left[l]


ans = float('inf')
maxa = max(A)
for g in range(2, maxa+1):
    cost = 0
    k = g
    for k in range(g, maxa+1, g):
        f = g - min(g, X//Y)
        cost += cnt(k-g+1, k-f)*X + (cnt(k-f+1, k)*k-sum(k-f+1, k))*Y
    ans = min(ans, cost)

print(ans)