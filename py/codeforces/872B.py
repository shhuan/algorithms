# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 08:25

"""

N, K = map(int, input().split())
A = [int(x) for x in input().split()]

if K == 1:
    print(min(A))
elif K >= 3:
    print(max(A))
else:
    left = [float('inf')] * (N+1)
    for i in range(1, N+1):
        left[i] = min(left[i-1], A[i-1])

    right = [float('inf')] * (N+1)
    for i in range(N-1, -1, -1):
        right[i] = min(right[i+1], A[i])

    ans = float('-inf')
    for i in range(1, N):
        ans = max(ans, max(left[i], right[i]))

    print(ans)
