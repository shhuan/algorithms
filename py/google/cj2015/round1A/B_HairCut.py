# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-25 16:04

有B个理发师，第i个理发师理发的时间是Mi。
计算第N个理发的人会被第几个理发师理发。



分析：
二分法找出理第N个人的发得时间，然后找出是那个理发师。

"""
__author__ = 'huash06'

import datetime
import sys
import math

# sys.stdin = open('input/B-small-practice.in', 'r')
# sys.stdout = open('output/B-small-practice.out', 'w')

sys.stdin = open('input/B-large-practice.in', 'r')
sys.stdout = open('output/B-large-practice.out', 'w')

class Solution:
    def __init__(self):
        self.B = 0
        self.N = 0
        self.M = None

    def test(self):
        pass

    def readInput(self):
        self.B, self.N = [int(x) for x in input().split()]
        self.M = list(map(int, input().split()))

    def readMockInput(self):
        pass

    def solve(self):
        if self.N < self.B:
            return self.N

        count = int(math.ceil((self.N - self.B) // self.B))
        tmin = count * min(self.M)
        tmax = (count + 1) * max(self.M) + 1

        res = 0
        while tmin < tmax:
            t = (tmax+tmin) // 2
            ct = self.cutting(t)
            if ct >= self.N:
                res = t
                tmax = t
            elif ct < self.N:
                tmin = t + 1

        ct = self.cutting(res-1)

        for i in range(self.B):
            if res % self.M[i] == 0:
                if ct == self.N-1:
                    return i+1
                ct += 1

        return 1

    def cutting(self, t):
        return sum([t//ti+1 for ti in self.M])


startTime = datetime.datetime.now()

T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    res = solution.solve()
    print('Case #{}: {}'.format(ti, res))

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))