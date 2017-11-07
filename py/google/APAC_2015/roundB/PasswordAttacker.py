# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-03 13:55

在键盘上按了M个按键组成了一个N位的密码，计算有多少种可能。

记c个按键组成长度为l的密码的数量为f(c,l)
f(c,l) = c^l - sum(f(c-i,l)*ncr(c,c-i)), 1<=i<l

如果不考虑每个c个按键每个都用过的话，总共有c^l种可能，
减去刚好使用c-i个按键的数量f(c-i,l)*ncr(c,c-i)就是最终结果。
ncr(i,j)是i个物体中取出j个的组合数量




"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils
import operator as op
import functools

__DEBUG__ = True

if __DEBUG__:
    sys.stdin = open('input/sample.txt', 'r')

sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-large-practice.out', 'w')

MAXNN = 101
reader = Utils.Reader()
reader.read()

COUNT = [[0 for col in range(MAXNN)] for row in range(MAXNN)]


def ncr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = functools.reduce(op.mul, range(n, n-r, -1))
    denom = functools.reduce(op.mul, range(1, r+1))
    return numer//denom


def cal(m, n):
    if m <= 1:
        return 1
    if COUNT[m][n] > 0:
        return COUNT[m][n]
    count = 0
    for i in range(1, m):
        count += cal(m-i, n)*ncr(m, m-i)
    count = pow(m, n) - count
    COUNT[m][n] = count
    return count

T = reader.next_int()

for ti in range(1, T+1):
    M = reader.next_int()
    N = reader.next_int()
    RESULT = 0
    print('Case #{}: {}'.format(ti, cal(M, N) % 1000000007))