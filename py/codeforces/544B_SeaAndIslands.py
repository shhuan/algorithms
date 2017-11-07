# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-18 16:56

使用N个单位沙子把一块海域划分成K个岛屿

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import math

N, K = [int(x) for x in input().split()]

if K > int(math.ceil((N*N)/2)):
    print('NO')
elif K == 0:
    for i in range(N):
        print('S'*N)
else:
    board = [[0 for c in range(N)] for r in range(N)]

    for r in range(0, N):
        start = 0 if r%2 == 0 else 1
        for c in range(start, N, 2):
            K -= 1
            board[r][c] = 1
            if K <= 0:
                break
        if K <= 0:
            break
    for r in range(N):
        row = ''
        for c in range(N):
            if board[r][c]:
                row += 'L'
            else:
                row += 'S'
        print(row)


