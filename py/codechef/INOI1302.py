# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/17 05:04

"""

N, K = map(int, input().split())
residents = []
for i in range(N):
    residents.append([int(x) for x in input().split()][1:])

family = [0] * N
family[0] = 1

q = [0]
while q:
    a = q.pop()
    for b in range(1, N):
        if not family[b] and len(set(residents[a]) & set(residents[b])) >= K:
            family[b] = 1
            q.append(b)

print(sum(family))
