# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 19:23

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        code = 0
        ans = [code]
        for r in range(n, -1, -1):
            for l in range(r):
                code |= 1 << (n - l - 1)

                if l > 0:
                    code ^= 1 << (n - l)
                ans.append(code)
        for c in ans:
            print("{0:{fill}13b}".format(c, fill='0'))
        return ans
    def grayCode1(self, n):
        if n < 0:
            return []
        elif n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        visited = {0}
        ret = [0]
        while True:
            num = ret[-1]
            nexts = self.nextNumbers(num, n)
            hasNext = False
            for v in nexts:
                if v not in visited:
                    visited.add(v)
                    ret.append(v)
                    hasNext = True
                    break
            if not hasNext:
                break
        return ret


    def nextNumbers(self, num, bits):
        ret = []
        for i in range(bits):
            v = num ^ ((num | (1 << i)) & (1 << i))
            ret.append(v)
        # print('nexts({},{}) = {}'.format(num, bits, ret))
        return ret



s = Solution()

# print(s.nextNumbers(0, 2))
print(s.grayCode(13))