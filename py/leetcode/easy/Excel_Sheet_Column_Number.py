# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 07:59

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""
__author__ = 'huash'

import sys
import os


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):

        result = 0
        for ch in s:
            v = ord(ch) - ord('A') + 1
            result *= 26
            result += v
        return result


s = Solution()
print(ord('D') - ord('A'))
print(s.titleToNumber('A'))
print(s.titleToNumber('EA'))
print(s.titleToNumber('AA'))
print(s.titleToNumber('Z'))