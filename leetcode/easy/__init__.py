# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-15 08:34
"""
__author__ = 'huash06'

import sys
import os


sys.stdin = open('input/sample.txt', 'r')
sys.stdin = open('input/B-small-practice.in', 'r')
sys.stdout = open('output/B-small-practice.out', 'w')

# sys.stdin = open('input/A-large-practice.in', 'r')
# sys.stdout = open('output/A-large-practice.out', 'w')

__DEBUG__ = True

MAXNN = 301

T = int(input())
for ti in range(1, T + 1):

    # N, M, K = (int(v) for v in input().split(' '))

    result = ''

    if result > 0:
        print('Case #{}: {}'.format(ti, result))
    else:
        print('Case #{}: impossible'.format(ti))