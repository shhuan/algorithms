# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/12 10:34

"""

n, x = map(int, input().split())


if n == 1:
    print('YES')
    print(x)
elif n == 2:
    if x == 0:
        print('NO')
    else:
        print('YES')
        print(0, x)
else:
    nums = [x for x in range(1, n-2)]
    y = 0
    for i in range(len(nums)):
        y ^= nums[i]
    if x == y:
        nums += [2**17, 2**18]
        nums.append(nums[-1] ^ nums[-2])
    else:
        nums += [0, 2**17, (2**17)^x^y] # y^(x^y) = x
    print('YES')
    print(' '.join([str(v) for v in nums]))