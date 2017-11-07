# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import random
import time

"""
created by shhuan at 2017/10/3 09:58

"""


N = int(input())
S = input()

tos = 0
tof = 0
for i in range(1, N):
    if S[i] == 'S' and S[i-1] == 'F':
        tos += 1
    elif S[i] == 'F' and S[i-1] == 'S':
        tof += 1

if tof > tos:
    print('YES')
else:
    print('NO')