# -*- coding: utf-8 -*-
"""
created by huash at 2016/6/18 19:11

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers.
Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.

Hint:

There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

"""
__author__ = 'huash'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 3:
            return max(0, n - 1)

        r = n % 3
        d = n // 3
        if r == 0:
            return self.p3(d)
        elif r == 2:
            return 2 * self.p3(d)
        else:
            return 4 * self.p3(d-1)

        return s

    def p3(self, i):
        if i == 0:
            return 1
        if i == 1:
            return 3
        d = self.p3(i // 2)
        if i & 1:
            return d * d * 3
        return d * d

    def integerBreak2(self, n):
        if n <= 3:
            return max(0, n - 1)

        r = n % 3
        d = n // 3
        if r == 0:
            return 3 ** d
        elif r == 2:
            return 2 * (3 ** d)
        else:
            return 4 * (3 ** (d-1))

    def integerBreak3(self, n):
        if n <= 3:
            return max(0, n - 1)

        r = n % 3
        d = n // 3
        if r == 0:
            return pow(3, d)
        elif r == 2:
            return 2 * pow(3, d)
        else:
            return 4 * pow(3, d-1)

    def integerBreak4(self, n):
        if n <= 3:
            return max(0, n - 1)

        r = n % 3
        d = n // 3

        return 3 ** d if r == 0 else (2 * (3 ** d) if r == 2 else 4 * (3 ** (d-1)))

def test(f):
    t0 = datetime.datetime.now()
    for i in range(20000):
        f(i)
    print("{} Cost: {}".format(f.func_name, datetime.datetime.now() - t0))

s = Solution()
test(s.integerBreak)
test(s.integerBreak3)
test(s.integerBreak2)
test(s.integerBreak4)

