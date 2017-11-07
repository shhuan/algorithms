# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/6 22:33

"""

N, M = map(int, input().split())

MAXN = 255 # ??
MOD = 1000000007

U = [0]*MAXN
V = [0]*MAXN

mp = {}
def get_id(x):
    if x not in mp:
        mp[x] = len(mp)

    return mp[x]

E = collections.defaultdict(list)
def add_edge(u, v):
    E[u].append(v)
    E[v].append(u)


def cal_size(u, n, d):
    t, c, res = u, 0, 0
    while t > 0:
        c += 1
        t >>= 1

    res = (1 << (d-c+1))-1
    t = c
    while t < d:
        t += 1
        u = (u << 1) | 1

    return res-max(min(u-n, 1<<(d-c)), 0)

num = [0] * MAXN
def pre_dp(u, f):
    for v in E[u]:
        if v != f:
            num[u] -= num[v]
            pre_dp(v, u)


vis = [0] * MAXN
def dfs(u, tot):
    tot = (tot + u) % MOD
    vis[u] = 1
    for v in E[u]:
        if not vis[v]:
            tor = (tot+dfs(v, tot)) % MOD
    vis[u] = 0

    return tot


d = 0
while (1 << d) <= N:
    d += 1

get_id(1)

for i in range(M):
    U[i], V[i] = map(int, input().split())
    t = U[i]
    while t > 0:
        get_id(t)
        t >>= 1
    t = V[i]
    while t > 0:
        get_id(t)
        t >>= 1

for u, id in mp.items():
    if u > 1:
        add_edge(get_id(u), get_id(u >> 1))
    num[id] = cal_size(u, N, d)

pre_dp(1, 0)
for i in range(M):
    add_edge(get_id(U[i]), get_id(V[i]))

res = 0

for i in range(1, len(mp)):
    tot = dfs(i, 0)
    res = (res+tot*num[i]) % MOD

print(res)
