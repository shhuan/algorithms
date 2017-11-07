# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-09 13:27
"""
__author__ = 'huash06'

import sys
import os
import math
from fractions import gcd

def is_power_of_two(x):
  return x & (x - 1) == 0

def min_generation(P, Q):
    """
    1st gen:  0/1                                     1/1
    2nd gen:  0/2                 1/2                 2/2
    3rd gen:  0/4       1/4       2/4       3/4       4/4
    4th gen:  0/8  1/8  2/8  3/8  4/8  5/8  6/8  7/8  8/8

    1. 第i代的分母是2^i，分子是[0,i]
    2. a P/Q Elf could have a Z/Q parent where Z is ranged from max(0, P - (Q-P)) to min(Q, P * 2).
        即生成P/Q的父母最大的是2*P/Q，如下等式所示
        (0/8 + 6/8) / 2 = 3/8
        (1/8 + 5/8) / 2 = 3/8
        (2/8 + 4/8) / 2 = 3/8
        (3/8 + 3/8) / 2 = 3/8
    3. 只要滿足條件1 且 P/Q >= 1/2， P/Q就能通過1/1和另外一個字節生產
    4. 為了最快找到1/1，每個P/Q都找他的最大父母2*P/Q。
        f(P, Q) = f(2*, Q)， f(P, Q)==1 if P/Q>=1/2


    :param P:
    :param Q:
    :return:
    """
    g = gcd(P, Q)
    P = P // g
    Q = Q // g

    if not (is_power_of_two(Q)):
        return "impossible"

    gen = 0
    while P < Q:
        P = P * 2
        gen += 1
    return gen


sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-large-practice-p.out', 'w')

for tc in range(int(input())):
  print("Case #%d: %s" % (tc+1, \
    min_generation(*map(int, input().split('/')))))
