# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 13:10

"""

N, K = map(int, input().split())

if K == N or K == 0:
    print(0, 0)
else:
    print(1, min(N-K, K*2))