# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-26 12:06

给猴子一个键盘让他打字，键盘上有K个按键，每个按键上有个大写字母，不同的按键可能是相同的字母。
让猴子打S个字母，其中每包含一个厂为L的目标字符串T就给他一根香蕉。

你必须带够足够多的香蕉保证任何情况下都香蕉都够用，计算剩下的香蕉的期望。




分析：
先计算出打出每个字母的概率，如果某个字符不能够打出，不带香蕉，剩下0个。

猴子打出的字符串中从第i个字符开始是一个目标字符串的概率是pi，显然pi是相互独立的。
期望能够打出的T的数量是：E = S//L * pi

猴子最多能够打出T的数量和T的格式相关，假设T的最长的前缀后缀的长度是N，最多可以打出
(S-(L-N))//N个T

期望剩余的数量就是: (S-(L-N))//N - S//L*pi


"""
__author__ = 'huash06'

import datetime
import sys
import collections
# sys.stdin = open('input/B-small-practice.in', 'r')
# sys.stdout = open('output/B-small-practice.out', 'w')

sys.stdin = open('input/B-large-practice.in', 'r')
sys.stdout = open('output/B-large-practice.out', 'w')

class Solution:
    def __init__(self):
        self.K, self.L, self.S = 0, 0, 0
        self.keys = None
        self.target = None

    def test(self):
        pass

    def readInput(self):
        self.K, self.L, self.S = [int(x) for x in input().split()]
        self.keys = list(input())
        self.target = input()

    def readMockInput(self):
        pass

    def solve(self):
        if self.S < self.L:
            return .0

        wc = collections.defaultdict(int)
        for k in self.keys:
            wc[k] += 1

        for k in self.target:
            if wc[k] <= 0:
                return 0.0
        p = collections.defaultdict(int)
        count = len(self.keys)
        for k in wc:
            p[k] = wc[k]/count

        p0 = 1
        for w in self.target:
            p0 *= p[w]
        p0 *= self.S-self.L+1

        sx = self.suffix(self.target)
        sx = (self.S - self.L + sx) // sx
        res = max(sx - p0, 0.0)

        return res

    def suffix(self, astr):

        for i in range(1, len(astr)):
            if astr[i:] == astr[:len(astr)-i]:
                return i
        return len(astr)



startTime = datetime.datetime.now()

T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    res = solution.solve()
    print("Case #%d: %.9f" % (ti, res))

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))