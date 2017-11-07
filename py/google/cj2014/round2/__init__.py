# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-26 16:51
"""
__author__ = 'huash06'

import datetime
import sys

sys.stdin = open('input/-small-practice.in', 'r')
sys.stdout = open('output/A-small-practice.out', 'w')

# sys.stdin = open('input/A-large-practice.in', 'r')
# sys.stdout = open('output/A-large-practice.out', 'w')

class Solution:
    def __init__(self):
        pass

    def test(self):
        pass

    def readInput(self):
        pass

    def readMockInput(self):
        pass

    def solve(self):
        pass


startTime = datetime.datetime.now()

T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    res = solution.solve()
    print('Case #{}: {}'.format(ti, res))

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))