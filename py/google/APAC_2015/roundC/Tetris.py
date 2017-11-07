# -*- coding: utf-8 -*-

"""
created by huash06

模拟俄罗斯方块

每次尝试下落一层，如果有冲突就停止下落。
下落之后清除已经放满的层。
GameOver的条件是方块不能够完全放下。
"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

__DEBUG__ = True

# if __DEBUG__:
#     sys.stdin = open('input/sample.txt', 'r')

sys.stdin = open('input/D-large-practice.in', 'r')
sys.stdout = open('output/D-large-practice.out', 'w')

Tetromino = [
    [
        [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 1, 1, 0],
         [1, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 1, 1, 0],
         [1, 1, 0, 0]
         ],
    ],
    [
        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 1, 0]
         ],
        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 1, 0]
         ],
    ],
    [
        [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 0],
         [1, 1, 1, 0]
         ],
        [[0, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 0],
         [1, 0, 0, 0]
         ],
    ],
    [
        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 0],
         [0, 0, 1, 0]
         ],
        [[0, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 1, 0]
         ],
    ],
    [
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 1, 0, 0]
         ],
    ],
    [
        [[1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 1]
         ],
        [[1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 1]
         ],
    ],
    [
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 1, 0]
         ],
        [[0, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0]
         ],
        [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 0, 0]
         ],
    ],
]

MAXNN = 101
reader = Utils.Reader()
reader.read()
T = reader.next_int()


for ti in range(1, T+1):
    print('Case #{}:'.format(ti))
    W = reader.next_int()
    H = reader.next_int()
    N = reader.next_int()

    # Board y方向从上往下计数，x方向从左往右计数
    Board = [[0 for col in range(W)] for row in range(H)]
    gameover = False

    for ni in range(N):
        ti = reader.next_int()-1
        ri = reader.next_int()
        xi = reader.next_int()
        tetromino = Tetromino[ti][ri]

        # 如果游戏结束，继续接受剩余输入并忽略
        if gameover:
            continue

        # 判断最多能够下落几步
        right = min(xi+4, W)
        left = xi
        drop = 0
        for drop in range(H):
            bottom = drop
            top = max(bottom-4, 0)
            candrop = True
            for row in range(bottom, top, -1):
                for col in range(left, right):
                    if Board[row][col] + tetromino[3-bottom+row][col-left] > 1:
                        candrop = False
                        break
                if not candrop:
                    break
            if not candrop:
                drop -= 1
                break

        # 如果不能下落，表示GameOver
        if drop < 0:
            gameover = True
            continue

        # 如果下落步数小于3，需要判断是否有没有落下的实体
        if drop < 3:
            for row in range(3-drop):
                for col in range(4):
                    if tetromino[row][col] != 0:
                        gameover = True
                        break

        # drop tetromino down {drop} level
        if not gameover and drop >= 0:
            bottom = drop
            top = max(bottom-4, -1)

            # tetromino falled at line {bottom}
            for row in range(bottom, top, -1):
                for col in range(xi, right):
                    Board[row][col] += tetromino[3-bottom+row][col-left]

            # clear lines which are filled by tetrominos
            row = bottom
            while row > top:
                filled = True
                for col in range(W):
                    if Board[row][col] == 0:
                        filled = False
                        break
                # clear this filled line, and move above lines down
                if filled:
                    for col in range(W):
                        Board[row][col] = 0
                    for above in range(row-1, -1, -1):
                        for col in range(W):
                            Board[above+1][col] = Board[above][col]
                    row += 1
                    # clear the highest line
                    for col in range(W):
                        Board[0][col] = 0
                row -= 1
        else:
            gameover = True

    # output result
    if gameover:
        print('Game Over!')
    else:
        for row in range(H):
            for col in range(W):
                if Board[row][col] == 1:
                    sys.stdout.write('x')
                else:
                    sys.stdout.write('.')
            print('')



