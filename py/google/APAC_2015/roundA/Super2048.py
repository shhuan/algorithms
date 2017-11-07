# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-06 18:25

计算2048游戏中移动一次之后每一格的数字
"""
__author__ = 'huash'

import sys
import os

# sys.stdin = open('input/sample.txt', 'r')
sys.stdin = open('input/B-large-practice.in', 'r')
sys.stdout = open('output/B-large-practice.out', 'w')


def move(B, N, D):
    if D == 'up':
        # up
        for c in range(N):
            d = 0
            for r in range(N):
                if B[r][c] != 0:
                    Board[d][c] = B[r][c]
                    d += 1
            for r in range(d, N):
                Board[r][c] = 0

        for r in range(N-1):
            for c in range(N):
                if B[r][c] == B[r+1][c]:
                    B[r][c] *= 2
                    for i in range(r+1, N-1):
                        B[i][c] = B[i+1][c]
                    B[N-1][c] = 0
    elif D == 'down':
        # down
        for c in range(N):
            d = N-1
            for r in range(N-1, -1, -1):
                if B[r][c] != 0:
                    Board[d][c] = B[r][c]
                    d -= 1
            for r in range(d, -1, -1):
                Board[r][c] = 0

        for r in range(N-1, 0, -1):
            for c in range(N):
                if B[r][c] == B[r-1][c]:
                    B[r][c] *= 2
                    for i in range(r-1, 0, -1):
                        B[i][c] = B[i-1][c]
                    B[0][c] = 0
    elif D == 'left':
        # left
        for r in range(N):
            d = 0
            for c in range(N):
                if B[r][c] != 0:
                    Board[r][d] = B[r][c]
                    d += 1
            for c in range(d, N):
                Board[r][c] = 0

        for c in range(N-1):
            for r in range(N):
                if B[r][c] == B[r][c+1]:
                    B[r][c] *= 2
                    for i in range(c+1, N-1):
                        B[r][i] = B[r][i+1]
                    B[r][N-1] = 0
    elif D == 'right':
        # right
        for r in range(N):
            d = N-1
            for c in range(N-1, -1, -1):
                if B[r][c] != 0:
                    Board[r][d] = B[r][c]
                    d -= 1
            for c in range(d, -1, -1):
                Board[r][c] = 0

        for c in range(N-1, 0, -1):
            for r in range(N):
                if B[r][c] == B[r][c-1]:
                    B[r][c] *= 2
                    for i in range(c-1, 0, -1):
                        B[r][i] = B[r][i-1]
                    B[r][0] = 0


T = int(sys.stdin.readline())
for ti in range(1, T+1):
    line = sys.stdin.readline().strip().split(' ')
    N = int(line[0])
    dir = line[1]

    Board = [0 for col in range(N)]

    for r in range(N):
        line = sys.stdin.readline()
        Board[r] = list(map(int, line.strip().split(' ')))
    move(Board, N, dir)
    print('Case #{}:'.format(ti))
    for r in range(N):
        print(' '.join(str(v) for v in Board[r]))
