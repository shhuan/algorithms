# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 22:46

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned
in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers)
upon entering these rooms; other rooms are either empty (0's) or contain magic orbs
that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible,
the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must
be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the
knight enters and the bottom-right room where the princess is imprisoned.

"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        """
        考虑正向递推，当前位置可能有左边和上边过来，
        假设到达左边的最小花费和剩余生命值分别位c1，r1。
        到达上边的最小花费和剩余的生命值分别位c2, r2。
        此时应该从左边过来还是从上边过来呢？
        答案是无法判断。
        因为如果当前位置是最后一个格子，选择左边还是上边依赖于当前位置的花费。
        1. 如果当前位置是怪物，不仅要根据c1，c2，还要根据r1，r2的值来选择前一步的格子
        2. 如果当前位置是加血宝石，那么应该选择c1，c2更小的格子即可
        所以正向递推是行不通的。


        需要反向递推，即从右下角往左上角递推。
        
            


        :param dungeon:
        :return:
        """
        if not dungeon:
            return 1

        row = len(dungeon)
        col = len(dungeon[0])
        minHP = [[(1<<32)-1 for c in range(col)] for r in range(row)]
        minHP[row-1][col-1] = max(1-dungeon[row-1][col-1], 1)

        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                hp = minHP[r][c]
                if r > 0:
                    if dungeon[r-1][c] >= 0:
                        # 如果上一行相同位置是加血宝石，血量可以更低，只要血量加上宝石的血量大于当前所需的血量即可
                        minHP[r-1][c] = min(max(hp-dungeon[r-1][c], 1), minHP[r-1][c])
                    else:
                        # 如果上一行相同位置是怪物，最低血量升高位hp+|dungeon[r-1][c]|
                        minHP[r-1][c] = min(hp-dungeon[r-1][c], minHP[r-1][c])
                if c > 0:
                    # 相同的方式处理左边
                    if dungeon[r][c-1] >= 0:
                        minHP[r][c-1] = min(max(hp-dungeon[r][c-1], 1), minHP[r][c-1])
                    else:
                        minHP[r][c-1] = min(hp-dungeon[r][c-1], minHP[r][c-1])

        # for c in minHP:
        #     print(c)

        return minHP[0][0]

print((1<<32)-1)

dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]

]

s = Solution()
print(s.calculateMinimumHP(dungeon))

print(s.calculateMinimumHP([[0]]))
print(s.calculateMinimumHP([[100]]))

dungeon = [
    [3,-20,30],
    [-3,4,0]
]
print(s.calculateMinimumHP(dungeon))

dungeon = [
    [1,-3,3],
    [0,-2,0],
    [-3,-3,-3]
]
print(s.calculateMinimumHP(dungeon))