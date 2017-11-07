# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import sys

"""
created by shhuan at 2017/10/12 11:57

"""

n = int(input())


def make_query(l, r, n):
    ans = ['1'] * n
    for i in range(l, r+1):
        ans[i] = '0'
    return ' '.join(ans)

print(make_query(0, -1, n))
sys.stdout.flush()
allzeros = int(input())
# allzeros = allzeros - (n-allzeros)

l = 0
r = n-1
zeroindex = -1
oneindex = -1
while True:
    if zeroindex >= 0 and oneindex >= 0:
        print('! %d %d' % (zeroindex+1, oneindex+1))
        exit(0)
    mid = (l+r)//2
    print(make_query(l, mid, n))
    sys.stdout.flush()
    d = int(input())
    zeros = d-allzeros
    if zeros == mid-l+1:
        zeroindex = l
        l = mid+1
        r = n-1
    elif zeros == mid-r-1:
        oneindex = l
        l = mid+1
        r = n-1
    else:
        r = mid-1




