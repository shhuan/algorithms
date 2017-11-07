# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-08 13:42

在地板上只能往前走，或者右转后往前走，走到不能走为止。
问R*C的地板上有多少种走法
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

sys.stdin = open('input/sampleD.txt', 'r')
sys.stdin = open('input/D-small-practice.in', 'r')
sys.stdout = open('output/D-small-practice.out', 'w')

sys.stdin = open('input/D-large-practice.in', 'r')
sys.stdout = open('output/D-large-practice.out', 'w')

__DEBUG__ = True

MAXNN = 301


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(board, row, col, r, c, direction):
    count = 0
    r += delta[direction][0]
    c += delta[direction][1]
    if 0 <= r < row and 0 <= c < col:
        if not board[r][c]:
            board[r][c] = True
            count += dfs(board, row, col, r, c, direction)
            board[r][c] = False

    direction = (direction + 1) % 4
    r += delta[direction][0]
    c += delta[direction][1]
    if 0 <= r < row and 0 <= c < col:
        if not board[r][c]:
            board[r][c] = True
            count += dfs(board, row, col, r, c, direction)
            board[r][c] = False
    # if count == 0:
    #     for b in board:
    #         print(b)
    #     print()
    return max(count, 1)



def dp(R, C):
    """
    假设从最左边一列往上开始走， 每到一个格子（包括第一个）都可以往右转。
    假设从第r行右转，那么转过去之后又只能在一个r*(C-1)的矩形内移动，
    所以这是一个递归的问题。
    设f(r,c)表示在r*c中移动的数量，有
    f(r,c) = sigma(f(r', c-1)), 1<=r'<=r


    :param R:
    :param C:
    :return:
    """

    board = [[0 for c in range(C)] for r in range(R)]

    for r in range(R):
        board[r][0] = 1

    for r in range(R):
        for c in range(C-1):
            for ru in range(r, R):
                board[ru][c+1] += board[r][c]

    # for b in board:
    #     print(b)
    # print()

    return board[R-1][C-1]




T = int(input())
for ti in range(1, T + 1):

    R, C = (int(v) for v in input().split(' '))

    board = [[False for c in range(C)] for r in range(R)]


    board[0][0] = True
    # result = dfs(board, R, C, 0, 0, 0)
    result = dp(R, C)
    if result > 0:
        print('Case #{}: {}'.format(ti, result))
    else:
        print('Case #{}: impossible'.format(ti))


