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

N, K = map(int, input().split())

problems = []
for i in range(N):
    row = [int(x) for x in input().split()]
    k = sum(row)
    if k == 0:
        print('YES')
        exit(0)
    elif k < K:
        problems.append(row)

if not problems:
    print('NO')
    exit(0)

N = len(problems)
for i in range(N):
    for j in range(i+1, N):
        if all([(problems[i][x] + problems[j][x]) < 2 for x in range(K)]):
            print('YES')
            exit(0)
print('NO')

