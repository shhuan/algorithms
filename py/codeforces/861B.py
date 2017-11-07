# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 10:06

"""

N, M = map(int, input().split())

A = []
for i in range(M):
    A.append([int(x) for x in input().split()])

flats = [] # even each floor has multiple possible flats, the answer may be deterministic
for k in range(1, 10005):
    valid = True
    for a, b in A:
        f = a//k if a%k==0 else a//k+1
        if f != b:
            valid = False
            break

    if valid:
        flats.append(k)
if flats:
    flats = [N//v if N%v==0 else N//v+1 for v in flats]
    if all([x==flats[0] for x in flats]):
        print(flats[0])
    else:
        print(-1)
else:
    print(-1)


