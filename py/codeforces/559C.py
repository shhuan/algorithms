# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/7 17:36

"""

h, w, n = map(int, input().split())

A = []
for i in range(n):
    r, c = map(int, input().split())
    A.append((r, c))

A.sort()
A.append((n, n))

N = len(A)
D = [0] * N

def cmb(a, b):
    if b == 0:
        return 0
    if b > a//2:
        b = a-b

    ans = 1
    for i in range(a, a-b, -1):
        ans *= i
        ans %= 10**9+7
    d = 1
    for i in range(1,b):
        d *= i
        d %= 10**9+7

    print(a, b, ans//d)
    return ans//d


for i in range(N):
    r, c = A[i]
    d = cmb(r+c-2, r-1)
    for j in range(i):
        pr, pc = A[j]
        d -= D[j] * cmb(r+c-pr-pc, r-pr)
    D[i] = d
print(D)
print(D[-1])