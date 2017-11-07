# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-04 16:56

有一组卡牌，每次从中拿掉三个a,b,c满足如下条件
    c-b == b-a == c
    1. a,b,c是卡牌上的数字
    2. a,b,c所在的卡牌相邻
问最后最少剩下多少张卡牌

经典动态规划问题

"""
__author__ = 'huash'

import sys
import os
import py.lib.Utils as Utils

sys.stdin = open('input/C-large-practice.in', 'r')
# sys.stdin = open('input/sample.txt', 'r')

sys.stdout = open('output/C-large-practice-p.out', 'w')

MAXN = 101

reader = Utils.Reader()
reader.read()
T = reader.next_int()

for ti in range(1, T + 1):
    N = reader.next_int()
    K = reader.next_int()
    A = [0] * N
    for i in range(N):
        A[i] = reader.next_int()

    F = [[False for col in range(N)] for row in range(N)]

    # F[i][j]==True表示数字A[i:j]之间的全部数字都可以拿掉，F[i][j]==False, if j-i<2
    # 有以下几种情况F[i][j]=True
    # 1. 如果j-i==2 而且A[i], A[i+1], A[i+2] 之间的差值等于K
    # 2. A[i], A[k], A[j] 之间的差值等于K，且F[i+1][k-1]==F[k+1][j-1]==True
    #    如果k==i+1, F[k+1][j-1]==True 即可
    #    如果k==j-1, F[i+1][k-1]==True 即可
    #    如果k==i+1==j-1, 就是情况1, 即情况1可以包含在情况2中
    # 3. F[i][k]==F[k+1][j]==True

    # gap<3已经求出
    for gap in range(2, N):
        # i+gap<N ==> i<N-gap
        for i in range(N - gap):
            j = i + gap
            if F[i][j]:
                continue

            for k in range(i+1, j):
                if A[k]-A[i] == K and A[j]-A[k] == K:
                    if k == i+1 or F[i+1][k-1]:
                        if k == j-1 or F[k+1][j-1]:
                            F[i][j] = True
                            break

            if not F[i][j]:
                # F[i][k] equal True if only k>=i+2
                # F[k][j] equal True if only k<=j-2
                for k in range(i + 2, j-1):
                    if F[i][k] and F[k + 1][j]:
                        F[i][j] = True
                        break

    # G[i]表示前i+1个数字最少剩下几个，
    # G[i] = min{G[i-1]+1, min{G[j], F[j][i]==True}}
    G = [0] * N
    G[0] = 1
    G[1] = 2
    for i in range(2, N):
        if F[0][i]:
            G[i] = 0
            continue
        g = G[i - 1] + 1
        for j in range(1, i):
            if F[j][i] and G[j-1] < g:
                g = G[j - 1]
        G[i] = g

    print('Case #%d: %d' % (ti, G[N - 1]))


