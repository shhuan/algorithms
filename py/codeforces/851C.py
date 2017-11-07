# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 17:35

"""
N = int(input())
P = []
for i in range(N):
    P.append([int(x) for x in input().split()])


def length(a):
    return math.sqrt(sum([x**2 for x in a]))

def angle(a, b):
    c = sum(a[i]*b[i] for i in range(len(a)))
    la = length(a)
    lb = length(b)
    if la and lb:
        return math.acos(c/la/lb)
    return -1

def cos(a, b, c):

    x = [b[i]-a[i] for i in range(len(a))]
    y = [c[i]-a[i] for i in range(len(a))]

    c = sum(x[i] * y[i] for i in range(len(x)))

    return c

ans = []
for i in range(N):
    bad = False
    for j in range(N):
        if bad:
            break
        if i != j:
            for k in range(N):
                if k != i and k != j:
                    if cos(P[i], P[j], P[k]) > 0:
                        bad = True
                        break
    if not bad:
        ans.append(i+1)
print(len(ans))
if ans:
    print(' '.join(map(str, ans)))