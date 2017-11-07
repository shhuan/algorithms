# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-16 11:30

390分


给定一个右A，B，？组成的字符串S，
定义它的丑陋度为连续相同的字符对的数量。
the ugliness of "ABABAABBB" is 3: there is one pair "AA" and two (overlapping) pairs "BB"

给定一个S，Taro想让把每个？改成A或者B，使得它的丑陋度最小。
要求计算最小的丑陋度。



分析：
S的长度最多为50， 直接暴力枚举复杂度为2^50，明显不可能。
考虑动态规划，
设f(i, A)表示位置i是A时的丑陋度，f(i, B)表示位置i是B时的丑陋度。
如果第i位是？，
    f(i, A) = min{f(i-1,B), f(i-1,A)+1}
    f(i, B) = min{f(i-1,A), f(i-1,B)+1}
如果第i位是A，
    f(i, A) = min{f(i-1,B), f(i-1,A)+1}
    f(i, B) = maxint
如果第i位是B，
    f(i, A) = maxint
    f(i, B) = min{f(i-1,A), f(i-1,B)+1}

"""
__author__ = 'huash06'

import datetime
import sys


class TaroFillingAStringDiv2:
    def getNumber(self, S):

        f = [[0 for c in range(2)] for r in range(len(S))]

        for i, v in enumerate(S):
            if i == 0:
                if v == 'A':
                    f[i][0] = 0
                    f[i][1] = 10000000
                elif v == 'B':
                    f[i][0] = 10000000
                    f[i][1] = 0
                else:
                    f[i][0] = 0
                    f[i][1] = 0
                continue
            if v == 'A':
                f[i][0] = min(f[i-1][0]+1, f[i-1][1])
                f[i][1] = 10000000
            elif v == 'B':
                f[i][0] = 10000000
                f[i][1] = min(f[i-1][0], f[i-1][1]+1)
            else:
                f[i][0] = min(f[i-1][0]+1, f[i-1][1])
                f[i][1] = min(f[i-1][0], f[i-1][1]+1)

        return min(f[len(S)-1][0], f[len(S)-1][1])

s = TaroFillingAStringDiv2()
print(s.getNumber("ABAA"))
print(s.getNumber("??"))
print(s.getNumber("A?A"))
print(s.getNumber("A??B???AAB?A???A"))
print(s.getNumber("?BB?BAAB???BAB?B?AAAA?ABBA????A?AAB?BBA?A?"))
