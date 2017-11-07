# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 13:34


失配时，模式串向右移动的位数为：失配字符所在位置 - 失配字符对应的next 值


"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


def getNext(pattern):
    """
    返回Next数组
    :param pattern:
    :return: next
    """

    plen = len(pattern)
    nextArr = [0] * plen
    nextArr[0] = -1
    k = -1
    j = 0
    while j < plen-1:
        # p[k]表示前缀, p[j]表示后缀
        if k == -1 or pattern[j] == pattern[k]:
            k += 1
            j += 1
            nextArr[j] = k
        else:
            k = nextArr[k]
    return nextArr

def kmp(astr, pattern):
    if not astr or not pattern:
        return -1
    slen = len(astr)
    plen = len(pattern)
    nextArr = getNext(pattern)
    i = 0
    j = 0
    while i < slen and j < plen:
        if j == -1 or astr[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = nextArr[j]
    if j == plen:
        return i - j
    return -1


print(kmp('abacababc', 'abab'))
print(kmp('', 'aba'))
print(kmp('abc', ''))