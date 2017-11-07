# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/4 19:43

"""

a, b, f, k = map(int, input().split())

if b < f or f+b < a:
    print(-1)
    exit(0)

r = a-f

res = 0
fuel = b
for i in range(k):
    if i % 2 == 0:
        # 0->a
        if i == k-1:
            if fuel >= a:
                break
            elif fuel >= f:
                res += 1
                break
            else:
                print(-1)
                exit(0)
        else:
            if fuel < f:
                print(-1)
                exit(0)
            if fuel >= a + r:
                fuel -= a
            else:
                res += 1
                fuel = b - r
    else:
        # a->0
        if i == k-1:
            if fuel < r:
                print(-1)
                exit(0)
            if fuel >= a:
                break
            elif fuel >= r:
                res += 1
                break
            else:
                print(-1)
                exit(0)
        else:
            if fuel >= a + f:
                fuel -= a
            else:
                res += 1
                fuel = b - f
print(res)