"""


"""

__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools


class Solution:
    # @param numerator, an integer
    # @param denominator, an integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if not denominator:
            return 'NAN'

        if numerator == 0:
            return '0'
        negative = False
        if numerator < 0:
            negative = not negative
            numerator = -numerator
        if denominator < 0:
            negative = not negative
            denominator = -denominator

        result = '' if not negative else '-'

        # 注意输出格式，要输出字符串，正负号，小数点，小数位数等
        if numerator > denominator:
            result += str(numerator // denominator)
            numerator %= denominator
        else:
            result += '0'
        numerator *= 10

        if numerator == 0:
            return result

        result += '.'
        rem = {}
        while True:
            # 先判断是为了处理余数是0的情况
            # 如果余数和之前的某个除数一样，是循环小数
            if numerator in rem:
                result = result[:rem[numerator]]+'('+result[rem[numerator]:]+')'
                break
            rem[numerator] = len(result)
            # print('{}/{} = {}, {}'.format(numerator, denominator, numerator//denominator, numerator%denominator))
            v = numerator // denominator
            r = numerator % denominator
            result += str(v)
            if r == 0:
                break
            numerator = r * 10

        return result

s = Solution()
print(s.fractionToDecimal(1, 2))
print(s.fractionToDecimal(2, 1))
print(s.fractionToDecimal(2, 3))
print(s.fractionToDecimal(1, 333))
print(s.fractionToDecimal(0, 3))
print(s.fractionToDecimal(-3, 932))
print(s.fractionToDecimal(21, -321))
print(s.fractionToDecimal(-121, -123))
print(s.fractionToDecimal(500, 10))