# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 20:07


Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.


if ab > ba, then place a before be

"""

__author__ = 'huash06'

import sys
import os


class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if not num:
            return ''

        num = sorted(num, cmp=lambda x, y: int(str(y)+str(x)) - int(str(x)+str(y)))

        result = ''.join(list(map(str, num)))
        if result.startswith('0'):
            i = 0
            for j in range(len(result)):
                if result[j] != '0':
                    break
                i = j
            if i == len(num) - 1:
                result = '0'
            else:
                result = result[i:]

        return result

s = Solution()
print(s.largestNumber((3, 30, 34, 5, 9)))

print(s.largestNumber((0, 0)))