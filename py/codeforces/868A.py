# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/5 14:59

"""

password = input()
N = int(input())

words = []
for i in range(N):
    words.append(input())

p1 = False
p2 = False
for w in words:
    if w == password:
        p1 = True
        p2 = True
        break
    if w[1] == password[0]:
        p1 = True
    if w[0] == password[1]:
        p2 = True

if p1 and p2:
    print('YES')
else:
    print('NO')
