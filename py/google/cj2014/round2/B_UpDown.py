# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-26 17:20


给一个数组，问最少需要几次交换让它变成一个先递增后递减的序列。


使用贪心算法，每次找一个最小的数字把他交换到最边上。
因为最终结果最小的数字一定是在最边上，所以贪心策略是正确的，
交换之后最小的数字不会再移动，把他移除。

"""
__author__ = 'huash06'

import datetime
import sys

# sys.stdin = open('input/B-small-practice.in', 'r')
# sys.stdout = open('output/B-small-practice.out', 'w')

sys.stdin = open('input/B-large-practice.in', 'r')
sys.stdout = open('output/B-large-practice.out', 'w')

class Solution:
    def __init__(self):
        self.N = 0
        self.nums = None

    def test(self):
        pass

    def readInput(self):
        self.N = int(input())
        self.nums = list(map(int, input().split()))

    def readMockInput(self):
        pass

    def solve(self):

        left = 0
        right = len(self.nums) - 1
        res = 0
        while left < right:
            mi = left + self.nums[left: right+1].index(min(self.nums[left: right+1]))
            if mi - left < right - mi:
                res += mi - left
                tmp = self.nums[mi]
                for i in range(mi, left, -1):
                    self.nums[i] = self.nums[i-1]
                self.nums[left] = tmp
                left += 1
            else:
                res += right - mi
                tmp = self.nums[mi]
                for i in range(mi, right):
                    self.nums[i] = self.nums[i+1]
                self.nums[right] = tmp
                right -= 1
        return res
            



startTime = datetime.datetime.now()

T = int(input())
for ti in range(1, T + 1):
    solution = Solution()
    solution.readInput()
    res = solution.solve()
    print('Case #{}: {}'.format(ti, res))
    sys.stderr.write("{}, {}\n".format(solution.nums, res))

sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now() - startTime))