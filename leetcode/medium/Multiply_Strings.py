
# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 14:50

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if not num1 or not num2:
            return None

        negative = False
        if num1.startswith('-'):
            negative = not negative
            num1 = num1[1:]
        if num2.startswith('-'):
            negative = not negative
            num2 = num2[1:]

        if num1.startswith('0') or num2.startswith('0'):
            return '0'

        car = 0

        i1 = len(num1)-1
        i2 = len(num2)-1
        ret = [0] * (len(num1) + len(num2))

        for i in range(len(num2)-1, -1, -1):
            k = len(ret) - (len(num2) - i)
            car = 0
            for j in range(len(num1)-1, -1, -1):
                v = int(num2[i]) * int(num1[j])
                v += car + ret[k]
                ret[k] = v % 10
                car = v // 10
                k -= 1
            ret[k] = car
            # print(ret)
        if ret[0] == 0:
            ret = ''.join(map(str, ret[1:]))
        else:
            ret = ''.join(map(str, ret))
        if negative:
            ret = '-' + ret
        return ret


s = Solution()
print(s.multiply('12345', '-21'))
print(s.multiply('0', '-123'))
print(s.multiply('231', '231'))
print(s.multiply('-12', '-232'))
print(s.multiply('9', '9'))
print(s.multiply('0', '0'))