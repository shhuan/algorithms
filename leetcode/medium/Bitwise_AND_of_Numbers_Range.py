# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 10:22

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        if m > n:
            return 0
        if m == n:
            return m

        # m和n最左边都是1的部分就是结果
        # The idea is to use a mask to find the leftmost common digits of all 1's for m and n.
        # Example: m=1110001, n=1110111, and you just need to find 1110000 and it will be the answer.
        mask = (1 << 32)-1
        while (m & mask) != (n & mask):
            mask <<= 1
        return m & mask




s = Solution()
print(s.rangeBitwiseAnd(5, 7))
print(s.rangeBitwiseAnd(3, 1000))
print(s.rangeBitwiseAnd(0, 2147483647))
print(s.rangeBitwiseAnd(600000000, 2147483645))