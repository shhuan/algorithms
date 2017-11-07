"""

created by huash06 at 2015-04-29

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.
"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools
import operator

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        # self.dfs(board, 0, 0)
        self.solve(board)

    def dfs(self, board, row, col):
        if row >= 9:
            return True

        pvs = self.possibleVals(board, row, col)
        for pv in pvs:
            pre = board[row][col]
            board[row][col] = pv
            if col == 8:
                if self.dfs(board, row+1, 0):
                    return True
            else:
                if self.dfs(board, row, col+1):
                    return True
            # 状态恢复
            board[row][col] = pre

        return False

    def possibleVals(self, board, row, col):
        if board[row][col] != '.':
            return {board[row][col]}
        res = {str(i) for i in range(1, 10)}
        for r in range(9):
            res -= {board[r][col]}
        for c in range(9):
            res -= {board[row][c]}
        for r in range(row//3*3, row//3*3+3):
            for c in range(col//3*3, col//3*3+3):
                res -= {board[r][c]}
        return res

    def solve(self, board):
        """
        模拟人的做法，速度快很多。
        先找出可选择最少的空格去填，如果某一个个格子只能够填一个数字，就相当于直接剪掉了很多分支。
        尝试过使用set或者数组记录还有那些格子是空的，话费时间比这个版本高
        :param board:
        :return:
        """
        pos = None
        pvs = None
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    apvs = self.possibleVals(board, r, c)
                    # 优化， 如果有一个位置没有可用的值， 直接返回False
                    if not apvs:
                        return False
                    # 优化， 如果找到一个只能填入一个数字的格子，直接填
                    if len(apvs) == 1:
                        board[r][c] = apvs.pop()
                        if self.solve(board):
                            return True
                        board[r][c] = '.'
                        # 如果填上这个数字之后不能得到最终结果，其他格子也不需要在看
                        return False
                    if not pvs or len(pvs) > len(apvs):
                        pvs = apvs
                        pos = r, c

        # 所有的格子都填上了数字
        if not pvs:
            return True
        for p in pvs:
            pre = board[pos[0]][pos[1]]
            board[pos[0]][pos[1]] = p
            if self.solve(board):
                return True
            board[pos[0]][pos[1]] = pre
        return False


s = Solution()

# board = [['5', '1', '9', '7', '4', '8', '6', '3', '2'],
#         ['7', '8', '3', '6', '5', '2', '4', '1', '.'],
#         ['.', '2', '.', '1', '.', '9', '.', '.', '.'],
#         ['.', '.', '7', '.', '.', '.', '2', '4', '.'],
#         ['.', '6', '4', '.', '1', '.', '5', '9', '.'],
#         ['.', '9', '8', '.', '.', '.', '3', '.', '.'],
#         ['.', '.', '.', '8', '.', '3', '.', '2', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '2', '7', '5', '9', '.', '.']]
# print(s.possibleVals(board, 1, 8))


board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = [list(i) for i in board]
for r in board:
    print(r)
print()

s.solveSudoku(board)

expect = [
    ['5', '1', '9', '7', '4', '8', '6', '3', '2'],
    ['7', '8', '3', '6', '5', '2', '4', '1', '9'],
    ['4', '2', '6', '1', '3', '9', '8', '7', '5'],
    ['3', '5', '7', '9', '8', '6', '2', '4', '1'],
    ['2', '6', '4', '3', '1', '7', '5', '9', '8'],
    ['1', '9', '8', '5', '2', '4', '3', '6', '7'],
    ['9', '7', '5', '8', '6', '3', '1', '2', '4'],
    ['8', '3', '2', '4', '9', '1', '7', '5', '6'],
    ['6', '4', '1', '2', '7', '5', '9', '8', '3']
]

equals = True
for r in range(9):
    for c in range(9):
        if board[r][c] != expect[r][c]:
            equals = False
            break
    if not equals:
        break
print(equals)
if not equals:
    for r in board:
        print(r)


