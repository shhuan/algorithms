# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-12 08:28
"""
__author__ = 'huash06'

import datetime
import sys


class FallingSand:
    def simulate(self, board):
        if not board:
            return []
        newBoard = [['.' for c in range(len(board[0]))] for r in range(len(board))]
        for r in range(len(board)-1, -1, -1):
            for c in range(len(board[0])):
                if board[r][c] == 'o':
                    finalRow = r
                    for nr in range(r+1, len(board)):
                        if newBoard[nr][c] == '.':
                            finalRow = nr
                        else:
                            break
                    newBoard[finalRow][c] = 'o'
                else:
                    newBoard[r][c] = board[r][c]
        result = [''.join(row) for row in newBoard]
        return result





s = FallingSand()
result = s.simulate(["ooooo", "..x..", "....x", ".....", "....o"])
for row in result:
    print(row)

print(s.simulate(["..o..", "..x.o", "....x", ".....", "oo.oo" ]) == ["..o..", "..x.o", "....x", ".....", "oo.oo" ])
print(s.simulate(['oxxo']))