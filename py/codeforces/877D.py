
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
created by shhuan at 2017/10/30 16:51

"""


# N, M, K = map(int, input().split())
#
# R = []
# for i in range(N):
#     R.append([0 if x == '#' else 1 for x in list(input())])
#
# x1, y1, x2, y2 = map(int, input().split())


N, M, K = 1000, 1000, 1000
R = []
for i in range(N):
    R.append([1 for _ in range(M)])

x1, y1, x2, y2 = random.randint(1, M+1), random.randint(1, N+1), random.randint(1, M+1), random.randint(1, N+1),
#
t0 = time.time()

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

q = collections.deque()
q.append((x1, y1))

vis = [[0 for _ in range(M)] for _ in range(N)]
vis[x1][y1] = 1

novisrow = {}
noviscol = {}

for r in range(N):
    novisrow[r] = {c for c in range(M) if R[r][c]}
for c in range(M):
    noviscol[c] = {r for r in range(N) if R[r][c]}


while q:
    if vis[x2][y2] > 0:
        print(vis[x2][y2]-1)
        print(time.time() - t0)
        exit(0)

    x, y = q.popleft()

    visrow = set()
    if y-1 in novisrow[x]:
        for c in sorted([c for c in novisrow[x] if 0 < y-c <= K], reverse=True):
            if not R[x][c]:
                break
            if vis[x][c] == 0:
                vis[x][c] = vis[x][y] + 1
                q.append((x, c))
                visrow.add(c)
    if y+1 in novisrow[x]:
        for c in sorted([c for c in novisrow[x] if 0 < c-y <= K]):
            if not R[x][c]:
                break
            if vis[x][c] == 0:
                vis[x][c] = vis[x][y] + 1
                q.append((x, c))
                visrow.add(c)
    novisrow[x] -= visrow

    viscol = set()
    if x-1 in noviscol[y]:
        for r in sorted([r for r in noviscol[y] if 0<=x-r<=K], reverse=True):
            if not R[r][y]:
                break
            if vis[r][y] == 0:
                vis[r][y] = vis[x][y] + 1
                q.append((r, y))
                viscol.add(r)
    if x+1 in noviscol[y]:
        for r in sorted([r for r in noviscol[y] if 0<=r-x<=K]):
            if not R[r][y]:
                break
            if vis[r][y] == 0:
                vis[r][y] = vis[x][y] + 1
                q.append((r, y))
                viscol.add(r)
    noviscol[y] -= viscol

print(-1)