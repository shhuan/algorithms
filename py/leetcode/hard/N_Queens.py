# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 13:56

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import copy
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        if n <= 0:
            return []
        board = [['.'] * n for _ in range(n)]
        return self.dfs(n, 0, board, [False]*n)

    def dfs(self, num, row, board, usedCols):
        if row >= num:
            # 这里可以不用deepcopy， 快很多
            aboard = copy.copy(board)
            return [[''.join(arow) for arow in aboard]]

        ret = []
        for col, used in enumerate(usedCols):
            if not used and self.canPlace(board, num, row, col):
                usedCols[col] = True
                board[row][col] = 'Q'
                oneBoard = self.dfs(num, row+1, board, usedCols)
                ret.extend(oneBoard)
                board[row][col] = '.'
                usedCols[col] = False
        return ret
    def canPlace(self, board, num, row, col):
        # 只需要看上面的斜线位置是否放置， (1, -1), (1, 1)不用检查
        delta = [(-1, -1), (-1, 1)]
        for d in delta:
            r = row + d[0]
            c = col + d[1]
            while 0 <= r < num and 0 <= c < num:
                if board[r][c] == 'Q':
                    return False
                r += d[0]
                c += d[1]
        return True



s = Solution()


print(s.solveNQueens(4))

startTime = datetime.datetime.now()
print(s.solveNQueens(9))
print('Time Cose: {}'.format(datetime.datetime.now() - startTime))
