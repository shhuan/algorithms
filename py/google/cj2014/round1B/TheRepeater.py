# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-08 14:00
"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

sys.stdin = open('input/sample.txt', 'r')

sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-large-practice.out', 'w')

MAXNN = 301
T = int(sys.stdin.readline())

for ti in range(1, T + 1):
    N = int(sys.stdin.readline())
    strs = list()
    for i in range(N):
        strs.append(map(list, sys.stdin.readline().strip()))

    # 把所有字符串記錄成wc=[[c1, i1], [c2, ic], [c3, i3], ... , [in, cn]]的形式
    # 表示字符串按順序是由i1個字符c1,...,in個字符cn組成
    # 如果所有字符串都能轉換成一樣的字符串，必要條件是是他們的這種表示除了數字不一樣其他部分是一樣的。
    #
    wc = list()
    l = -1
    invalid = False
    for s in strs:
        fl = list()
        for i in s:
            if len(fl) <= 0 or fl[-1][0] != i:
                fl.append([i, 1])
            else:
                fl[-1][1] += 1
        wc.append(fl)
        if l < 0:
            l = len(fl)
        else:
            if l != len(fl):
                invalid = True
                break
    if invalid:
        print('Case #{}: Fegla Won'.format(ti))
        continue
    # for each string, change the ith character wi to k same wi, [wi]*k and record the changes op_count.
    # op_count[wi] = min{change(j, k)} 0<=j<N, min{count(j,wi)}<=k<=max{count(j, wi)}
    # change(j,k) is the count of changes needed to change the ith character wi of jth string to [wi]*k
    # count(j, wi) is the count of wi in the jth string
    # finally, op_count = sum{op_count[i]}
    op_count = 0
    for i in range(l):
        w = wc[0][i][0]
        cc = list()
        cc.append(wc[0][i][1])
        for r in range(1, len(wc)):
            s = wc[r][i][0]
            cc.append(wc[r][i][1])
            if s != w:
                invalid = True
                break
        if invalid:
            break

        # change the ith character wi to wc*k,
        # and select the k leads to minimus changes
        tc = sys.maxint
        for v in range(min(cc), max(cc)+1):
            tcc = 0
            for c in cc:
                tcc += abs(c-v)
            if tcc < tc:
                tc = tcc
        op_count += tc

    if invalid:
        print('Case #{}: Fegla Won'.format(ti))
        continue
    else:
        print('Case #{}: {}'.format(ti, op_count))