# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-26 15:43

某个国家有D种面值的货币，规定付款时每种面值的货币不能超过C个，
给出现有D种货币的面值，计算最少需要增加几种货币才能够一次支付[1, V]的所有数量的货款。


分析：
假设现有货币能够支付[1, V1]的所有货款，假设增加一种面值为X的货币，
此时就能够支付[1, V1+C*X]的所有货款，X必须小于等于V1+1。

因为[1, V1]的最后X个数字为V1-X+1,...,V1,每个都加上X后得到V1+1,...,V1+X，
最后X个数字继续增加X得到V1+X+1,...,V1+2*X，最后能够达到V1+C*X。


显然每次X选择上次能够达到的最大值V1'+1时，需要增加的货币数量最少。



"""
__author__ = 'huash06'

import datetime
import sys

# sys.stdin = open('input/C-small-practice.in', 'r')
# sys.stdout = open('output/C-small-practice.out', 'w')

sys.stdin = open('input/C-large-practice.in', 'r')
sys.stdout = open('output/C-large-practice.out', 'w')

class Solution:
    def __init__(self):
        pass

    def test(self):
        pass

    def readInput(self):
        self.C, self.D, self.V = [int(x) for x in input().split()]
        self.coins = list(map(int, input().split()))
        self.coins.sort()

    def readMockInput(self):
        pass

    def solve(self):
        vmax = 0
        res = 0

        while vmax < self.V:
            x = vmax + 1 # The smallest value we cannot produce.
            if self.coins and self.coins[0] <= x:
                x = self.coins.pop(0)
            else:
                res += 1
            vmax += x * self.C
        return res


startTime = datetime.datetime.now()

T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    res = solution.solve()
    print('Case #{}: {}'.format(ti, res))

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))