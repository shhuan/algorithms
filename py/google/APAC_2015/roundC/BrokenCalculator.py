# -*- coding: utf-8 -*-

"""
created by 'huash' at '2015-03-30 20:09'

只能使用乘法、等号以及某些数字键，求能够得到给定数字的最少按键次数

"""
__author__ = 'huash'

import sys
import os
import py.lib.Utils as Utils
import itertools
import math

# sys.stdin = open('input/sample.txt', 'r')
sys.stdin = open('input/C-large-practice.in', 'r')
sys.stdout = open('output/C-large-practice.out', 'w')

reader = Utils.Reader()
reader.read()

T = reader.next_int()
for ti in range(1, T + 1):
    availableDigit = list()
    for i in range(10):
        v = reader.next_int()
        if v == 1:
            availableDigit.append(str(i))
    value = reader.next_int()

    # print('========={}========'.format(value))
    # print(availableDigit)

    times = [0] * (value + 1)

    # 如果组成数字的所有的数字字符都可以按，直接按出结果即可
    valueDigit = str(value)
    allDigitAvailable = True
    for digit in valueDigit:
        if digit not in availableDigit:
            allDigitAvailable = False
            break
    if allDigitAvailable:
        print('Case #{}: {}'.format(ti, len(valueDigit) + 1))
        continue

    # 找到所有可以直接按的数字
    Q = list()
    for v in range(1, value):
        valueDigit = str(v)
        allDigitAvailable = True
        for digit in valueDigit:
            if digit not in availableDigit:
                allDigitAvailable = False
                break
        if allDigitAvailable:
            times[v] = len(valueDigit)
            Q.append(v)

    # 使用最短路径的方式，如果某个数字可以使用更少的步骤得出，更新所有可以由它做乘法得到的数字的按键次数
    while len(Q) > 0:
        a = Q.pop()
        if a <= 1 or times[a] <= 0:
            continue
        for b in range(2, value // a + 2):
            if times[b] > 0:
                v = a * b
                t = times[a] + times[b] + 1
                if v <= value and (times[v] == 0 or times[v] > t):
                    times[v] = t
                    Q.append(v)

    if times[value] > 0:
        print('Case #{}: {}'.format(ti, times[value] + 1))
    else:
        print('Case #{}: Impossible'.format(ti))

