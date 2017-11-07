# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/17 05:15

"""


N, K = map(int, input().split())
A = [int(x) for x in input().split()]

if N == 1:
    print(0)
else:
    K -= 1

    f = [float('-inf') for _ in range(N)]  # f[i] means jump from i -> 0 backwards
    g = [float('-inf') for _ in range(N)]  # f[i] means jump from k->i forwards

    f[0] = 0
    f[1] = A[0]
    for i in range(2, N):
        f[i] = max(f[i - 1] + A[i - 1], f[i - 2] + A[i - 2])

    g[K] = 0
    if K+1 < N:
        g[K + 1] = A[K + 1]
        for i in range(K + 2, N):
            g[i] = max(g[i - 2] + A[i], g[i - 1] + A[i])

    # jump forwards to i and backwards to 0
    ans = float('-inf')
    for i in range(K, N):
        ans = max(ans, g[i] + f[i])

    print(ans)



