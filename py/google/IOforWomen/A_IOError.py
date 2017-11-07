# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-08 08:35

把IO表示的01字符串转换为普通字符串
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
# sys.stdout = open('output/B-small-practice.out', 'w')

# sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-small-practice.out', 'w')

__DEBUG__ = True

MAXNN = 301

T = int(input())
for ti in range(1, T + 1):

    B = int(input())
    line = input()
    result = ''
    for i in range(0, B*8, 8):
        ch = line[i:i+8]
        ch = ch.replace('I', '1')
        ch = ch.replace('O', '0')
        result += chr(int(ch, 2))
    print('Case #{}: {}'.format(ti, result))