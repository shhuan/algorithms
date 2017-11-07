# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 17:14

"""

N, K, T = map(int, input().split())

if T <= K:
    print(T)
elif T <= N:
    print(K)
elif T <= N+K:
    print(N+K-T)
else:
    print(0)