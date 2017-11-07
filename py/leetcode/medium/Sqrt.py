# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 13:32

Implement int sqrt(int x).

Compute and return the square root of x.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import math

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        """
        只要求返回整数解， 二叉查找即可
        :param x:
        :return:
        """
        if x < 0:
            return None
        elif x <= 1:
            return x

        left = 1
        right = x // 2 + 1
        if x > 10000:
            bits = 1
            cx = x
            while cx > 0:
                cx //= 10
                bits += 1
            left = 10 ** (bits // 2 - 1)
            right = left * 10

        while left < right:
            mid = left + (right - left) // 2
            mv = mid * mid
            if mv == x or mid == left:
                return mid
            elif mv > x:
                right = mid
            else:
                left = mid
        return left


    def sqrt(self, x):
        """
        平方根公式， 利用斜率计算
        X(k+1) = (X(k) + n/X(k)) / 2

        :param x:
        :return:
        """
        if x == 0:
            return 0
        elif x < 0:
            return None
        ret = 1
        for i in range(1000):
            ret = (ret + x/ret) / 2
        return ret


s = Solution()
for i in range(10):
    print('sqrt({}) = {}'.format(i, s.sqrt(i)))

for i in range(10000000, 10000010):
    print('sqrt({}) = {}'.format(i, s.mySqrt(i)))