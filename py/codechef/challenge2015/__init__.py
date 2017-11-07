# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-09 09:51
"""
__author__ = 'huash'

import sys
import os

SMALL_DATASET = True

if SMALL_DATASET:
    sys.stdin = open('input/-small-practice.in', 'r')
    sys.stdout = open('output/-small-practice.out', 'w')
else:
    sys.stdin = open('input/-large-practice.in', 'r')
    sys.stdout = open('output/-large-practice.out', 'w')

T = int(input())
for ti in range(1, T + 1):
    result = ''

    print('Case #{}: {}'.format(ti, result))