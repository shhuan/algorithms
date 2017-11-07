# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/20 08:16

"""


N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

a = min(A)
b = min(B)
c = set(A) & set(B)

if c:
    print(min(c))
elif a > b:
    print(b*10+a)
else:
    print(a*10+b)
