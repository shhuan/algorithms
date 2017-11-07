# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-16 09:25


给定一个数字，把它写下来，如果它是偶数，除以二继续写，如果是奇数则停止。
给定两个数字，计算他们写下的相同的数字的个数。


分析：
通过一个数字最多写出的数字个数是它的二进制表示右端0的个数+1。
1. 如果两个数字去掉右端的0之后不相等，那么他们不会写出相同的数字
2. 否则写出的数字个数字是较小的0的个数+1

"""
__author__ = 'huash06'

import datetime
import sys
import random

class TaroJiroDividing:
    def getNumber(self, A, B):
        if A < B:
            A, B = B, A

        za, a = self.rightZeros(A)
        zb, b = self.rightZeros(B)
        if a == b:
            return min(za, zb) + 1
        else:
            return 0



    def rightZeros(self, num):
        count = 0
        while num & 1 == 0:
            count += 1
            num >>= 1
        return count, num


    def getNumber2(self, A, B):
        nums = {A}
        while A % 2 == 0:
            A /= 2
            nums.add(A)

        res = 1 if B in nums else 0
        while B % 2 == 0:
            B /= 2
            if B in nums:
                res += 1
        return res



s = TaroJiroDividing()
print(s.getNumber(8, 4))
print(s.getNumber(7, 4))
print(s.getNumber(12, 12))
print(s.getNumber(24, 96))
print(s.getNumber(1000000000, 999999999))
print(s.getNumber(12792, 12792))
print(s.getNumber2(12792, 12792))
for i in range(1000):
    A = random.randint(1, 100000)
    B = random.randint(1, 100000)
    if s.getNumber(A, B) != s.getNumber2(A, B):
        print('{}, {}'.format(A, B))