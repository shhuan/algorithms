# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 08:21


Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB


注意这个和普通的进制转换有些区别是他的数字是1-N，
所以如果余数是0的时候需要高位减1，本位取N

"""
__author__ = 'huash'

import sys
import os



class Solution:
    # @return a string
    def convertToTitle(self, num):

        if num <= 0:
            return ''

        result = ''
        while num >= 26:
            r = num % 26
            num //= 26
            if r == 0:
                # 余数是0， 高位减1，本位取N
                num -= 1
                result += 'Z'
            else:
                result += chr(r + ord('A') - 1)
        if num > 0:
            result += chr(num+ord('A')-1)
        return ''.join(list(reversed(result)))



s = Solution()

print(s.convertToTitle(52))
for i in range(1000):
    print(s.convertToTitle(i))