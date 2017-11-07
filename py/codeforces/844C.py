# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 10:12

"""

N = int(input())
A = [int(x) for x in input().split()]

B = [x for x in A]
B.sort()

ind = {v: i for i,v in enumerate(B)}

order = [ind[A[i]] for i in range(N)]

done = [0] * N
ans = []
for i in range(N):
    if not done[i]:
        g = []
        cur = i

        while not done[cur]:
            g.append(cur)
            done[cur] = 1
            cur = order[cur]
        ans.append([len(g)] + [j+1 for j in g])

print(len(ans))
for row in ans:
    print(' '.join(map(str, row)))