# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-14 14:56
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import copy

sys.stdin = open('input/sampleF.txt', 'r')
sys.stdout = open('output/sampleF-2.txt', 'w')

MOD = 1000000007
def mul(a, b):
    return (a * b) % MOD


T = int(input())
for ti in range(1, T + 1):

    N, K = (int(v) for v in input().split(' '))

    POW = [0] * (N+1)
    POW[0] = 1
    for i in range(1, N+1):
        POW[i] = (POW[i-1] * K) % MOD
    # print(POW)
    count = 0
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            amb = mul(POW[a], POW[b]-POW[b-a])
            amb = mul(amb, 6)
            for c in range(b+1, N+1):
                # tmp = (((((POW[a] * (POW[b] - POW[b-a])) % MOD) * (POW[c] - POW[c-b] - POW[c-a]) % MOD) % MOD) * 6) % MOD
                # tmp = mul(POW[a], POW[b]-POW[b-a])
                tmp = mul(amb, POW[c]-POW[c-b]-POW[c-a])
                # tmp = mul(tmp, 6)
                # print('{},{},{} = {}'.format(a, b, c, tmp))
                count += tmp
                count %= MOD
    # print('a<b<c: {}'.format(count))
    for a in range(1, N+1):
        b = a
        amb = mul(POW[a], POW[a]-1)
        amb = mul(amb, 3)
        for c in range(b+1, N+1):
            # count += (((((POW[a] * (POW[b] - POW[b-a])) % MOD) * (POW[c] - (2*POW[c-a]) % MOD)) % MOD) * 3) % MOD
            # tmp = mul(POW[a], POW[b]-POW[b-a])
            tmp = mul(amb, POW[c]-2*POW[c-a])
            # tmp = mul(tmp, 3)
            count += tmp
            count %= MOD
    # print('a=b<c: {}'.format(count))
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            c = b
            # count += (((((POW[a] * (POW[b]-POW[b-a])) % MOD) * (POW[c] - POW[c-a] - 1)) % MOD) * 3) % MOD
            tmp = mul(POW[a], POW[b]-POW[b-a])
            tmp = mul(tmp, POW[c]-POW[c-a]-1)
            tmp = mul(tmp, 3)
            count += tmp
            count %= MOD
    # print('a<b=c: {}'.format(count))
    for a in range(1, N+1):
        b = a
        c = a
        # count += (((POW[a] * (POW[b] - 1)) % MOD) * (POW[c] - 2)) % MOD
        tmp = mul(POW[a], POW[b]-1)
        tmp = mul(tmp, POW[c]-2)
        count += tmp
        count %= MOD
    # print('a=b=c: {}'.format(count))
    print(count)


