# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 15:03

Implement pow(x, n).

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n == 2:
            return x*x

        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x



s = Solution()
print(s.myPow(2, 3))
print(s.myPow(2, -3))
print(s.myPow(5.123, 10))