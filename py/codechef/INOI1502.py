# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/17 11:06

"""

N, M = map(int, input().split())

# N = random.randint(10**7, 10**8)
# M = 10*9+7

d = collections.defaultdict(int)

n = N
while n > 1:
    k = False
    for i in range(2, n//2+1):
        if n % i == 0:
            d[i] += 1
            n = n//i
            k = True
            break
    if not k:
        d[n] += 1
        n = 1
if not d or sum(d.values()) < 2:
    print((2**N-2) % M)
else:
    ds = [k**v for k,v in d.items()]
    ans = 2**N-2

    if len(ds) == 1:
        ans -= 2**(list(d.values())[0]-1)-2
    else:
        for x in ds:
            ans -= 2**x-2

    print(ans % M)
