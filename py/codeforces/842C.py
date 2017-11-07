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
created by shhuan at 2017/10/20 15:45

"""


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)


N = 2*10**5+5
vis = [0] * N
G = collections.defaultdict(list)
ans = [0] * N
mas = [0] * N


def dfs1(v):
    global vis
    global ans
    vis[v] = 1
    for u in G[v]:
        if not vis[u]:
            ans[u] = gcd(ans[v], mas[u])
            dfs1(u)


def dfs2(v, dist):
    vis[v] = 1
    for