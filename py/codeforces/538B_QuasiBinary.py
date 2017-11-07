"""

created by huash06 at 2015-05-19

只由1、0组成的数字叫quasibinary。
给一个数字N，找出最少数量的quasibinary，使他们的和等于N


"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools
import math

class Solution:
    def __init__(self):
        self.N = 0

    def readInput(self):
        self.N = input()

    def readMockInput(self):
        pass

    def solve(self):
        num = list(map(int, self.N))
        res = []
        while num.count(0) < len(num):
            tmp = ''
            for i in range(len(num)):
                if num[i] > 0:
                    num[i] -= 1
                    tmp += '1'
                else:
                    if len(tmp) > 0:
                        tmp += '0'
            res.append(tmp)
        print(len(res))
        print(' '.join(res))



s = Solution()
s.readInput()
# s.readMockInput()
s.solve()