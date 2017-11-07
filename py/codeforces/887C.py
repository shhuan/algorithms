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
created by shhuan at 2017/11/4 00:22

"""

A = [0] + [int(x) for x in input().split()]

cc = collections.Counter(A[1:])
if any([x != 4 for x in cc.values()]):
    print("NO")
    exit(0)

goodFace = []
for i in range(6):
    s = i*4+1
    if all([A[j] == A[s] for j in range(s, s+4)]):
        goodFace.append(i)

if len(goodFace) != 2:
    print("NO")
    exit(0)

gfd = "".join(map(str, goodFace))
if gfd not in {"02", "34", "15"}:
    print("NO")
    exit(0)

f1, f2 = [], []
if gfd == "02":
    f1 = [A[i] for i in [13, 14, 5, 6, 17, 18, 21, 22]]
    f2 = [A[i] for i in [15, 16, 7, 8, 19, 20, 23, 24]]
elif gfd == "34":
    f1 = [A[i] for i in [1, 3, 5, 7, 9, 11, 22, 24]]
    f2 = [A[i] for i in [2, 4, 6, 8, 10, 12, 21, 23]]
else:
    f1 = [A[i] for i in [3, 4, 17, 19, 10, 9, 16, 14]]
    f2 = [A[i] for i in [1, 2, 18, 20, 12, 11, 15, 13]]

for i in range(4):
    if i != 2 and f1 == f2:
        print("YES")
        exit(0)
    f1 = f1[-2:]+f1[:-2]

print("NO")