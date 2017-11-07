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
created by shhuan at 2017/10/20 11:12

"""


N, X, S = map(int, input().split())

print("?", X)
V, ni = map(int, input().split())

q = {random.randint(1, N) for _ in range(min(N, 999))}

if N > 1000:
    while len(q) < 999:
        q.add(random.randint(1, N))

for i in q:
    print('?', i)
    sys.stdout.flush()
    a, b = map(int, input().split())

    if V < a <= S:
        V = a
        ni = b

while V < S and ni > 0:
    print("?", ni)
    sys.stdout.flush()
    a, b = map(int, input().split())

    V = a
    ni = b

if V >= S:
    print("!", V)
else:
    print("!", -1)