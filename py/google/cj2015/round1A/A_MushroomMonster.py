# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-25 14:43


Kaylin 喜欢蘑菇，Bartholomew 可以随意往Kaylin的盘子里面放蘑菇。
每隔10秒钟看一次她盘子里面有多少个蘑菇，计算一下两种情况下Kaylin最少吃了多少个蘑菇。
1. Kaylin可以在任意时刻吃掉任意数量的蘑菇
2. Kaylin匀速吃掉蘑菇

"""
__author__ = 'huash06'

import datetime
import sys

# sys.stdin = open('input/A-small-practice.in', 'r')
# sys.stdout = open('output/A-small-practice.out', 'w')

sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-large-practice.out', 'w')
class Solution:
    def __init__(self):
        self.N = 0
        self.plates = None

    def test(self):
        pass

    def readInput(self):
        self.N = int(input())
        self.plates = list(map(int, input().split()))

    def readMockInput(self):
        pass

    def solve(self):
        ra = self.solveA()
        rb = self.solveB()
        return ra, rb
    def solveA(self):
        res = 0
        for i in range(len(self.plates)):
            if i < len(self.plates) - 1:
                res += max(0, self.plates[i]-self.plates[i+1])
        return res
    def solveB(self):
        v = 0
        for i in range(len(self.plates)):
            if i < len(self.plates) - 1:
                v = max(v, self.plates[i] - self.plates[i+1])
        res = 0
        for i in range(len(self.plates)-1):
            res += min(self.plates[i], v)
        return res

T = int(input())
for ti in range(1, T+1):
    solution = Solution()
    solution.readInput()
    startTime = datetime.datetime.now()
    ra, rb = solution.solve()
    sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))
    print('Case #{}: {} {}'.format(ti, ra, rb))
