# -*- coding: utf-8 -*-

"""
created by 'huash' at '2015'-'03'-'26' '20':'55'

题意：判断棋盘上只走一步有多少种吃子的可能

分析：扫描每个棋子，看他能杀死多少个其他棋子，总数即是累加和

"""
__author__ = 'huash'

import sys
import os
import matplotlib.pyplot as plt


__DEBUG__ = False
# __DEBUG__ = True
sys.stdin = open('input/D-large-practice.in', 'r')
# sys.stdin = open('input/sample.txt', 'r')
if not __DEBUG__:
    sys.stdout = open('output/D-large-practice.out', 'w')

lines = list()
for line in sys.stdin:
    if len(line.strip()) > 0:
        lines.append(line)

T = int(lines[0])

line_index = 0


def next_line():
    global line_index
    line_index += 1
    return lines[line_index]


CHESS_WIDTH = 8


def normalize_coord(pos, min_val, max_val):
    x = max(pos[0], min_val)
    x = min(x, max_val)
    y = max(pos[1], min_val)
    y = min(y, max_val)
    return x, y


def move_queen(loc, chessboard):
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for d in deltas:
        x = loc[0]
        y = loc[1]
        while 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
            x += d[0]
            y += d[1]
            if 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
                if chessboard.get('{}{}'.format(x, y)) is not None:
                    count += 1
                    break
            else:
                break
    if __DEBUG__:
        print('Queue ({},{}) kills {}'.format(symble_map[loc[0]], loc[1], count))
    return count


def move_king(loc, chessboard):
    deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for d in deltas:
        x = loc[0] + d[0]
        y = loc[1] + d[1]
        if 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
            if chessboard.get('{}{}'.format(x, y)) is not None:
                count += 1
    if __DEBUG__:
        print('King ({},{}) kills {}'.format(symble_map[loc[0]], loc[1], count))
    return count


def move_rook(loc, chessboard):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    for d in deltas:
        x = loc[0]
        y = loc[1]
        while 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
            x += d[0]
            y += d[1]
            if 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
                if chessboard.get('{}{}'.format(x, y)) is not None:
                    count += 1
                    break
            else:
                break
    if __DEBUG__:
        print('Rook ({},{}) kills {}'.format(symble_map[loc[0]], loc[1], count))
    return count


def move_bishop(loc, chessboard):
    deltas = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0
    for d in deltas:
        x = loc[0]
        y = loc[1]
        while 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
            x += d[0]
            y += d[1]
            if 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
                if chessboard.get('{}{}'.format(x, y)) is not None:
                    count += 1
                    break
            else:
                break
    if __DEBUG__:
        print('Bishop ({},{}) kills {}'.format(symble_map[loc[0]], loc[1], count))
    return count


def move_knight(loc, chessboard):
    deltas = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1)]
    count = 0
    for d in deltas:
        x = loc[0] + d[0]
        y = loc[1] + d[1]
        if 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
            if chessboard.get('{}{}'.format(x, y)) is not None:
                count += 1
    if __DEBUG__:
        print('Knight ({},{}) kills {}'.format(symble_map[loc[0]], loc[1], count))
    return count


def move_pawn(loc, chessboard):
    deltas = [(1, 1), (1, -1)]
    count = 0
    for d in deltas:
        x = loc[0] + d[0]
        y = loc[1] + d[1]
        if 1 <= x <= CHESS_WIDTH and 1 <= y <= CHESS_WIDTH:
            if chessboard.get('{}{}'.format(x, y)) is not None:
                count += 1
    if __DEBUG__:
        print('Pawn ({},{}) kills {}'.format(symble_map[loc[0]], loc[1], count))
    return count


number_map = dict(A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8)
symble_map = dict([(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F'), (7, 'G'), (8, 'H')])
for ti in range(1, T + 1):
    N = int(next_line())
    chessboard = dict([])
    for ni in range(N):
        pos = next_line().strip().split('-')
        chessboard['{}{}'.format(number_map[pos[0][0]], pos[0][1])] = pos[1]
    # print(chessboard)

    fig = plt.figure('Chessboard')
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel('A-H')
    plt.ylabel('1-9')

    for y in range(1, 9):
        plt.text(0.7, y + 0.5, '{}'.format(y))

    for x in range(1, 9):
        plt.text(x + 0.5, 0.7, '{}'.format(symble_map[x]))

    for x in range(1, 10):
        plt.plot((x, x), (1, 9), 'b')
    for y in range(1, 10):
        plt.plot((1, 9), (y, y), 'b')
    count = 0
    for pos, chess in chessboard.items():
        pos = map(int, pos)
        if chess == 'K':
            plt.text(pos[0] + 0.4, pos[1] + 0.4, r'K', {'color': 'black'})
            count += move_king(pos, chessboard)
        elif chess == 'Q':
            plt.text(pos[0] + 0.4, pos[1] + 0.4, r'Q', {'color': 'red'})
            count += move_queen(pos, chessboard)
        elif chess == 'R':
            plt.text(pos[0] + 0.4, pos[1] + 0.4, r'R', {'color': 'orange'})
            count += move_rook(pos, chessboard)
        elif chess == 'N':
            plt.text(pos[0] + 0.4, pos[1] + 0.4, r'N', {'color': '#A0522D'})
            count += move_knight(pos, chessboard)
        elif chess == 'B':
            plt.text(pos[0] + 0.4, pos[1] + 0.4, r'B', {'color': 'blue'})
            count += move_bishop(pos, chessboard)
        elif chess == 'P':
            plt.text(pos[0] + 0.4, pos[1] + 0.4, r'P', {'color': '#40E0D0'})
            count += move_pawn(pos, chessboard)
    print('Case #{}: {}'.format(ti, count))

    if __DEBUG__:
        plt.show()
        fig.savefig('output/chessboard.png')