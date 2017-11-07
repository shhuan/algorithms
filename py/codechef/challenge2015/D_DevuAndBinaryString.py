# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-09 15:47


"""
__author__ = 'huash'

import sys
import os
import random


# sys.stdin = open('input/sampleD.txt', 'r')
# sys.stdin = open('input/sampleD-mid.txt', 'r')
# sys.stdout = open('output/sampleD-out.txt', 'w')
# sys.stdout = sys.stderr
def reverse(ch):
    return '1' if ch == '0' else '0'


def caseGenerator(caseCount, maxN, maxK, name):
    f = open('input/{}.txt'.format(name), mode='w')
    f.write('{}\n'.format(caseCount))
    for ci in range(caseCount):
        n = random.randint(2, maxN)
        k = random.randint(2, min(n, maxK))
        f.write('{} {}\n'.format(n, k))
        line = []
        for i in range(n):
            zero = random.randint(1, 10) <= 3
            if zero:
                line.append('0')
            else:
                line.append('1')
        f.write('{}\n'.format(''.join(line)))
    f.close()
    # sys.stderr.write('Case generation finished!\n')

# caseGenerator(1000, 15, 5, 'sampleD-mid')
T = int(input())
for ti in range(1, T + 1):

    N, K = [int(i) for i in input().split()]
    S = input()
    # print(N, K, S)
    # sys.stderr.write('----{}, {}-----\n'.format(N, K))
    res = 0

    if K == 1:
        pre = '0'
        count = 0
        for v in S:
            if v == pre:
                count += 1
            pre = reverse(pre)
        res = count
        count = 0
        pre = '1'
        for v in S:
            if v == pre:
                count += 1
            pre = reverse(pre)
        res = min(res, count)
        print(res)
        # sys.stderr.write('{}\n'.format(S))
        if res == count:
            resList = list()
            resList.append('0')
            for i in range(1, len(S)):
                resList.append(reverse(resList[-1]))
            print(''.join(resList))
        else:
            resList = list()
            resList.append('1')
            for i in range(1, len(S)):
                resList.append(reverse(resList[-1]))
            print(''.join(resList))
    else:
        count = 1
        pre = S[0]
        res = 0
        resList = list()
        for i, v in enumerate(S[1:]):
            if v == pre:
                count += 1
            else:
                if count > K:
                    reverseCount = count//(K+1)
                    res += reverseCount
                    segLen = count//(reverseCount+1)+1
                    for j in range(reverseCount-1):
                        resList.extend([pre]*(segLen - 1))
                        resList.append(reverse(pre))
                    remain = count-(reverseCount-1)*segLen
                    resList.extend([pre] * (remain // 2 - (1 if remain % 2 == 0 else 0)))
                    resList.append(reverse(pre))
                    resList.extend([pre] * (remain // 2))
                else:
                    resList.extend([pre] * count)
                pre = v
                count = 1
        if count <= K:
            resList.extend([pre]*count)
        else:
            reverseCount = count//(K+1)
            res += reverseCount
            segLen = count//(reverseCount+1)+1
            for j in range(reverseCount-1):
                resList.extend([pre]*(segLen - 1))
                resList.append(reverse(pre))
            remain = count-(reverseCount-1)*segLen
            resList.extend([pre] * (remain // 2 - (1 if remain % 2 == 0 else 0)))
            resList.append(reverse(pre))
            resList.extend([pre] * (remain // 2))
        print(res)
        # sys.stderr.write('{}\n'.format(S))
        print(''.join(resList))

        # rs = ''.join(resList)
        # count = 1
        # pre = rs[0]
        # maxSame = 0
        # for i in range(1, len(rs)):
        #     if rs[i] != pre:
        #         maxSame = max(maxSame, count)
        #         count = 1
        #         pre = rs[i]
        #     else:
        #         count += 1
        # maxSame = max(maxSame, count)
        # if maxSame > K:
        #     sys.stderr.write('{}, {}, {} \n'.format(S, N, K))
        #     sys.stderr.write('{}, reversed {}\n'.format(rs, res))
        #     sys.stderr.write('{}\n'.format(''.join(['\n']*2)))
