# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 08:46

"""

N = int(input())
A = [int(x) for x in input().split()]


ks = collections.defaultdict(int)

found = False
for i in range(N):
    if found or i > 1:
        break
    for j in range(i+1, N):
        k = (A[j]-A[i])/(j-i)
        ks[k] += 1
        if ks[k] > 1:
            found = True
            break

K = [(k, v) for k,v in ks.items() if v == max(ks.values())][0][0]

vis = [0] * N
vis[0] = 1

for i in range(1, N):
    if (A[i]-A[0])/i == K:
        vis[i] = 1

b = 0
for i in range(N):
    if vis[i] == 0:
        b = i
        break

if b == 0:
    print('No')
else:
    vis[b] = 2
    for i in range(b+1, N):
        if (A[i]-A[b])/(i-b) == K:
            vis[i] = 2
    c1 = vis.count(1)
    c2 = vis.count(2)
    if c1 > 0 and c2 > 0 and c1+c2==N:
        print('Yes')
    else:
        print('No')
