# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-08 10:02

定义数字后面跟K个感叹号为他的K阶乘，

5!! equals 5 * (5-2) * (5-4) = 15

5!!! equals 5 * (5-3) = 10

5!!!! equals 5 * (5-4) = 5

5 followed by five or more !s = 5


给定一个数字的位数，找出9000的最大的小于它的K阶乘


分析：
数字的位数是它以10为底的对数+1

lg(a*b) = lg(a) + lg(b)
所以a*b的位数等于 lg(a) + lg(b) + 1


"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import math
sys.stdin = open('input/sampleC.txt', 'r')
sys.stdin = open('input/C-small-practice.in', 'r')
sys.stdout = open('output/C-small-practice.out', 'w')

sys.stdin = open('input/C-large-practice.in', 'r')
sys.stdout = open('output/C-large-practice.out', 'w')

__DEBUG__ = True

MAXNN = 301


Digits = [0] * 9001
Digits[0] = 3

for i in range(1, 9001):
    d = math.log10(9000)
    cur = 9000 - i
    while cur > 0:
        d += math.log10(cur)
        cur -= i
    Digits[i] = int(d) + 1

T = int(input())
for ti in range(1, T + 1):

    D = int(input())
    result = -1

    for i in range(9000, 0, -1):
        if Digits[i] < D:
            result = i
        else:
            break
    if result > 0:
        print("Case #{}: IT'S OVER 9000{}".format(ti, ''.join(['!']*result)))
    else:
        print('Case #{}: ...'.format(ti))