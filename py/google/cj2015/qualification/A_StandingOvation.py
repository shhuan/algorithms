# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-08 15:01

每个观众有个害羞值Si，必须要有Si个人站起来他才站起来。
问需要邀请多少额外的观众才能使得所有人都站起来。

分析：
直接以Si从小到大遍历，如果当前站起来的人数不够，则需要增加相应的人数

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

sys.stdin = open('input/sampleA.txt', 'r')
sys.stdin = open('input/A-small-practice.in', 'r')
sys.stdout = open('output/A-small-practice.out', 'w')

# sys.stdin = open('input/A-large-practice.in', 'r')
# sys.stdout = open('output/A-large-practice.out', 'w')

__DEBUG__ = True

MAXNN = 301

T = int(input())
for ti in range(1, T + 1):

    N, S = input().split(' ')
    N = int(N)
    result = 0
    count = int(S[0])
    for i in range(1, N+1):
        if count < i:
            result += i-count
            count = i
        count += int(S[i])

    print('Case #{}: {}'.format(ti, result))