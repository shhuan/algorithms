# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-05 08:42

You are given two s: N and K. Lun the dog is interested in strings that satisfy the following conditions:

The string has exactly N characters, each of which is either 'A' or 'B'.
The string s has exactly K pairs (i, j) (0 <= i < j <= N-1) such that s[i] = 'A' and s[j] = 'B'.
If there exists a string that satisfies the conditions, find and return any such string.
Otherwise, return an empty string.


"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


class AB:
    def createString(self, N, K):
        """
        假设结果是a1,b1,a2,b2,...,ak,bk,ak+1,
        即a1个A跟b1个B再跟a2个A...，
        a1*(b1+b2+...+bk)+a2(b2+...+bk)+...ai*(bi+...+bk) == K

        :param N:
        :param K:
        :return:
        """
        res = ''
        if K < N:
            res += 'A'
            for i in range(K):
                res += 'B'
            for i in range(N-K-1):
                res += 'A'
            return res
        else:
            if K > self.maxPairCount(N):
                return ''

            for b in range(N, 0, -1):
                a = K // b
                if a + b <= N:
                    exps = self.findExp(K-a*b, N-a-b, b)
                    if exps:
                        # print(N, K, a, b, exps)
                        res = ['A']*a + ['B']*b
                        # print(res)
                        for ea, eb in exps:
                            res = res[:len(res)-eb]+['A']*ea+res[len(res)-eb:]
                            # print(res)
                        if len(res) <= N:
                            res += ['A']*(N-len(res))
                            return ''.join(res)
        return ''

    def maxPairCount(self, N):
        return pow(N//2, 2) if N % 2 == 0 else N//2*(N//2 + 1)


    def findExp(self, K, a, b):
        """
        在b个B中插入1~a个A
        :param K:
        :param A:
        :param B:
        :return:
        """
        if K == 0:
            return [(0, 0)]
        if K > a*(b-1):
            return []

        for i in range(b-1, 0, -1):
            for j in range(a, 0, -1):
                if K == i * j:
                    return [(j, i)]
                if K > i*j:
                    nexts = self.findExp(K-i*j, a-j, i)
                    if nexts:
                        return [(j, i)] + nexts
        return []











s = AB()
print(s.createString(3, 2))
print(s.createString(2, 0))
print(s.createString(6, 8))
print(s.createString(10, 12))
print(s.createString(6, 7))
print(s.createString(5, 7))
print(s.createString(4, 7))
print(s.createString(7, 7))

# print(s.findExp(7,))
# for b in range(6, 0, -1):
#     a = 7 // b
#     if a + b <= 6:
#         print(a, b, 7-a*b, 6-a-b, b)
#         print(s.findExp(7-a*b, 6-a-b, b))