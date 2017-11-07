"""

created by huash06 at 2015-07-15

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools

import math

h, q = [int(x) for x in input().split()]


def rightIndex(index, height):
    res = index
    for _ in range(height):
        res = res * 2 + 1
    return res


def cross4(l1, r1, l2, r2):
    return l2 <= r1 <= r2 or l1 <= l2 <= r1


def cross2(range1, range2):
    l1 = range1[0]
    r1 = range1[1]
    l2 = range2[0]
    r2 = range2[1]
    return cross4(l1, r1, l2, r2)


def merge4(l1, r1, l2, r2):
    return min(l1, l2), max(l2, r2)


def merge2(range1, range2):
    l1 = range1[0]
    r1 = range1[1]
    l2 = range2[0]
    r2 = range2[1]
    return merge4(l1, r1, l2, r2)


def intersection(range1, range2):
    l1 = range1[0]
    r1 = range1[1]
    l2 = range2[0]
    r2 = range2[1]
    return max(l1, l2), min(r1, r2)


def difference(range1, range2):
    if cross2(range1, range2):
        l1 = range1[0]
        r1 = range1[1]
        l2 = range2[0]
        r2 = range2[1]
        if l1 < l2:
            return l1, l2 - 1
        elif r1 > r2:
            return r2 + 1, r1
        else:
            return None
    else:
        return range1


def addRange(rangeList, newRange):
    ar = newRange
    for i, v in enumerate(rangeList):
        r = difference(newRange, v)
        if ar:
            ar = difference(ar, v)
        if not r:
            return False
        else:
            rangeList[i] = r
    if ar:
        rangeList.append(ar)
    return True


possible = []
impossible = []
res = None
for qi in range(q):
    i, l, r, ans = [int(x) for x in input().split()]
    if res:
        continue
    newRange = (int(math.pow(2, h - i) * l), rightIndex(r, h - i))
    if ans == 0:
        if not addRange(impossible, newRange):
            res = "Game cheated!"
            break
    else:
        if not addRange(possible, newRange):
            res = "Game cheated!"
            break
if not possible:
    possible.append((int(pow(2, h - 1)), int(pow(2, h)) - 1))
print(possible)
print(impossible)

if res:
    print(res)
else:
    res = []
    for p in possible:
        v = p
        for ip in impossible:
            if not v:
                break
            v = difference(v, ip)
        if v:
            addRange(res, v)
    count = 0
    for v in res:
        count += v[1] - v[0] + 1
    if count == 1:
        print(res[0][0])
    else:
        print("Data not sufficient!")


