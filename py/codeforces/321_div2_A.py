# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-15 09:14


Amr 从坐标0开始往左或者有走，遇到一颗苹果树就采掉上面的所有苹果，
然后掉头，遇到苹果树在采。

问Amr最多能够采集到多少苹果。

Sample test(s)
    input
        2     # 苹果树的数量
        -1 5  # 每个苹果树的坐标和上面的苹果的数量
        1 5
    output
        10

    input
        3
        -2 2
        1 4
        -1 3
    output
        9

    input
        3
        1 9
        3 5
        7 10
    output
        9

分析：
把苹果树分为坐标大于0和小于0两个部分，数量少的那边肯定全部被采集完，多的那边最多比少的那边多采集一个树。
如果数量相等，全部都能采到

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


def collectApple(tree):
    if not tree:
        return 0
    left = sorted(filter(lambda x: x[0] < 0, tree))
    right = sorted(filter(lambda x: x[0] > 0, tree))

    res = 0
    if len(left) > len(right):
        res += sum([x[1] for x in right])
        res += sum([x[1] for x in left[len(left) - len(right) - 1:]])
    else:
        res += sum([x[1] for x in left])
        res += sum([x[1] for x in right[:min(len(left) + 1, len(right))]])
    return res


N = int(input())

tree = []
for i in range(N):
    tree.append([int(x) for x in input().split()])
print(collectApple(tree))