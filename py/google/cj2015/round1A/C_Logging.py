# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-25 17:18

有一个森林，计算以每一颗树作为凸包顶点至少需要砍掉多少颗树

"""
__author__ = 'huash06'

import datetime
import sys
from math import atan2
import functools
# sys.stdin = open('input/C-small-practice.in', 'r')
# sys.stdout = open('output/C-small-practice.out', 'w')

sys.stdin = open('input/C-large-practice.in', 'r')
sys.stdout = open('output/C-large-practice.out', 'w')

class Solution:
    def __init__(self):
        self.N = 0
        self.trees = list()

    def test(self):
        pass

    def readInput(self):
        self.N = int(input())
        self.trees = [tuple(map(int, input().split())) for _ in range(self.N)]


    def readMockInput(self):
        pass

    def solve(self):
        P = self.trees
        n = self.N - 1
        for cx, cy in P:
            D = [(x-cx, y-cy) for x, y in P if x != cx or y != cy]

            # 根据向量夹角排序
            D.sort(key=lambda p: atan2(*p))
            j = 0
            m = 0

            for i in range(n):
                # 对每一个向量，把他右边的向量都砍掉
                while self.right(D[i], D[j%n]) and j < i+n:
                    j += 1
                m = max(m, j-i)
            print(n-m)


    def right(self, p, q):
        """
        p, q 是选定点到两个点的向量。
        向量乘积p x q = x1*y2-x2*y1 = |p|*|q|*sin(angle)。
        所以p x q <= 0时，在顺时针方向，即右边
        :param p:
        :param q:
        :return:
        """
        return p[0]*q[1]-p[1]*q[0] <= 0


startTime = datetime.datetime.now()

T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    print('Case #{}:'.format(ti))
    solution.solve()

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))