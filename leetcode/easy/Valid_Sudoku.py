# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 15:50

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

"""
__author__ = 'huash06'

import sys
import os


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        if not board:
            return False
        for r in board:
            print(' '.join(r))

        # 行
        for r in range(len(board)):
            used = [0] * 10
            for c in range(len(board[r])):
                ch = board[r][c]
                if not ch.isdigit():
                    continue
                ch = int(ch)
                if not used[ch]:
                    used[ch] = True
                else:
                    return False

        # 列
        for c in range(len(board)):
            used = [0] * 10
            for r in range(len(board[c])):
                ch = board[r][c]
                if not ch.isdigit():
                    continue
                ch = int(ch)
                if not used[ch]:
                    used[ch] = True
                else:
                    return False
        # 宫
        for i in range(3):
            for j in range(3):
                used = [0] * 10
                for r in range(i*3, i*3+3):
                    for c in range(j*3, j*3+3):
                        ch = board[r][c]
                        if not ch.isdigit():
                            continue
                        ch = int(ch)
                        if not used[ch]:
                            used[ch] = True
                        else:
                            return False
        return True



s = Solution()
# print(s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]))
# print(s.isValidSudoku([".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]))
print(s.isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]))