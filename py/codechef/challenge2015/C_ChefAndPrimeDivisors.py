# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-09 13:25

给定两个正整数A, B，请判断A是否能够被B的所有质因素整除。

数据范围
• 1 ≤ T ≤ 104
• 数据集1: 1 ≤ A ≤ 1018, 1 ≤ B ≤ 107
• 数据集2: 1 ≤ A ≤ 107, 1 ≤ B ≤ 1018
• 数据集3: 1 ≤ A ≤ 1018, 1 ≤ B ≤ 1018


分析:
1. 对B做质因树分解，得到质因数集合S，判断是否A能被所有的S中的数整除。
    问题是在B很大的时候分解质因数非常慢

2. 考虑求A、B的最大公约数g = gcd(A, B)，
    如果g==1, A肯定不能被B的所有因数。
    否则B //= g之后A，还是能被B的所有因数整除的话返回True。
    A不能除g，比如A=2, B=6

"""
__author__ = 'huash'

import sys
import os
import math
import random

import datetime
import fractions


# DEBUG = True
#
# if DEBUG:
#     sys.stdin = open('input/sampleC.txt', 'r')
    # sys.stdout = open('output/sampleC-out.txt', 'w')


def deducePrimes(num, primes):
    if num <= 1:
        return primes
    prime = num
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            prime = i
            break
    if prime == num:
        primes.add(num)
        return primes
    primes.add(prime)
    deducePrimes(num//prime, primes)
    return primes

def deducePrimes2(num):

    res = set()

    # for i in range(2, int(math.sqrt(num))+1):
    #     if num % i == 0:
    #         res.add(i)
    #         while num % i == 0:
    #             num //= i

    # 递归比上面快是因为i的范围比较小
    i = 2
    maxi = int(math.sqrt(num))
    while i <= maxi:
        if num % i == 0:
            res.add(i)
            while num % i == 0:
                num //= i
            maxi = int(math.sqrt(num))
        i += 1

    if num > 1:
        res.add(num)
    return res


def isNumDividedByPrimes(num, primes):
    for prime in primes:
        if num % prime != 0:
            return False
    return True


def isPrimeDivisor(A, B):
    if A % B == 0:
        return True
    if A <= 1:
        return False
    g = fractions.gcd(A, B)
    if g == 1:
        return False
    # A //= g
    B //= g
    return isPrimeDivisor(A, B)

T = int(input())
for ti in range(1, T + 1):
    A, B = [int(i) for i in input().split()]

    # print('Yes' if isNumDividedByPrimes(A, deducePrimes(B, set())) else 'No')
    print('Yes' if isPrimeDivisor(A, B) else 'No')

# print(deducePrimes2(25))
# print(deducePrimes2(1))
# print(deducePrimes2(2))
# print(deducePrimes2(3))
# startTime = datetime.datetime.now()
# N = 10
# costA = datetime.timedelta(0)
# costB = datetime.timedelta(0)
# for i in range(N):
#     A = random.randint(1000000000000000, 1000000000000000000)
#     B = random.randint(1000000000000000, 1000000000000000000)
#
#     # s = datetime.datetime.now()
#     # print('primes({}) = {}'.format(B, deducePrimes2(B)))
#     # ta = datetime.datetime.now() - s
#     # print('primes({}) = {}'.format(B, deducePrimes(B, set())))
#     # tb = datetime.datetime.now() - s - ta
#     #
#     # costA += ta
#     # costB += tb
#
#     # print('Yes' if isNumDividedByPrimes(A, deducePrimes2(B)) else 'No')
#     print('Yes' if isPrimeDivisor(A, B) else 'No')
# timeNow = datetime.datetime.now()
# print('Time Cost: {}, {}, {}, AVG: {}, '.format(timeNow-startTime, costA, costB, (timeNow-startTime)/N))

