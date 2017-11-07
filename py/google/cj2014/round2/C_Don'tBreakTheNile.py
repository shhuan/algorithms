# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-29 10:07

外星人要在宽W，长H的河上建一些建筑。
要求计算建完之后最多有多少水流量能从最下面流到最上面。



分析：
每次从最左边一个入口出发，向上找到一条最左的水流路径。
直接计算能够处理小输入




"""
__author__ = 'huash06'

import datetime
import sys
import py.lib.GridViewer as GridViewer
sys.stdin = open('input/C-small-practice.in', 'r')
sys.stdout = open('output/C-small-practice.out', 'w')

# sys.stdin = open('input/A-large-practice.in', 'r')
# sys.stdout = open('output/A-large-practice.out', 'w')

class Solution:
    def __init__(self):
        pass

    def test(self):
        pass

    def readInput(self):
        self.W, self.H, self.B = [int(x) for x in input().split()]
        self.buildings = [list(map(int, input().split())) for i in range(self.B)]

    def readMockInput(self):
        pass

    def showRiver(self, river):
        colors = dict()
        row = [0] * self.W # 0 means water, 1 means wall, 2 means nothing
        for r in range(1, self.H):
            nextRow = [1 if _ == 1 else 2 for _ in river[r]]
            for c in range(self.W):
                if row[c] == 0:
                    colors[(r-1, c)] = 'g'
            row = nextRow
        for c in range(self.W):
            if row[c] == 0:
                colors[(self.H-1, c)] = 'g'
        for r in range(self.H):
            for c in range(self.W):
                if not colors.get((r, c)):
                    if river[r][c] == 1:
                        colors[(r, c)] = 'k'
                    else:
                        colors[(r, c)] = '#009cca'
        GridViewer.draw_rect(self.W, self.H, colors,  edgecolor='#0074a5', title='Max Flow is {}'.format(row.count(0)))

    def solve(self):

        river = [[0 for c in range(self.W)] for r in range(self.H)]
        for x0, y0, x1, y1 in self.buildings:
            for r in range(y0, y1+1):
                for c in range(x0, x1+1):
                    river[r][c] = 1

        row = [0] * self.W # 0 means water, 1 means wall, 2 means nothing
        for c in range(self.W):
            row[c] = river[0][c]

        self.showRiver(river)

        colors = dict()
        for r in range(1, self.H):
            nextRow = [1 if _ == 1 else 2 for _ in river[r]]
            i = self.W - 1
            while i >= 0:
                if row[i] == 0:

                    # flow to right
                    j = i + 1
                    found = False
                    lastJ = j
                    while j < self.W and row[j] == 2:
                        if nextRow[j] == 2:
                            lastJ = j
                            found = True
                        j += 1
                    if found:
                        j = lastJ
                        nextRow[j] = 0
                        row[j] = 0
                    else:
                        # flow to up
                        if nextRow[i] == 2:
                            nextRow[i] = 0
                        else:
                            # flow to left
                            j = i - 1
                            while j >= 0 and row[j] == 2:
                                if nextRow[j] == 2:
                                    nextRow[j] = 0
                                    row[j] = 0
                                    break
                                j -= 1
                i -= 1
            row = nextRow
        return row.count(0)



startTime = datetime.datetime.now()

T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    res = solution.solve()
    print('Case #{}: {}'.format(ti, res))

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))