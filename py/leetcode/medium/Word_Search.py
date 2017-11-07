# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 21:09

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not board or not word:
            return False
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if self.dfs(board, word, r, c, {(r, c)}):
                        return True
        return False

    def dfs(self, board, word, row, col, visited):
        if len(word) == 1:
            return True

        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for d in delta:
            r = row + d[0]
            c = col + d[1]
            if 0 <= r < len(board) and \
                0 <= c < len(board[0]) and \
                    (r, c) not in visited and \
                    board[r][c] == word[1]:
                visited.add((r, c))
                if self.dfs(board, word[1:], r, c, visited):
                    return True
                visited.remove((r, c))

        return False


s = Solution()
board = [
  "ABCE",
  "SFCS",
  "ADEE"
]

print(s.exist(board, 'ABCCED'))
print(s.exist(board, 'SEE'))
print(s.exist(board, 'ABCB'))
