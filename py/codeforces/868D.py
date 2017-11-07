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

N = int(input())
S = ['']
for i in range(N):
    S.append(input())

M = int(input())


def find(s, x, v):
    if s.find(x) < 0:
        return v

    return 0


X = {1: ['0', '1']}
for mi in range(M):
    a, b = map(int, input().split())
    s = S[a]+S[b]
    S.append(s)
    k = 0
    while True:
        k += 1
        x = []
        if k in X:
            x = X[k]
        else:
            x = X[k-1]
            x = [v + '0' for v in x] + [v + '1' for v in x]
            X[k] = x

        if any([s.find(v)<0 for v in x]):
            k -= 1
            break


    print(k)






