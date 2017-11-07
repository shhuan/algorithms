# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/18 20:43

"""

# N = int(input())
# A = [int(x) for x in input().split()]
# N = 200000
# A = [random.randint(10**8, 10**9) for _ in range(N)]
A = [5, 2, 3, 6]
N = len(A)
t0 = time.time()


maxVal = [N] * N
v = 0
q = []
# use stack to get left most element that greater then A[i] on right side of i
for i in range(N):
    while q and A[i] > A[q[-1]]:
        maxVal[q[-1]] = i
        q.pop()
    q.append(i)


print(maxVal)
print(time.time() - t0)
i = 1
l = 0
ans = 0
while i < N:
    r = maxVal[i]
    if r >= N:
        i += 1
        continue

    a = l-1
    for j in range(i-1, max(-1, l-1), -1):
        if A[j] | A[r] > A[r]:
            a = j
            break

    ans += (a-l+1) * (N-i)
    l = i
    i = r


def solve():
    ans = 0
    pairs = []
    for i in range(N):
        for j in range(i+1, N):
            x = A[i]
            for k in range(i+1, j+1):
                x |= A[k]
            if x > max(A[i:j+1]):
                pairs.append((i, j))
                ans += 1
    print(ans, pairs)
    return ans
print(ans)
solve()


