# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-11 19:11

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

"""
__author__ = 'huash'

import sys
import os


class Solution:
    # @return a string
    def countAndSay(self, n):
        if n < 1:
            return ''
        elif n == 1:
            return '1'
        next_str = '1'
        for ni in range(n-1):
            s = next_str
            next_str = ''
            pre = ''
            count = 0
            for ch in s:
                if pre == '':
                    pre = ch
                    count += 1
                elif ch == pre:
                    count += 1
                else:
                    next_str += str(count)
                    next_str += pre
                    pre = ch
                    count = 1
            next_str += str(count)
            next_str += pre
        return next_str


s = Solution()
for i in range(25):
    print('f({}) = {}'.format(i, s.countAndSay(i)))