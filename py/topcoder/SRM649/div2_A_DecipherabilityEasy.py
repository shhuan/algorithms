# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-17 16:44

字符串t是否可能是字符串s去掉一个字符之后的结果。

"""
__author__ = 'huash06'

import datetime
import sys


class DecipherabilityEasy:
    def check(self, s, t):

        for i in range(len(s)):
            # print(''.join(s[:i] + s[i+1:]))
            if ''.join(s[:i] + s[i+1:]) == t:
                return "Possible"

        return "Impossible"



s = DecipherabilityEasy()
print(s.check("sunuke", 'snuke'))



