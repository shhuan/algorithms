# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/16 13:09

"""


innerdist = []

def init_inner_dist(cycles):
    global innerdist
    for i, cycle in enumerate(cycles):
        n = len(cycle) + 1
        s = [0] * len(n)
        for i in range(1, n):
            s[i] = s[i - 1] + cycle[i - 1]
            innerdist[i] = s

def inner(i , s, t):
    global innerdist

    dist = innerdist[i]

    if s <= t:
        return dist[t] - dist[i]
    else:

        return dist[-1] - dist[s] + dist[t]

outerdist = []

def init_outer_dist(edges):
    global outerdist

    n = len(edges) + 1
    outerdist = [0] * n
    outerdist[1] = edges[0][2]
    for i in range(2, n):
        s, t, w = edges[i-1]
        outerdist[i] = outerdist[i-1] + inner(i-1, edges[i-2][1], s) + w

def out_dist_right(c1, c2, edges):
    n = len(edges)
    outerdist[c2] - outerdist[c1] + inner(c1, edges[(c1-1+n) % n][1], edges[c1][0])

def out_dist_left(c1, c2):
    pass





# T = int(input())
T = 5
MAXN = 10**4
for ti in range(T):
    # N, Q = map(int, input().split())
    N, Q = MAXN, MAXN
    cycles = []
    outer = {}
    for i in range(N):
        # s = list(map(int, input().split()))
        a = random.randint(2, MAXN)
        s = [a] + [random.randint(1, MAXN) for _ in range(a)]
        cycles.append(s[1:])

    init_inner_dist(cycles)




    for i in range(N):
        # v1, v2, w = map(int, input().split())
        v1 = random.randint(1, len(cycles[i]))
        v2 = random.randint(1, len(cycles[(i+1)%N]))
        w = random.randint(1, 10**3)
        v1 -= 1
        v2 -= 1
        outer[(i, (i+1)%N)] = v1, v2, w
        outer[((i+1)%N, i)] = v2, v1, w

    init_outer_dist()

    print("starting")

    outermemo = {}
    for qi in range(Q):
        t0 = time.time()
        # v1, c1, v2, c2 = [int(v)-1 for v in input().split()]
        c1 = random.randint(0, N-1)
        c2 = random.randint(0, N-1)
        v1 = random.randint(0, len(cycles[c1])-1)
        v2 = random.randint(0, len(cycles[c2])-1)

        v1b, c1b, v2b, c2b = v1, c1, v2, c2
        s1, t1, w1 = outer[(c1, (c1+1)%N)]
        s2, t2, w2 = outer[((c2-1+N)%N, c2)]
        k1 = (c1, s1, c2, t2)
        d1 = inner(c1, v1, s1)
        if k1 in outermemo:
            d1 += outermemo[k1]
        else:
            d = 0
            while c1 != c2:
                s, t, w = outer[(c1, (c1+1)%N)]
                d += inner(c1, s1, s)
                d += w
                c1 = (c1+1)%N
                s1 = t
            outermemo[k1] = d
            d1 += d
        d1 += inner(c2, t2, v2)

        v1, c1, v2, c2 = v1b, c1b, v2b, c2b
        s1, t1, w1 = outer[(c1, (c1-1+N)%N)]
        s2, t2, w2 = outer[((c2+1)%N, c2)]
        k2 = (c1, s1, c2, t2)
        d2 = inner(c1, v1, s1)
        if k2 in outermemo:
            d2 += outermemo[k2]
        else:
            d = 0
            while c1 != c2:
                s, t, w = outer[(c1, (c1-1+N)%N)]
                d += inner(c1, s1, s)
                d += w
                c1 = (c1-1)%N
                s1 = t
            outermemo[k2] = d
            d2 += d
        d2 += inner(c2, t2, v2)

        print(min(d1, d2))
        print(time.time() - t0)
        t0 = time.time()






