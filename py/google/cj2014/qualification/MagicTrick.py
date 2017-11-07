# -*- coding: utf-8 -*-

"""

created by huash06 at 2015-04-07 11:32

在4×4的格子中挑一張牌，說出所在行，洗牌後再挑一次。
問是否可以確定選的哪張牌

過於簡單

"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

__DEBUG__ = True

sys.stdin = open('input/A-small-practice.in', 'r')
sys.stdout = open('output/A-small-practice.out', 'w')

T = int(sys.stdin.readline())
for ti in range(1, T+1):
    r1 = int(sys.stdin.readline())
    p1 = None
    for i in range(4):
        line = sys.stdin.readline()
        if i == r1-1:
            p1 = line.strip().split(' ')
    r2 = int(sys.stdin.readline())
    p2 = None
    for i in range(4):
        line = sys.stdin.readline()
        if i == r2-1:
            p2 = line.strip().split(' ')

    retult = list(set(p1).intersection(set(p2)))
    if len(retult) == 1:
        print('Case #{}: {}'.format(ti, retult[0]))
    elif len(retult) > 1:
        print('Case #{}: {}'.format(ti, 'Bad magician!'))
    else:
        print('Case #{}: {}'.format(ti, 'Volunteer cheated!'))
