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
created by shhuan at 2017/10/28 15:51

"""

N, K = map(int, input().split())
P = [int(x) for x in input().split()]

if K >= N-1:
    print(max(P))
else:
    if P[0] > max(P[1: K+1]):
        print(P[0])
        exit(0)

    for i in range(1, N):
        if P[i] > max(P[:i] or [float('-inf')]):

            tail = []
            p = P[0]
            for j in range(1, i):
                tail.append(min(p, P[j]))
                p = max(p, P[j])
            tail.append(p)

            tail = P[i+1: ] + tail
            if P[i] > max(tail[:K-1]):
                print(P[i])
                exit(0)

