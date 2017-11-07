
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
created by shhuan at 2017/10/28 16:08

"""

N = int(input())


M = 1024
ys = [i for i in range(M)]

for i in range(N):
    o, v = input().split()
    v = int(v)
    if o == '&':
        for j in range(M):
            ys[j] &= v
    elif o == '|':
        for j in range(M):
            ys[j] |= v
    else:
        for j in range(M):
            ys[j] ^= v


def transform(ops, x):
    for op, v in ops:
        if op == '&':
            x &= v
        elif op == '|':
            x |= v
        else:
            x ^= v

    return x



def dfs(ops):
    if len(ops) > 5:
        return None

    if len(ops) == 5:
        vals = [0 for _ in range(5)]
        lastbit = [0 for _ in range(5)]
        for i in range(32):
            for j in range(32):
                lastbit[j%5] ^= 1

                for k in range(M):
                    valid = True
                    if transform(zip(ops, lastbit), k) & 1 != ys[k] & 1:
                        valid = False
                        break
                if valid:
                    for k in range(5):
                        vals[k] <<= 1
                        vals[k] |= lastbit[k]
                    break

        return zip(ops, vals)

    for op in ['&', '|', '^']:
            res = dfs(ops+[op])
            if res:
                return res

    return None

ans = list(dfs([]))

if ans:
    print(len(ans))
    for op, v in ans:
        print(op, v)
else:
    print(0)
