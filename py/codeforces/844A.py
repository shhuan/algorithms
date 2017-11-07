# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 09:48

"""

S = input()
N = int(input())

C = collections.Counter(S)

m = sum([x-1 for x in C.values()])
n = len(C)

changes = max(0, N-n)
if changes > m:
    print("impossible")
else:
    print(changes)