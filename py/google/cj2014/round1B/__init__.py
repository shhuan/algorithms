# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-08 14:00
"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

sys.stdin = open('input/sample.txt', 'r')

# sys.stdin = open('input/A-large-practice.in', 'r')
# sys.stdout = open('output/A-large-practice.out', 'w')

MAXNN = 301
T = int(sys.stdin.readline())

for ti in range(1, T + 1):
    # N, L = map(int, sys.stdin.readline().strip().split(' '))

    result = ''

    print('Case #{}: {}'.format(ti, result))