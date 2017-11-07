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
created by shhuan at 2017/10/21 12:11

"""

N, K = map(int, input().split())

S = input()

C = collections.Counter(S)

if max(C.values()) > K:
    print("NO")
else:
    print("YES")