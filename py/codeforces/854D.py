# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 14:58

"""

N, M, K = map(int, input().split())

S = [[] for _ in range(N+1)]
T = [[] for _ in range(N+1)]

to0 = set()
for i in range(M):
    d, f, t, c= map(int, input().split())
    # A.append([d, f, t, c])
    to0.add(d)
    if f == 0: # 0->t
        S[t].append((d, c))
    else: # f->0
        T[f].append((d, c))

for v in S:
    v.sort()
for v in T:
    v.sort()

to0 = list(sorted(to0))
D = {d:i for i, d in enumerate(to0)}
RD = {i:d for i, d in enumerate(to0)}

for i in range(len(S)):
    S[i] = [(D[d], c) for d,c in S[i]]
for i in range(len(T)):
    T[i] = [(D[d], c) for d,c in T[i]]

left = [[float('inf') for _ in range(len(D))] for _ in range(N+1)]
for i in range(1, N+1):
    io = T[i]
    minc = float('inf')
    for d, c in io:
        minc = min(c, minc)
        left[i][d] = minc
    c = float('inf')
    for d in range(1, len(D)):
        if left[i][d] != float('inf'):
            c = left[i][d]
        left[i][d] = c

right = [[float('inf') for _ in range(D)] for _ in range(N+1)]
for i in range(1, N+1):
    oi = S[i]
    minc = float('inf')
    for j in range(len(oi)-1, -1, -1):
        d, c = oi[j]
        minc = min(minc, c)
        right[i][d] = minc
    c =  float('inf')
    for j in range(len(oi)-1, -1, -1):
        d, c = oi[j]
        if right[i][d] != float('inf'):
            c = right[i][d]
        right[i][d] = c

C = [[float('inf') for _ in range(len(D))] for _ in range(N+1)]

L, R = 0, len(D)
for i in range(1, N+1):
    io = T[i]
    oi = S[i]
    # cal

    l = -1
    r = -1
    for d1, c1 in io:
        c = float('inf')
        for d2, c2 in oi:
            if RD[d2]-RD[d1] > K:
                c = min(c, c1+c2)
        C[i][d1] = c
        if l < 0 and c != float('inf'):
            l = d1
        if c != float('inf'):
            r = d1

    L = max(L, l)
    R = min(R, r)

for row in C:
    print(row)
print("===========")
SC = [sum([row[j] for row in C]) for j in range(len(D))]
print(SC)
print(min(SC))





