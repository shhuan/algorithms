# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-18 23:20


某个游戏的每一层地板都是由一格一格的冰块组成，冰块有完好的和碎裂的两种。
人走到碎裂的冰块上就会掉到下一层，走到完好的冰块上这个冰块就会碎裂。
由于游戏机制的限制，不能通过在一格冰块上跳动来使得冰块碎裂并掉下去。
目标是从起始位置开始，找到一条路线能够从目标位置掉下去到下一层。


分析：
目标位置有可能是碎裂的和完好的。
1，如果目标位置是碎裂的，只要找到一条路线能够到达目标位置即可。
2，如果目标位置是完好的，有以下两种情况可以达到目的。
    a，目标位置四周至少有两块完好的冰块，并且有一条路线从起始位置到达目标位置。
        此时到达目标位置之后，目标位置碎裂，然后走到四周的另一块完好的冰块，再回来即可掉下去。
    b，目标位置四周只有一块完好的冰块，除非起始位置就在目标位置隔壁，否则不可能到达。
    c, 如果目标位置周围没有完整的冰块，明显无法走到目标位置，故无法达成目标。


"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime



DELTA = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def existsPath(board, sr, sc, er, ec):
    visited = {(sr, sc)}
    q = [(sr, sc)]
    while q:
        r, c = q.pop(0)

        for d in DELTA:
            nr = r + d[0]
            nc = c + d[1]
            if nr == er and nc == ec:
                return True
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and board[nr][nc] == '.':
                visited.add((nr, nc))
                q.append((nr, nc))

    return False

def isNeighbor(sr, sc, er, ec):
    for d in DELTA:
        r = sr + d[0]
        c = sc + d[1]
        if r == er and c == ec:
            return True
    return False

N, M = list(map(int, input().split()))

board = []
for i in range(N):
    board.append([x for x in input()])

sr, sc = list(map(int, input().split()))
er, ec = list(map(int, input().split()))

sr -= 1
sc -= 1
er -= 1
ec -= 1


if board[er][ec] == 'X':
    if existsPath(board, sr, sc, er, ec):
        print('YES')
    else:
        print('NO')
else:
    itactNeighbor = 0
    for d in DELTA:
        r = er + d[0]
        c = ec + d[1]
        if 0 <= r < N and 0 <= c < M and board[r][c] == '.':
            itactNeighbor += 1

    if itactNeighbor > 1:
        if existsPath(board, sr, sc, er, ec):
            print('YES')
        else:
            print('NO')
    else:
        if itactNeighbor == 1 and isNeighbor(sr, sc, er, ec):
            print('YES')
        else:
            print('NO')



