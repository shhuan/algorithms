# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 11:22

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.


罗马数字共有7个，即I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）
1、相同的数字连写，所表示的数等于这些数字相加得到的数，如：Ⅲ = 3；
2、小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数， 如：Ⅷ = 8；Ⅻ = 12；
3、小的数字，（限于Ⅰ、X 和C）在大的数字的左边，所表示的数等于大数减小数得到的数，如：Ⅳ= 4；Ⅸ= 9；
4、正常使用时，连写的数字重复不得超过三次。（表盘上的四点钟“IIII”例外）
5、在一个数的上面画一条横线，表示这个数扩大1000倍。
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import random
class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        if num <= 0:
            return ''

        ret = ''
        if num > 1000:
            ret += 'M' * (num//1000)
            num %= 1000

        if num >= 900:
            ret += 'C' * (10 - num//100)
            ret += 'M'
            num %= 100
        elif num >= 500:
            ret += 'D'
            num -= 500
        if num >= 400:
            ret += 'C' * (5 - num//100)
            ret += 'D'
            num %= 100
        elif num >= 100:
            ret += 'C' * (num//100)
            num %= 100
        if num >= 90:
            ret += 'X' * (10 - num//10)
            ret += 'C'
            num %= 10
        elif num >= 50:
            ret += 'L'
            num -= 50
        if num >= 40:
            ret += 'X' * (5 - num//10)
            ret += 'L'
            num %= 10
        elif num >= 10:
            ret += 'X' * (num//10)
            num %= 10
        if num >= 9:
            ret += 'I' * (10-num)
            ret += 'X'
            num = 0
        elif num >= 5:
            ret += 'V'
            num -= 5
        if num >= 4:
            ret += 'I' * (5-num)
            ret += 'V'
            num = 0
        elif num > 0:
            ret += 'I' * num
        return ret




s = Solution()

s.intToRoman(800)
for i in range(20):
    # v = random.randint(1, 3999)
    v = i
    print('{} = {}'.format(v, s.intToRoman(v)))

for i in range(1, 11):
    # v = random.randint(1, 3999)
    v = i*10
    print('{} = {}'.format(v, s.intToRoman(v)))

for i in range(1, 11):
    # v = random.randint(1, 3999)
    v = i*100
    print('{} = {}'.format(v, s.intToRoman(v)))

for i in range(1, 4):
    # v = random.randint(1, 3999)
    v = i*1000
    print('{} = {}'.format(v, s.intToRoman(v)))
