# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-11 23:51

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.


"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 'MAX_INT'

        negative = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif divisor < 0:
                divisor = -divisor
                negative = True
        elif dividend < 0:
                negative = True
                dividend = -dividend

        result = 0
        while dividend > 0:
            d = divisor
            r = 1
            while d < dividend:
                d <<= 1
                r <<= 1
            if d > dividend:
                r >>= 1
                d >>= 1
            if result > 2147483647 - r:
                return 2147483647
            result += r
            dividend -= d
        if negative:
            return -result
        return result

s = Solution()
print(s.divide(1, 1))

print(s.divide(0, 1))
print(s.divide(-22, -2))
print(s.divide(-22, 3))

print(s.divide(22, -4))

print(s.divide(2, 5))
print(s.divide(22, 134))
print(s.divide(122, 134))
print(s.divide(23, 4))


print(s.divide(0, 4))
print(s.divide(-32147483648, -1))