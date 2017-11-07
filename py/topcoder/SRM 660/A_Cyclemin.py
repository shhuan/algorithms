# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-11 17:09
"""
__author__ = 'huash06'

import datetime
import sys

class Cyclemin:
    def bestmod(self, s, k):
        result = ''
        for i in range(len(s)):
            cyclic = list(s[i:]) + list(s[:i])
            ck = 0
            for j in range(len(s)):
                if ck >= k:
                    break
                if cyclic[j] > 'a':
                    cyclic[j] = 'a'
                    ck += 1
            cyclic = ''.join(cyclic)
            if not result or result > cyclic:
                result = cyclic
        return result

s = Cyclemin()
print(s.bestmod('aba', 1))
