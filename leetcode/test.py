# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/15 22:16

"""

M = [[0 for _ in range(4)] for _ in range(5)]
M[0][1] = 1

T = 0
def dfs(s, p):
    if len(p) == 19:
        print(p)
        global T
        T += 1
        return len(p)

    ans = len(p)
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in ds:
        r, c = s[0]+d[0], s[1]+d[1]
        if 0 <= r < len(M) and 0 <= c < len(M[0]) and not M[r][c]:
            M[r][c] = 1
            x = dfs((r, c), p + [(r, c)])
            ans = max(ans, x)
            M[r][c] = 0

    return ans

for r in range(len(M)):
    for c in range(len(M[0])):
        if M[r][c] != 1:
            print(dfs((r, c), []))
print(T)
