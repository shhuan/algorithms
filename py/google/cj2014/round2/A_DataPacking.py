# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-26 16:52


Adam花了很多时间把文件放在不同的磁盘上，每个磁盘的容量是X，
1. 每张磁盘上最多放两个文件
2. 每个文件只放在一个磁盘，文件大小一定小于磁盘大小

要求计算最少需要多少个磁盘



分析：

把文件按照大小排序之后，如果最小的文件和最大的文件可以放在一张盘上就放一张盘上，
否则最大的文件单独放一张盘，最小的文件在和最大的能放在一起的文件放在一张盘。

只有一个滑动窗口即可


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
        self.X = 0
        self.files = None

    def test(self):
        pass

    def readInput(self):
        self.N, self.X = [int(x) for x in input().split()]
        self.files = list(map(int, input().split()))

    def readMockInput(self):
        pass

    def solve(self):
        self.files.sort()

        l = 0
        r = len(self.files) - 1
        res = 0
        while l <= r:
            if l == r:
                res += 1
                break
            if self.files[l] + self.files[r] <= self.X:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1

        return res



startTime = datetime.datetime.now()

T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    res = solution.solve()
    print('Case #{}: {}'.format(ti, res))

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))