# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 15:28

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

"""
__author__ = 'huash06'

import sys
import os

class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):

        if not grid:
            return 0

        delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        count = 0
        row_count = len(grid)
        for i in range(row_count):
            col_count = len(grid[i])
            for j in range(col_count):
                if grid[i][j] == '1':
                    count += 1
                    q = [(i, j)]
                    while q:
                        i0, j0 = q.pop()
                        for d in delta:
                            i1 = i0 + d[0]
                            j1 = j0 + d[1]
                            if 0 <= i1 < row_count and 0 <= j1 < col_count:
                                if grid[i1][j1] == '1':
                                    q.append((i1, j1))
                                    grid[i1][j1] = 'X'
                # for r in grid:
                #     print(r)
                # print('')
        return count

s = Solution()

# A = [
#     list('11110'),
#     list('11010'),
#     list('11000'),
#     list('00000')
#     ]
# print(s.numIslands(A))


B = [
    list('11000'),
    list('11000'),
    list('00100'),
    list('00011')
]
print(s.numIslands(B))








