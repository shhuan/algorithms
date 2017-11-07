# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-08 08:49


3位颜色，每位的值是[0,K]，如果任意两位之间的差值小于V，我们就说这个颜色是黑色。
对于给定的K和V，计算有多少种黑色

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

sys.stdin = open('input/sampleB.txt', 'r')
sys.stdin = open('input/B-small-practice.in', 'r')
sys.stdout = open('output/B-small-practice.out', 'w')

sys.stdin = open('input/B-large-practice-2.in', 'r')
sys.stdout = open('output/B-large-practice-2.out', 'w')

__DEBUG__ = True

MAXNN = 301

def solve(K, V):
    result = 0
    if V == 0:
        result = K + 1
    elif K >= 0 and V >= 0:
        for r in range(K+1):
            for g in range(max(0, r-V), min(r+V, K)+1):
                for c in range(max(0, r-V, g-V), min(r+V, g+V, K)+1):
                    result += 1
    return result

def solve2(K, V):
    """
    As is often the case in programming contests, the specified limits provide a clue.
    There’s no way to iterate over 2 billion values in time, so there must be a formulaic element to the answer.
    Indeed, if you look at the numbers of valid values beginning with each possible value for R, a pattern emerges.
    For example, consider this data for K = 10, V = 3:

    R	            0	1	2	3	4	5	6	7	8	9	10
    Valid colors 	16 	23 	30 	37 	37 	37 	37 	37 	30 	23 	16

    合法数量是 先递增，然后不增不减，然后递减

    R取中间的值和去两边的值的时候，合法数量是一样的

    :param K:
    :param V:
    :return:
    """
    result = 0
    if V <= K - V:
        # 如果[r-v, r+v]属於[0, k]，即r属於[v, k-v]，r的所有取值都能产生一样数量的解
        tmpCount = 0
        r = V
        for g in range(r-V, r+V+1):
            b = min(g+V, r+V) - max(0, g-V) + 1
            tmpCount += b
        result = tmpCount * (K - 2*V + 1)

        # *2是因为r属於[0, v-1] 和 r属於[k-v+1, k+1]两种情况对称的
        for r in range(V):
            for g in range(max(0, r-V), min(r+V, K)+1):
                bmax = min(r+V, g+V, K)
                bmin = max(0, r-V, g-V)
                result += 2*(bmax - bmin + 1)
    else:
        # 如果[v, k-v]是空集，r属於[0, K]
        # result = pow(K+1, 3)
        for r in range(K // 2 + 1):
            for g in range(max(0, r-V), min(r+V, K)+1):
                bmax = min(r+V, g+V, K)
                bmin = max(0, r-V, g-V)
                if r == K//2 and K % 2 == 0:
                    result += (bmax-bmin+1)
                else:
                    result += 2*(bmax-bmin+1)
    return result

def solve3(K, V):
    """
    在solve2的基础上， 其实我们直接计算r从0到V时候的值，
    然后V时候的值就是中间重复的值。

    :param K:
    :param V:
    :return:
    """
    result = 0
    for r in range(V+1):
        count = 0
        for g in range(max(0, r-V), min(r+V, K)+1):
            bmax = min(r+V, g+V, K)
            bmin = max(0, r-V, g-V)
            count = bmax - bmin - 1
        if r == V:
            result *= 2 # 前面r取[0, V-]时候的数量和后面对称
            result += count * (K-2*V+1) # 中间部分
        else:
            result += count
    return result





T = int(input())
for ti in range(1, T + 1):
    K, V = (int(v) for v in input().split(' '))
    print('Case #{}: {}'.format(ti, solve3(K, V)))

# solve(2, 0)