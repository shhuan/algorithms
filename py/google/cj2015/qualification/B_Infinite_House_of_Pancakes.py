# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-08 16:02

有无限多的客人，每个人面前有一个盘子，有些人的盘子不是空的。
每个时刻，Waiter都可以叫停然后把其中一个盘子的食物挪动到另外一个盘子。
挪动花费1单位时间，1单位时间一个人只能吃掉1单位的食物。

问最少需要多少时间能够把所以的食物吃完。

分析：

假设挪动之后，需要X时间吃完，那么挪动之后所以盘子里面的食物都少于X。
把食物多余X的盘子中的食物挪到其他盘子中至少需要ceil(N/X) - 1的时间


"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import math
sys.stdin = open('input/sampleB.txt', 'r')
sys.stdin = open('input/B-small-practice.in', 'r')
sys.stdout = open('output/B-small-practice.out', 'w')

# sys.stdin = open('input/B-large-practice.in', 'r')
# sys.stdout = open('output/B-large-practice.out', 'w')

__DEBUG__ = True

MAXNN = 301

T = int(input())
for ti in range(1, T + 1):
    D = int(input())
    Cakes = [int(i) for i in input().split(' ')]

    result = 1000
    for x in range(1, 1001):
        t = 0
        for c in Cakes:
            t += math.ceil(c/x) - 1
        result = min(result, x+t)

    print('Case #{}: {}'.format(ti, result))