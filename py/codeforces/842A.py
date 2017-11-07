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
created by shhuan at 2017/10/20 15:24

"""

l, r, x, y, k = map(int, input().split())


while x <= y:
    b = (x+y)//2
    if l <= b*k <= r:
        print('YES')
        exit(0)
    elif b*k < l:
        x = b+1
    else:
        y = b-1

print('NO')