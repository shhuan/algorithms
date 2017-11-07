# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 16:47

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        if n <= 0:
            return []
        board = [['.'] * n for _ in range(n)]
        return self.dfs(n, 0, board, [False]*n)

    def dfs(self, num, row, board, usedCols):
        if row >= num:
            return 1

        ret = 0
        for col, used in enumerate(usedCols):
            if not used and self.canPlace(board, num, row, col):
                usedCols[col] = True
                board[row][col] = 'Q'
                ret += self.dfs(num, row+1, board, usedCols)
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


print(s.totalNQueens(4))

startTime = datetime.datetime.now()
print(s.totalNQueens(9))
print('Time Cose: {}'.format(datetime.datetime.now() - startTime))