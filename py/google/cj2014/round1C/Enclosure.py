# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-10 11:21
"""
__author__ = 'huash06'

import sys
import os


sys.stdin = open('input/sample.txt', 'r')
# sys.stdin = open('input/B-small-practice.in', 'r')
sys.stdout = open('output/C-small-practice.out', 'w')

# sys.stdin = open('input/A-large-practice.in', 'r')
# sys.stdout = open('output/A-large-practice.out', 'w')

__DEBUG__ = True

MAXNN = 301



DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

DELTA_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def is_board_enclosed(board, row_count, col_count):
    """
    如果能够涂成同样的颜色，表示未封闭
    :param board:
    :param row_count:
    :param col_count:
    :return:
    """

    start_row = -1
    start_col = -1

    for r in range(row_count):
        if start_row >= 0 and start_col >= 0:
            break
        for c in range(col_count):
            if board[r][c] != '*':
                start_row = r
                start_col = c
                break

    has_blank_edge = False
    q = [(start_row, start_col)]
    board[start_row][start_col] = 'r'
    redge = [0, row_count-1]
    cedge = [0, col_count-1]
    if start_row in redge or start_col in cedge:
        has_blank_edge = True
    while len(q) > 0:
        cr, cc = q.pop()
        for d in DELTA_4:
            r = cr + d[0]
            c = cc + d[1]
            if 0 <= r < row_count and 0 <= c < col_count:
                if board[r][c] != '*' and board[r][c] != 'r':
                    board[r][c] = 'r'
                    q.append((r, c))
                    if r in redge or c in cedge:
                        has_blank_edge = True
    count = 0
    for row in board:
        count += row.count('*')
        count += row.count('r')
    for r in range(row_count):
        for c in range(col_count):
            if board[r][c] == 'r':
                board[r][c] = '.'

    if count < row_count*col_count or (count == row_count*col_count and not has_blank_edge):
        if __DEBUG__:
            print('=======ENCLOSED=======')
            for row in board:
                print(row)
            print()
        return True
    # if __DEBUG__:
    #     print('=======NOT ENCLOSED=======')
    #     for row in board:
    #         print(''.join(row))
    #     print()
    return False


def count_enclose(board):
    count = 0
    stone_count = 0
    for r in range(len(board)):
        li = -1
        ri = -1
        for c in range(len(board[r])):
            if board[r][c] == '*':
                stone_count += 1
                if li == -1:
                    li = c
                else:
                    ri = c
        if ri < 0:
            if li < 0:
                return 1000000, 1000000
            else:
                count += 1
        else:
            count += ri - li + 1

    print('========COUNT BOARD========')
    for row in board:
        print(''.join(row))
    print('COUNT of ABOVE BOARD is {}'.format(count))
    return count, stone_count

DFS_DELTA = [(-1, 0), (1, 0), (1, -1), (1, 0), (1, 1)]
def dfs(board, enclose_count, row_count, col_count, count, row, col):
    if count <= 0:
        if not is_board_enclosed(board, row_count, col_count):
            return enclose_count, enclose_count
        return count_enclose(board)
    min_count = 1000000
    for d in DELTA:
        r = row + d[0]
        c = col + d[1]
        if 0 <= r < row_count and 0 <= c < col_count and board[r][c] != '*':
            board[r][c] = '*'
            ec, sc = dfs(board, enclose_count, row_count, col_count, count-1, r, c)
            if ec == enclose_count:
                min_count = min(sc, min_count)
            board[r][c] = '.'
    return enclose_count, min_count

DELTA_RIGHT = [(-1, 0), (-1, 1), (0, 0), (0, 1), (1, 0), (1, 1)]
DELTA_DOWN_RIGHT = [(1, 0), (1, 1), (0, 1), ]
def DFS(board, enclose_count, row_count, col_count, stone_count, up_row, up_col, down_row, down_col, up_up, down_down):
    if abs(up_row - down_row) <= 1 and abs(up_col - down_col) <= 1 and (up_col > 0 or down_col > 0):
        return count_enclose(board)
    if stone_count <= 0 :
        print('======INVALID STATE======')
        for row in board:
            print(''.join(row))

        return -1, 100000
    # print('======STATE up:{},{} down: {},{}======'.format(up_row, up_col, down_row, down_col))
    # for row in board:
    #     print(''.join(row))
    up_delta = DELTA_RIGHT
    if not up_up:
        up_delta = DELTA_RIGHT[2:]
    down_delta = DELTA_RIGHT
    if not down_down:
        down_delta = DELTA_RIGHT[:4]

    min_stone_used = 1000000
    for du in up_delta:
        for dd in down_delta:
            ur = up_row + du[0]
            uc = up_col + du[1]
            dr = down_row + dd[0]
            dc = down_col + dd[1]
            if 0 <= ur < row_count and \
                0 <= dr < row_count and \
                0 <= uc < col_count and \
                0 <= dc < col_count and \
                abs(ur - dr) <= stone_count and \
                abs(uc - dc) <= stone_count and \
                ur >= dr:
                placed = 0
                if board[ur][uc] != '*':
                    placed += 1
                    board[ur][uc] = '*'
                if board[dr][dc] != '*':
                    placed += 1
                    board[dr][dc] = '*'
                if placed > 0:
                    sc, ec = DFS(board, enclose_count, row_count, col_count, stone_count-placed, ur, uc, dr, dc, ur <= up_row, dr >= down_row)
                    if ec == enclose_count and sc > 0:
                        min_stone_used = min(min_stone_used, sc)
                board[ur][uc] = '.'
                board[dr][dc] = '.'



    return min_stone_used, enclose_count




T = int(input())
for ti in range(1, T + 1):

    N, M, K = (int(v) for v in input().split(' '))

    board = [['.' for c in range(M)] for r in range(N)]
    # print(board)
    if K > M*N:
        result = 0
    else:
        result, enclosed_count = DFS(board, K, N, M, K, N//2, 0, N//2, 0, True, True)
    if result > 0:
        print('Case #{}: {}'.format(ti, result))
    else:
        print('Case #{}: impossible'.format(ti))