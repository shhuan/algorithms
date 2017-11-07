# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-08 20:55


每隔10秒看一看Kaylin的盘子里面有几个蘑菇。
Kaylin吃蘑菇的方式有两种：
1. 任意时刻吃掉任意多的蘑菇
2. 按照某个一定的速度吃


给出每隔10秒蘑菇的数量，计算两种情况下Kaylin最少吃了多少个蘑菇


"""
__author__ = 'huash'

import sys
import os

SMALL_DATASET = True
sys.stdin = open('input/sampleA.txt', 'r')


if SMALL_DATASET:
    sys.stdin = open('input/A-small-practice.in', 'r')
    sys.stdout = open('output/A-small-practice.out', 'w')
else:
    sys.stdin = open('input/A-large-practice.in', 'r')
    sys.stdout = open('output/A-large-practice.out', 'w')



T = int(input())
for ti in range(1, T + 1):

    N = int(input())
    M = list(map(int, input().split()))

    res1 = 0
    res2 = 0

    v = 0
    # 吃蘑菇的最小速度是每个差值的最大值
    for m in range(1, len(M)):
        eated = max(M[m-1] - M[m], 0)
        res1 += eated
        v = max(v, eated)

    for i in range(len(M)-1):
        if M[i] < v:
            res2 += M[i]
        else:
            res2 += v

    print('Case #{}: {} {}'.format(ti, res1, res2))