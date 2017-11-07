# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/6 09:03

"""


H, Q = map(int, input().split())


LL = [2**(i-1) for i in range(H+1)]
LR = [2**i-1 for i in range(H+1)]

M1 = []
M2 = []
for i in range(Q):
    i, l, r, a = map(int, input().split())
    ll = l * (2 ** (H - i))
    rl = (r + 1) * (2 ** (H - i)) - 1
    if a:
        if ll > rl:
            print("Game cheated!")
            exit(0)
        M1.append((ll, rl))
    else:
        if 2**(H-1) <= ll <= rl <= 2**H-1:
            M2.append((ll-rl, ll, rl))
# M1.sort()
# M2.sort(reverse=True)

L, R = 2**(H-1), 2**H-1
for ll, lr in M1:
    L = max(L, ll)
    R = min(R, lr)
if L > R:
    print("Game cheated!")
    exit(0)

M2.sort()
LR = {(L, R)}
for d, ll, lr in M2:
    # merge [L, R] and [1, ll-1]
    # merge [L, R] and [lr+1, 2**H-1]
    nextlr = set()
    for L, R in LR:
        if R < ll or L > lr:
            nextlr.add((L, R))
        if L <= ll-1 <= R:
            nextlr.add((L, ll-1))
        if L <= lr+1 <= R:
            nextlr.add((lr+1, R))
    LR = nextlr

LR = list(LR)
if len(LR) == 0:
    print("Game cheated!")
elif len(LR) == 1 and LR[0][0] == LR[0][1]:
    print(LR[0][0])
else:
    print("Data not sufficient!")