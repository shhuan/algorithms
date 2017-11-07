# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-03-27 13:31

最少多少步可以扫掉所有雷

"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils
import matplotlib.pyplot as plt
import py.lib.GridViewer as GridViewer
__DEBUG__ = False

sys.stdin = open('input/A-large-practice.in', 'r')
# if __DEBUG__:
#     sys.stdin = open('input/sample.txt', 'r')
if not __DEBUG__:
    sys.stdout = open('output/A-large-practice.out', 'w')


MAXNN = 301
board = [[0 for row in range(MAXNN)] for col in range(MAXNN)]

reader = Utils.Reader()

T = int(sys.stdin.readline())
deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

#  读取输入并且为每个格子标记上相应的数字
for ti in range(1, T+1):
    N = int(sys.stdin.readline())
    for ni in range(N):
        board[ni] = list(sys.stdin.readline().strip())
    for row in range(N):
        for col in range(N):
            if board[row][col] == '.':
                board[row][col] = 0
            elif board[row][col] == '*':
                for delta in deltas:
                    x = row + delta[0]
                    y = col + delta[1]
                    if 0 <= x < N and 0 <= y < N:
                        if board[x][y] == '.':
                            board[x][y] = 1
                        elif isinstance(board[x][y], int):
                            board[x][y] += 1

    # grid_viewer = GridViewer.draw_grid(board, 0, N, 0, N)
    if __DEBUG__:
        plt.figure(u'MineBoard')
        plt.subplot(3, 1, 1)
        plt.xlim(-1, N+1)
        plt.ylim(-1, N+1)
        for row in range(N):
            for col in range(N):
                if isinstance(board[row][col], int):
                    plt.text(row, col, '{}'.format(board[row][col]), color='#8E2323')
                else:
                    plt.text(row, col, '{}'.format(board[row][col]))

    # 第一次扫描，把所有的数字是0个格子和附近的格子都扫除掉
    count = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:
                count += 1
                board[row][col] = '{}'.format(count)
                q = [(row, col)]
                while len(q) > 0:
                    r, c = q.pop()
                    for delta in deltas:
                        x = r + delta[0]
                        y = c + delta[1]
                        if 0 <= x < N and 0 <= y < N:
                            if board[x][y] == 0:
                                # print('({},{}) <-- ({},{})'.format(row, col, x, y))
                                board[x][y] = '{}'.format(count)
                                q.append((x, y))
                            elif isinstance(board[x][y], int):
                                # print('sweep {},{}'.format(x, y))
                                board[x][y] = '{}'.format(count)

                # print('==========')

    # print(count)
    if __DEBUG__:
        plt.subplot(3, 1, 2)
        plt.xlim(-1, N+1)
        plt.ylim(-1, N+1)
        for row in range(N):
            for col in range(N):
                if isinstance(board[row][col], int):
                    plt.text(row, col, '{}'.format(board[row][col]), color='#8E2323')
                elif board[row][col] == '*':
                    plt.text(row, col, '{}'.format(board[row][col]))
                else:
                    plt.text(row, col, '{}'.format(board[row][col]), color='green')
        plt.subplot(3, 1, 3)
        plt.xlim(-1, N+1)
        plt.ylim(-1, N+1)

    # 第二次扫描剩下的不和0相连的其他数字
    for row in range(N):
        for col in range(N):
            if isinstance(board[row][col], int):
                count += 1
                if __DEBUG__:
                    plt.text(row, col, '{}'.format(count), color='red')
            elif __DEBUG__:
                if board[row][col] == '*':
                    plt.text(row, col, board[row][col])
                else:
                    plt.text(row, col, board[row][col], color='green')

    print('Case #{}: {}'.format(ti, count))

    if __DEBUG__:
        plt.show()
