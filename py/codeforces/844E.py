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
created by shhuan at 2017/10/20 14:23

"""

MAXN = 2000000+5
G = collections.defaultdict(list)


def addEdge(s, t):
    G[s].append(t)
    G[t].append(s)


N = 0
siz = [0] * MAXN


def predfs(v, fa):
    siz[v] = 1
    for u in G[v]:
        if u != fa:
            predfs(u, v)
            siz[v] += siz[u]


def fincent(v, fa):
    for u in G[v]:
        if u != fa and siz[u] > N//2:
            return fincent(u, v)
    return v

topo = []
def dfs(v, fa):
    global topo
    for u in G[v]:
        if u != fa:
            dfs(u, v)
    topo.append((v, fa))

ans = []
def genans(v, fa):
    global topo
    topo = []
    dfs(v, fa)
    topo.pop()

    iter = v
    for now in topo:
        ans.append((fa, iter, now[0]))
        ans.append((now[0], now[1], v))
        iter = now[0]

    ans.append((fa, iter, v))


N = int(input())
for i in range(N-1):
    s, t = map(int, input().split())
    addEdge(s, t)

predfs(1, -1)
cent = fincent(1, -1)
cent2 = 0
for u in G[cent]:
    if siz[u]*2 == N:
        cent2 = u

for u in G[cent]:
    if u != cent2:
        genans(u, cent)

if cent2:
    for u in G[cent2]:
        if u != cent:
            genans(u, cent2)

print(len(ans))
for row in ans:
    print(' '.join(map(str, row)))


print(siz[:N+1])