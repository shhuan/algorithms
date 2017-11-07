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
created by shhuan at 2017/10/30 12:09

"""

N = int(input())

ans = []
for i in range(2, N+1, 2):
    ans.append(i)
for i in range(1, N+1, 2):
    ans.append(i)
for i in range(2, N+1, 2):
    ans.append(i)

print(len(ans))
print(' '.join(map(str, ans)))