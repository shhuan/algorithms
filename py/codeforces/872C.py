# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 08:33

"""

Q = int(input())

for i in range(Q):
    N = int(input())

    ds = {4, 6, 9, 15}

    ans = -1
    for d in ds:
        if N >= d and (N-d) % 4 == 0:
            if d == 15:
                ans = (N-d)//4+2
            else:
                ans =(N-d)//4+1
                break
    print(ans)