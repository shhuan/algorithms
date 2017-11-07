# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 09:32

"""

N, K = map(int, input().split())

ans = float('inf')


for a in range(int(math.log(10**K, 2))+2):
    for b in range(100000):
        v = N * 2**a * 5**b
        if v > N * 10**K:
            break
        d = 0
        x = v
        while x % 10 == 0:
            d += 1
            x //= 10
        if d >= K:
            ans = min(ans, v)
print(ans)