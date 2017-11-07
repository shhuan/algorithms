# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/17 13:09

"""

# A = [int(x) for x in input().split()]
# N, K = A[0], A[1]
# V = A[2: 2+N]
# B = A[2+N:]
INF = float('-inf')

N, K = 400, 7
V = [random.randint(-10**6, 10**6) for _ in range(N)]
B = [random.randint(1, 2*K) for _ in range(N)]
# V = [-7, 10, 3, -7, 0, -7]
# B = [4, 2, 2, 1, 2, 5]


def inf2Zero(val):
    return val if val != INF else 0


memo = {}
def dfs(start, end):
    if end - start < 2:
        return 0

    key = (start, end)
    if key in memo:
        return memo[key]

    if B[start] > K:
        ans = dfs(start+1, end)
        memo[key] = ans
        return ans
    if B[end-1] <= K:
        ans = dfs(start, end-1)
        memo[key] = ans
        return ans

    ans = INF
    for i in range(start, end):
        if B[i] <= K:
            x = 0
            for j in range(i+1, end):
                if B[j] == B[i] + K:
                    ans = max(ans, V[i] + V[j] + dfs(i+1, j) + dfs(j+1, end))

    # print(start, end, ans)
    ans = ans if ans != INF else 0
    memo[key] = ans
    return ans

t0 = time.time()
print(dfs(0, N))
print(time.time() - t0)

