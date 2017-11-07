# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-14 14:56


C(m,k)=m!/(k!*(m-k)!)    对C(m,k)取模mod

取模运算规则：

(a + b) % p = (a % p + b % p) % p （1）
(a - b) % p = (a % p - b % p) % p （2）
(a * b) % p = (a % p * b % p) % p （3）
a ^ b % p = ((a % p)^b) % p （4）
在求 m!/(k!*(m-k)!)的时候由于有除法不能像以上那样一步取模一次，因此我们想到了用费马小定理把分母转化成整数再用第三条求模。



费马小定理：假如a是整数，p是质数，且a,p互质，那么a的(p-1)次方除以p的余数恒等于1。

                 那么a^(p-1)/a = 1/a%p 得到1/a%p= a^(p-2) ,  将一个分数的值化成了整数

  因此在求以上令a=k!*(m-k)!   ,   p=mod(即mod=1000000009)，

  1/(k!*(m-k)!)  %mod= (k!*(m-k)!)^(mod-2)

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import copy

sys.stdin = open('input/sampleF-gen.txt', 'r')
sys.stdout = open('output/sampleF-opt-2.txt', 'w')
sys.stderr = open('output/smapleF-debug-opt-2.txt', 'w')


MOD = 1000000007
def mul(a, b):
    return (a * b) % MOD

def sub(a, b):
    return (a-b+MOD) % MOD

def denoMod(a):
    # return (1/a) % MOD
    return powMod(a, MOD-2)

@functools.lru_cache(maxsize=None)
def powMod(a, b):

    if b == 0:
        return 1
    elif b == 1:
        return a

    hlf = powMod(a, b//2)

    if b & 1 == 0:
        return (hlf * hlf) % MOD
    else:
        return (((hlf * hlf) % MOD) * a) % MOD

def divMod(a, b):
    pass

T = int(input())
for ti in range(1, T + 1):

    N, K = (int(v) for v in input().split(' '))

    POW = [0] * (2*N+1)
    POW[0] = 1
    for i in range(1, 2*N+1):
        POW[i] = (POW[i-1] * K) % MOD
    # print(POW)
    count = 0
    for a in range(1, N-1):

        n = N-a-1
        ga = sub(n*POW[N+1], mul(mul(POW[a+2], POW[n]-1), denoMod(K-1)))
        ga = mul(mul(POW[a]-1, ga), denoMod(K-1))
        ha = sub(mul(POW[N+1], mul(mul(POW[a+1], POW[n]-1), denoMod(K-1))), mul(mul(POW[2*a+3], POW[2*n]-1), denoMod(POW[2]-1)))
        ha = mul(mul(POW[2*a]-2*POW[a]+1, ha), denoMod(mul(POW[a], K-1)))

        fa = ga + ha
        fa = mul(fa, 6)
        count += fa
        count %= MOD

        # for b in range(a+1, N):
        #     tmp = POW[a+b] - ((2*POW[b]) % MOD) - POW[a] + 1 + POW[b-a]
        #     tmp %= MOD
        #     segc = mul(POW[b+1], POW[N-b] - 1)
        #     segc = mul(segc, powMod(K-1, MOD-2))
        #     tmp = mul(tmp, segc)
        #     tmp = mul(tmp, 6)
        #     if N == 15 and K == 2:
        #         sys.stderr.write('{},{}, {}\n'.format(a, b, tmp))
        #     count += tmp
        #     count %= MOD
    sys.stderr.write('a<b<c: {}\n'.format(count))
    for a in range(1, N+1):
        b = a
        for c in range(b+1, N+1):
            # count += (((((POW[a] * (POW[b] - POW[b-a])) % MOD) * (POW[c] - (2*POW[c-a]) % MOD)) % MOD) * 3) % MOD
            tmp = mul(POW[a], POW[b]-POW[b-a])
            tmp = mul(tmp, POW[c]-2*POW[c-a])
            tmp = mul(tmp, 3)
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


