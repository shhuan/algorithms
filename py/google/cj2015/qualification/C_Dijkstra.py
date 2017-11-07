# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-08 19:51


一个循环的i、j、k字符串能否转换成ijk。


由于i*j*k = -1，所以整个字符串的结果是－1才可能够转换为ijk
由于满足结合律，只需要在前面找到最短的能够转换为i、j的字符串，剩下的就能转换为k


"""
__author__ = 'huash'

import sys
import os

SMALL_DATASET = False

if SMALL_DATASET:
    sys.stdin = open('input/C-small-practice.in', 'r')
    sys.stdout = open('output/C-small-practice.out', 'w')
else:
    sys.stdin = open('input/C-large-practice.in', 'r')
    sys.stdout = open('output/C-large-practice.out', 'w')

# sys.stdin = open('input/sampleC.txt', 'r')

M = [[0,  0,  0,  0,  0],
     [0,  1,  2,  3,  4],
     [0,  2, -1,  4, -3],
     [0,  3, -4, -1,  2],
     [0,  4,  3, -2, -1]]

def mul(a, b):
    sign = 1 if a * b > 0 else -1
    return sign * M[abs(a)][abs(b)]

def multiply_all(S, L, X):
    value = 1
    # for i in range(X):
    #     for j in range(L):
    #         value = mul(value, S[j])
    # return value

    # 计算整个序列的值可以优化成以下形式
    # 满足结合律，重复部分的乘积的X次方
    for i in range(L):
        value = mul(value, S[i])
    return power(value, X)


def power(a, n):
    # if n == 1: return a
    # if n % 2 == 0: return power(mul(a, a), n // 2)
    # return mul(a, power(mul(a, a), (n - 1) // 2))

    # 通过观察可以知道一个值和自身相乘4次又得到它自己
    # 所以可以把幂优化成如下形式
    value = 1
    for i in range(n % 4):
        value = mul(value, a)
    return value


def construct_first_two(S, L, X):
    i_value = 1
    j_value = 1
    for i in range(X):
        for j in range(L):
            if i_value != 2:
                i_value = mul(i_value, S[j])
            elif j_value != 3:
                j_value = mul(j_value, S[j])
    return i_value == 2 and j_value == 3

for tc in range(int(input())):
    L, X = map(int, input().split())
    # maps 'i' => 2, 'j' => 3, 'k' => 4
    S = [(ord(v) - ord('i') + 2) for v in input()]
    ok1 = multiply_all(S, L, X) == -1
    ok2 = construct_first_two(S, L, min(X, 8)) # 4次又回到自己，i、j两个最多8次
    print("Case #%d: %s" % (tc + 1, "YES" if ok1 and ok2 else "NO"))