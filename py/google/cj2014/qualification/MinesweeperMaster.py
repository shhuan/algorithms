# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-07 13:21

只能大小為R*C的掃雷棋盤， 上面有M個雷。
要求輸出任意一個地雷的佈局，使得只需要點擊一下就能夠掃掉全部的地雷。


"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

__DEBUG__ = True



sys.stdin = open('input/C-large-practice.in', 'r')
# sys.stdin = open('input/sample.txt', 'r')
sys.stdout = open('output/C-large-practice-p.out', 'w')

MAXNN = 51
reader = Utils.Reader()
reader.read()

def verify(Board, row, col):
    MINE_COUNT = [[0 for c in range(col)] for r in range(row)]
    blank = 0
    for r in range(row):
        for c in range(col):
            if Board[r][c] == '*':
                MINE_COUNT[r][c] = -1
                continue
            count = 0
            blank += 1
            for d in DELTA:
                x = r + d[0]
                y = c + d[1]
                if 0 <= x < row and 0 <= y < col:
                    if Board[x][y] == '*':
                        count += 1
            MINE_COUNT[r][c] = count

    sx = -1
    sy = -1
    for r in range(row):
        found = False
        for c in range(col):
            if MINE_COUNT[r][c] == 0:
                sx = r
                sy = c
                found = True
                break
        if found:
            break
    if sx < 0 or sy < 0:
        return False

    q = list()
    q.append((sx, sy))
    MINE_COUNT[sx][sy] = -2
    revealed = 1
    while len(q) > 0:
        r, c = q.pop()
        for d in DELTA:
            x = r + d[0]
            y = c + d[1]
            if 0 <= x < row and 0 <= y < col:
                if MINE_COUNT[x][y] == 0:
                    MINE_COUNT[x][y] = -2
                    revealed += 1
                    q.append((x, y))
                elif MINE_COUNT[x][y] > 0:
                    revealed += 1
                    MINE_COUNT[x][y] = -2

    if revealed == blank:
        Board[sx][sy] = 'c'
        return True
    return False


def back_trace(board, row_count, col_count, current_row, min_place_count, max_place_count, remain_count):
    """
    注意到合法的地雷佈置的方式是，每行都從左往右排，下一行的雷的數量小於等於上一行的數量。

    *****...
    *****...
    ****....
    ***.....
    **......

    總共M個雷，那麼第一行的雷的數量c1 屬於 [M/R, C]
    第2行雷的數量c2 屬於 [(M-c1)/(R-1), c1]
    第i行雷的數量是ci 屬於[(M-sigma(cj))/(max_place_count-i+1), ck]， 1<=j<i， k==i-1


    :param board:
    :param row_count:
    :param col_count:
    :param current_row: current row_count
    :param min_place_count: min mine count
    :param max_place_count: max mine count
    :param remain_count: remain mine count
    :return: true/false
    """
    if current_row >= row_count:
        if remain_count > 0:
            return False
        return verify(board, row_count, col_count)
    for c in range(min_place_count, max_place_count+1):
        for i in range(c):
            board[current_row][i] = '*'
        ll = (remain_count-c)//max((row_count-current_row-1), 1)
        rr = min(c, remain_count-c)
        if back_trace(board, row_count, col_count, current_row+1, ll, rr, remain_count-c):
            return True
        else:
            for i in range(current_row, row_count):
                for j in range(col_count):
                    board[i][j] = '.'


def output_board(Board, row, col):
    for r in range(row):
        print(''.join(Board[r][:col]))

DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

T = reader.next_int()
sys.setrecursionlimit(3000)
for ti in range(1, T+1):
    print('Case #{}:'.format(ti))
    R = reader.next_int()
    C = reader.next_int()
    M = reader.next_int()
    MINE_BOARD = [['.' for c in range(C)] for r in range(R)]
    blk = R*C-M
    if blk <= 0:
        print('Impossible')
        continue
    elif blk == 1:
        for r in range(R):
            for c in range(C):
                MINE_BOARD[r][c] = '*'
        MINE_BOARD[0][0] = 'c'
        output_board(MINE_BOARD, R, C)
        continue


    if back_trace(MINE_BOARD, R, C, 0, M//R, C, M):
        output_board(MINE_BOARD, R, C)
    else:
        print('Impossible')
