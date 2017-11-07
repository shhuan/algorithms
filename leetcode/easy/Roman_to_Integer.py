# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 17:54

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

"""
__author__ = 'huash'

import sys
import os


class Solution:
    # @return an integer
    def romanToInt(self, s):

        if not s:
            return 0

        vm = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '_': 0}

        count = 0
        pre_ch = '_'
        pre_count = 0
        for ch in s:
            if pre_ch == '_':
                pre_ch = ch
                pre_count = 1
                continue

            if ch != pre_ch:
                if vm[pre_ch] < vm[ch]:
                    count += vm[ch] - vm[pre_ch] * pre_count
                    pre_ch = '_'
                    pre_count = 0
                else:
                    count += vm[pre_ch] * pre_count
                    pre_ch = ch
                    pre_count = 1
            else:
                pre_count += 1
        count += vm[pre_ch]*pre_count
        return count


s = Solution()

print(s.romanToInt('XXXIII'))
# Ⅰ,1 】Ⅱ，2】 Ⅲ，3】 Ⅳ，4 】Ⅴ，5 】Ⅵ，6】Ⅶ，7】 Ⅷ，8 】Ⅸ，9 】
print(s.romanToInt('I'))
print(s.romanToInt('II'))
print(s.romanToInt('III'))
print(s.romanToInt('IIII'))
print(s.romanToInt('IV'))
print(s.romanToInt('V'))
print(s.romanToInt('VI'))
print(s.romanToInt('VII'))
print(s.romanToInt('VII'))
print(s.romanToInt('VIII'))
print(s.romanToInt('VIIII'))
print(s.romanToInt('X'))
print(s.romanToInt('IX'))
print(s.romanToInt('IIX'))
print(s.romanToInt('IIIX'))

print(s.romanToInt('MCM'))

print()
print(s.romanToInt('LXXX'))
print(s.romanToInt('XC'))
print(s.romanToInt('XCIII'))
print(s.romanToInt('XCVIII'))
print(s.romanToInt('XCIX'))
print(s.romanToInt('DCCC'))
print(s.romanToInt('CMXCIX'))
print(s.romanToInt('MMMCMXCIX'))
