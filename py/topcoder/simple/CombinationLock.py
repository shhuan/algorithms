# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-07 08:58
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


digits = int(input())
start = input()
end = input()

res = 0
for i in range(digits):
    ei = int(end[i])
    si = int(start[i])
    res += min(abs(ei-si), ei+si, si+10-ei, 10-si+ei)

print(res)