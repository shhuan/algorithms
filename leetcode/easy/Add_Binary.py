# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 15:28

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""
__author__ = 'huash06'

import sys
import os


class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if not a:
            return b
        if not b:
            return a

        car = 0
        la = len(a)
        lb = len(b)
        result = ''
        for i in range(min(la, lb)):
            ia = la-i-1
            ib = lb-i-1
            v = int(a[ia]) + int(b[ib]) + car
            result = str(v % 2) + result
            car = v // 2
        print(result)
        r = a if la > lb else b
        for i in range(abs(la-lb)-1, -1, -1):
            v = int(r[i]) + car
            result = str(v % 2) + result
            car = v // 2
        if car > 0:
            result = '1' + result
        return result

s = Solution()
a = '11'
b = '1'
print(s.addBinary(a, b))

print(s.addBinary("100", "110010"))
