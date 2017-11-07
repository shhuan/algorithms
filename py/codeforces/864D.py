# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/4 20:06

"""

N = int(input())
M = [int(x) for x in input().split()]

# t0 = time.time()
#
# N = 200000
# M = [random.randint(1, N) for _ in range(N)]

S = [0 for i in range(N+1)]

for v in M:
    S[v] += 1

changes = sum([S[i] - 1 for i in range(N+1) if S[i] > 1] or [0])
if changes == 0:
    print(changes)
    print(' '.join([str(x) for x in M]))
    exit(0)

used = [0 for _ in range(N+1)]
miss = collections.deque(sorted([x for x in range(1, N+1) if S[x] == 0]))

for i in range(N):
    v = M[i]
    if used[v]:
        M[i] = miss.popleft()
    else:
        if S[v] > 1:
            if miss and miss[0] < v:
                M[i] = miss.popleft()
                S[v] -= 1
            else:
                used[v] = 1
print(changes)
print(' '.join([str(x) for x in M]))

# print(time.time() - t0)