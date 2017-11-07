# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/11 22:08

"""

N = int(input())

s, t = set(), set()

edges = collections.defaultdict(list)
for i in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
    # edges.add((v, u))

s.add(1)
q = [1]
while q:
    s, t = t, s
    p = []
    for u in q:
        for v in edges[u]:
            if v not in s:
                s.add(v)
                p.append(v)
    q = p

# print(s, t)

ns = len(s)
nt = len(t)

print(ns * nt - (N-1))
