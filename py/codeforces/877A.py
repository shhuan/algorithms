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
created by shhuan at 2017/10/30 11:11

"""


S = input()

friends = ["Danil", "Olya", "Slava", "Ann", "Nikita"]

count = 0

for f in friends:
    if count > 1:
        break
    i = 0
    s = S[i:]
    c = 0
    while s:
        i = s.find(f)
        if i >= 0:
            c += 1
            s = s[i+len(f):]
        else:
            s = ''
    count += c

if count == 1:
    print("YES")
else:
    print("NO")