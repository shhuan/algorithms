# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/6 21:48

"""

a, b = map(int, input().split())


# b! / a! = a+1, a+2, ... b

x = 1
for i in range(a+1, b+1):
    x *= i
    x %= 10
    if x == 0:
        print(0)
        exit(0)
print(x)
