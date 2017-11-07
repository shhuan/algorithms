# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 11:21

"""

N = int(input())
A = []
for i in range(N):
    A.append(input())
#
# N = 70000
# A = [str(random.randint(10**9, 10**10-1)) for _ in range(N)]
#
vis = set()
cad = {}
for k, a in enumerate(A):
    for s in [a[i:j] for i in range(9) for j in range(i+1, 10)]:
        if s in cad and cad[s] != k:
            cad.pop(s)
        if s not in vis:
            cad[s] = k
            vis.add(s)

f = {}
for k,v in cad.items():
    f[v] = k if v not in f or len(f[v]) > len(k) else f[v]

print('\n'.join([x[1] for x in sorted((k, v) for k,v in f.items())]))
