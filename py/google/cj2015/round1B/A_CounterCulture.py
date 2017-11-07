# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-25 21:08
"""
__author__ = 'huash'

import sys
import os
import math

sys.stdin = open('input/A-small-practice.in', 'r')
sys.stdout = open('output/A-small-practice-2.out', 'w')
# sys.stdin = open('input/-large-practice.in', 'r')
# sys.stdout = open('output/-large-practice.out', 'w')


class Solution:
    def __init__(self):
        self.N = 0

    def readInput(self):
        self.N = int(input())

    def solve(self):
        # if self.N <= 20:
        #     return self.N
        # times = [i for i in range(self.N+1)]
        # for i in range(1, self.N+1):
        #     rv = self.reverse(i)
        #     if rv <= self.N:
        #         times[rv] = min(times[rv], times[i] + 1)
        #     if i < self.N:
        #         times[i+1] = min(times[i+1], times[i]+1)
        # return times[self.N]
        return self.solve2(self.N)

    def reverse(self, num):
        return int(''.join(list(reversed(str(num)))))

    def solve2(self, num):
        if num <= 20:
            return num

        res = 0
        numStr = list(str(num))
        for i in range(1, len(numStr)):
            pv = int(numStr[i-1])

            res *= 10
            if pv == 0:
                res += int(numStr[i])
                numStr[i] = 0
            elif int(numStr[i]) > pv - 1:
                res += int(numStr[i]) - pv + 1
                numStr[i] = pv - 1
        if numStr[-1] == 0:
            numStr[-1] = 1
            res += 1
        num = self.reverse(int(''.join(map(str, numStr))))
        res += self.solve2(num) + 1

        return res







T = int(input())
for ti in range(1, T + 1):
    s = Solution()
    s.readInput()
    print('Case #{}: {}'.format(ti, s.solve()))