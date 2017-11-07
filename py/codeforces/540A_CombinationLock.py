# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-07 08:58

最少需要多少步可以打开组合锁

5
82195
64723

In the sample he needs 13 moves:

1 disk: 8->7->6
2 disk: 2->3->4
3 disk: 1->0->9->8->7
4 disk: 9->0->1->2
5 disk: 5->4->3

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