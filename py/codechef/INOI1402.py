# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/16 22:39

"""

C, F = map(int, input().split())

E = [[float('inf') for _ in range(C+1)] for _ in range(C+1)]
G = collections.defaultdict(list)
for i in range(F):
    u, v, w = map(int, input().split())
    E[u][v] = w
    E[v][u] = w
    G[u].append(v)
    G[v].append(u)

for i in range(1, C+1):
    E[i][i] = 0


for u in range(1, C+1):
    q = [(E[u][v], v) for v in G[u]]
    heapq.heapify(q)
    while q:
        dus, s = heapq.heappop(q)
        for t in G[s]:
            d = dus + E[s][t]
            if E[u][t] > d:
                E[u][t] = d
                heapq.heappush(q, (d, t))

ans = max([E[u][v] for u in range(1, C+1) for v in range(1, C+1) if E[u][v] < float('inf')])

print(ans)
