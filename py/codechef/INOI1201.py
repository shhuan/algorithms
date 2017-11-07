# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/16 23:21

"""

N = int(input())

A = []
for i in range(N):
    a, b, c = map(int, input().split())
    A.append((b+c, a))

A.sort(reverse=True)

ans = 0
w = 0
for i in range(N):
    ans = max(ans, w+sum(A[i]))
    w += A[i][1]

print(ans)