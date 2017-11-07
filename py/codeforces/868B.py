# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/5 15:00

"""

H, M, S, t1, t2 = map(int, input().split())

# 0 - 11.999999999

if M != 0 or S != 0:
    H += 0.1

M = M * 12 / 60
S = S * 12 / 60

t1b, t2b = t1, t2

over = False
while t1 != t2:
    if t1 < 12:
        if t1 < H < t1+1 or t1 < M < t1+1 or t1 < S < t1+1:
            over = True
            break
        if t1+1 == t2:
            break
        else:
            if t1+1 == H or t1+1 == M or t1+1 == S:
                over = True
                break
        t1 += 1
    else:
        t1 = 1
        if 12 < H < 13 or 0 < M < 1 or 0 < S < 1:
            over = True
            break
        if t1 == t2:
            break
        else:
            if H == 1 or M == 1 or S == 1:
                over = True
                break
if not over:
    print('YES')
else:
    t1, t2 = t1b, t2b
    over = False
    while t1 != t2:
        if t1 > 1:
            if t1 > H > t1-1 or t1 > M > t1-1 or t1 > S > t1-1:
                over = True
                break
            if t1-1 == t2:
                break
            else:
                if t1-1 == H or t1-1 == M or t1-1 == S:
                    over = True
                    break
            t1 -= 1
        else:
            t1 = 12
            if 12 < H < 13 or 0 < M < 1 or 0 < S < 1:
                over = True
                break
            if t1 == t2:
                break
            else:
                if H == 12 or M == 0 or S == 0:
                    over = True
                    break
    if not over:
        print('YES')
    else:
        print('NO')







