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
created by shhuan at 2017/10/22 12:26

"""

N = int(input())
A = []
for i in range(N):
    A.append(input())


def transform(s):
    t = []
    for c in s:
        if c == 'u':
            t.append('oo')
        elif c == "h":
            while t and t[-1] == "k":
                t.pop()
            t.append("h")
        else:
            t.append(c)

    return "".join(t)

C = set()
for s in A:
    C.add(transform(s))

print(len(C))
