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
created by shhuan at 2017/10/20 15:34

"""

R, D = map(int, input().split())

N = int(input())

ans = 0
for i in range(N):
    x, y, r = map(int, input().split())

    d = math.sqrt(x**2+y**2)
    if d-r >= R-D and d+r <= R:
        ans += 1


print(ans)