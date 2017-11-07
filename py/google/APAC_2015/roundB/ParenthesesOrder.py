# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-06 11:09
"""
__author__ = 'huash'

import sys
import os
import py.lib.Utils as Utils

sys.stdin = open('input/D-large-practice.in', 'r')
sys.stdout = open('output/D-large-practice.out', 'w')

reader = Utils.Reader()
reader.read()

MAXN = 101

# 设F[l]][r]表示有l个左括号，r个右括号形成的合法前缀的数量，
# 设G[l][r]表示有l个左括号，r个右括号形成的合法后缀的数量，
# 根据对称性，G[l][r] == F[r][l]
# F[l][r] = F[l-1][r] + F[l][r-1]，即第一个分别使用左右括号时候的组合数之和
F = [[0 for col in range(MAXN)] for row in range(MAXN)]
F[0][0] = 1
for i in range(1, MAXN):
    F[i][0] = 1
    for j in range(1, i+1):
        F[i][j] = F[i-1][j]+F[i][j-1]


def get_kth(n, k):
    res = ""

    # l,r分别是已经使用的左右括号的数量
    l = 0
    r = 0

    # 如果k大于括号的组合数
    if k > F[n][n]:
        return "Doesn't Exist!"

    while len(res) < 2*n:
        # 如果写右括号会使得数量超过k
        if k <= F[n-r][n-l-1] and l < n:
            res += '('
            l += 1
        # 写右括号，排除了所有当前使用左括号时的组合数量，所以k-=f
        elif l < n:
            res += ')'
            k -= F[n-r][n-l-1]
            r += 1
        else:
            res += ')'
            r += 1

    return res


T = reader.next_int()
for ti in range(1, T+1):
    N = reader.next_int()
    K = reader.next_int()
    print('Case #{}: {}'.format(ti, get_kth(N, K)))
