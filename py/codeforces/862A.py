# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/11 22:00

"""

n, x = map(int, input().split())

e = [0] * 101

for v in [int(x) for x in input().split()]:
    e[v] = 1

ans = 0
for i in range(x):
    ans += e[i] == 0
ans += e[x] == 1

print(ans)