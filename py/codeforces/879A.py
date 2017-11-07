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
created by shhuan at 2017/10/28 15:36

"""

N = int(input())

ans = 0
for i in range(N):
    s, d = map(int, input().split())
    if ans >= s:
        diff = ans-s
        k = diff//d + 1
        ans = s + k*d
    else:
        ans = s

print(ans)

