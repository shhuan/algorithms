# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-09 09:51

Rupsa最近在大厨手下实习，她把所有食材都放到一个罐子里面。
每次只能从罐子中取出一份食材，然后才知道类型，并且不放回。
当大厨要求她每种食材拿出两份的时候，最坏的情况下需要多少次才能把保证每种两份？

"""
__author__ = 'huash'

import sys
import os

sys.stdin = open('input/sampleA.txt', 'r')

T = int(input())
for ti in range(1, T + 1):

    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    if len(list(filter(lambda x: x < 2, A))) > 0:
        result = -1
    else:
        result = sum(A) - (min(A) - 2)

    print(result)