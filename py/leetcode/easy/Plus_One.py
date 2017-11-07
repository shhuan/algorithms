# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 15:41

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

"""
__author__ = 'huash06'

import sys
import os

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return ''

        result = [' ']*(len(digits)+1)
        ri = len(digits)
        car = 1
        for i in range(len(digits)-1, -1, -1):
            v = int(digits[i])+car
            result[ri] = v % 10
            car = v // 10
            ri -= 1
        if car > 0:
            result[ri] = car
            ri -= 1
        return result[ri+1:]

s =Solution()
print(s.plusOne([1, 0]))
print(s.plusOne(''))
print(s.plusOne('999'))
print(s.plusOne('123'))