# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-18 15:10


把一个字符串分割成K个字符串，并且每个字符串的第一个字母都不相同

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections



def findBeautifulStr(astr, n):
    res = []
    firsts = set()
    i = 0
    while i < len(astr):
        firsts.add(astr[i])
        if len(res) == n - 1:
            res.append(astr[i:])
            break

        hasNext = False
        for j in range(i+1, len(astr)):
            if astr[j] not in firsts:
                res.append(astr[i:j])
                i = j
                hasNext = True
                break
        if not hasNext:
            break

    if len(res) == n:
        return res
    return []



N = int(input())
S = input()

res = findBeautifulStr(S, N)
if res:
    print('YES')
    for seg in res:
        print(seg)
else:
    print('NO')
