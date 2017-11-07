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
created by shhuan at 2017/10/19 13:58

"""

# N, K = map(int, input().split())
# A = [int(x) for x in input().split()]

N, K = 300000, random.randint(100000, 300000)
A = [random.randint(10**5, 10**7) for _ in range(N)]

t0 = time.time()

q = [(-A[i], i+1) for i in range(min(N, K+1))]
heapq.heapify(q)

D = [0] * N
cost = 0
K += 1
while q:
    c, i = heapq.heappop(q)
    D[i-1] = K
    cost -= (K-i) * c
    if K < N:
        heapq.heappush(q, (-A[K], K+1))
    K += 1

print(cost)
print(" ".join(map(str, D)))

sys.stdout.flush()

print(time.time() - t0)