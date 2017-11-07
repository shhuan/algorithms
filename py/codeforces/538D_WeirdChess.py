# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-20 08:39

有个N*N的棋盘，上面只有一种类型的棋子。
Igor在上面放了一些棋子，用o表示。
他命令这些棋子攻打一些位置，用x表示。

要求在一个(2N-1)*(2N-1)的棋盘上摆出这种棋子的所有走法。

注意，并不限定是国际象棋，棋子的走法任意。



分析：
暴力枚举所有可以走不可以走的偏移量。

"""
__author__ = 'huash06'

import datetime
import sys
import copy
import functools
import collections
import itertools

class Solution:
    def __init__(self):
        self.N = 0
        self.boards = None

    def test(self):
        pass

    def readInput(self):
        self.N = int(input())
        self.boards = []
        for i in range(self.N):
            self.boards.append(list(input()))

    def readMockInput(self):
        pass

    def solve(self):
        N = self.N
        impossibleMoves = set()
        chesses = list()
        notAttacked = list()
        # record all impossible moves
        for r in range(N):
            for c in range(N):
                if self.boards[r][c] == 'o':
                    chesses.append((r, c))
                elif self.boards[r][c] == '.':
                    notAttacked.append((r, c))
        # print(chesses)
        # print(notAttacked)
        for r, c in chesses:
            for i, j in notAttacked:
                impossibleMoves.add((i-r, j-c))

        startTime = datetime.datetime.now()

        # check whether there are any conflicts
        for i in range(N):
            for j in range(N):
                if self.boards[i][j] == 'o':
                    continue
                for r, c in chesses:
                    if (i-r, j-c) not in impossibleMoves:
                        if self.boards[i][j] == '.':
                            print('NO')
                            return
                        self.boards[i][j] = 'v'

        # LTE
        # for r, c in chesses:
        #     for i in range(-N+1, N):
        #         for j in range(-N+1, N):
        #             # much faster than 2 for
        #             if (i, j) not in impossibleMoves:
        #                 nr = r + i
        #                 nc = c + j
        #                 if 0 <= nr < N and 0 <= nc < N and self.boards[nr][nc] != 'o':
        #                     # reboard[nr][nc] = 'x'
        #
        #                     if self.boards[nr][nc] == '.':
        #                         print('NO')
        #                         return
        #                     self.boards[nr][nc] = 'v'
        if sum([row.count('x') for row in self.boards]) > 0:
            print('NO')
            return
        sys.stderr.write('Check Cost: {}\n'.format(datetime.datetime.now()-startTime))


        # output result
        rn = 2*N-1
        res = [['.' for c in range(rn)] for r in range(rn)]
        res[N-1][N-1] = 'o'
        for i in range(-N+1, N):
            for j in range(-N+1, N):
                if not (i == 0 and j == 0) and (i, j) not in impossibleMoves:
                    res[i+N-1][j+N-1] = 'x'
        print('YES')
        for row in res:
            print(''.join(row))



solution = Solution()
solution.readInput()
startTime = datetime.datetime.now()
solution.solve()
sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))