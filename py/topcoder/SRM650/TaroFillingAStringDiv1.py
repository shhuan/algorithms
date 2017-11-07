# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-17 11:17

Problem Statement
Cat Taro likes strings. He is currently constructing a string S of length N.
Each character of S will be either 'A' or 'B'.

Taro has already chosen some of the characters.
You are given these choices as a position and a value.
For each valid i, the character at the 1-based index position[i] in S is the character value[i].

To Taro, the ugliness of a string is the number of pairs of equal consecutive characters.
For example, the ugliness of "ABABAABBB" is 3: there is one pair "AA" and two (overlapping) pairs "BB".


Taro now wants to finish S by filling in the remaining characters.
His goal is to create a string with the smallest possible ugliness.
Let X be the number of possible strings Taro may produce. Return the value (X modulo 1,000,000,007).



Limits
Time limit (s): 2.000
Memory limit (MB): 256

Constraints
- N will be between 1 and 1,000,000,000, inclusive.
- position will contian between 1 and 50 elements, inclusive.
- value and position will contain the same number of elements.
- Each element of position will be between 1 and N, inclusive.
- All elements of position will be distinct.
- value will consist only of characters 'A' and 'B'.


分析：

1. 如果改变问号的值之后增加的丑陋度为0， 那么这一段只有一种填充方式。
  比如，A????B，只能填入BABA得到ABABAB。
  进一步分析，i,[?]*n,j位置i和位置j之间有n个？，i和j的值已知。
  如果i和j的值一样，那么当n是奇数的时候，能够使得增加的丑陋度为1，即只有一种填充方式。
  同样i和j的值不一样，且n是偶数的时候，也只有一种填充方式。
2. i和j的值一样，但是n是偶数的时候，例如A??????A， 有如下填充方式：
        ABABABAA
        ABABABBA
        ABABAABA
        ABABBABA
        ABAABABA
        ABBABABA
        AABABABA
    使得只有一个重复字符串，即增加的丑陋度为1。由于重复字符串的位置有n+1个，所以有n+1
    种填充方式。

3. i和j的值不一样，且n是奇数的时候同2，也是n+1种填充方式

"""
__author__ = 'huash06'

import datetime
import sys


class TaroFillingAStringDiv1:
    def getNumber(self, N, position, value):

        # print(list(zip(position, value)))
        # print(*zip(position, value))
        # print(*sorted(zip(position, value)))
        # print(list(zip(*sorted(zip(position, value)))))

        position, value = zip(*sorted(zip(position, value)))

        r = 1
        MOD = 1000000007
        for i in range(1, len(position)):
            same = 1 if value[i] == value[i-1] else 0
            r *= self.coutBridges(position[i]-position[i-1]-1, same)
            r %= MOD
        return r


    def coutBridges(self, n, same):
        return 1 if (n % 2 == same) else n+1



s = TaroFillingAStringDiv1()
print(s.getNumber(3, [1, 3], 'AB'))
print(s.getNumber(4, [2, 1, 3, 4], 'ABBA'))
print(s.getNumber(25, [23, 4, 8, 1, 24, 9, 16, 17, 6, 2, 25, 15, 14, 7, 13], "ABBBBABABBAAABA"))
print(s.getNumber(305, [183, 115, 250, 1, 188, 193, 163, 221, 144, 191, 92, 192, 58, 215, 157, 187, 227,
                        177, 206, 15, 272, 232, 49, 11, 178, 59, 189, 246], "ABAABBABBAABABBBBAAAABBABBBA"))