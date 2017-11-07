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
created by shhuan at 2017/10/21 13:33

"""

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A = sorted([(x, i) for i,x in enumerate(A)], reverse=True)
B = sorted([(x, i) for i,x in enumerate(B)])

ans = [0] * N
for i in range(N):
    a, ia = A[i]
    b, ib = B[i]
    ans[ib] = a

print(' '.join(map(str, ans)))