# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools

"""
created by shhuan at 2017/10/19 13:07

"""

N = int(input())


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b

    return gcd(b, a%b)

for a in range(N//2, -1, -1):
    b = N-a

    if gcd(b, a) == 1:
        print(a, b)
        exit(0)