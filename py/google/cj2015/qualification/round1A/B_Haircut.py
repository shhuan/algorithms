# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-08 21:17


有B个理发师，第i理发师给一个人理发的时间是Mi，
同时有多个理发师可用时，选择编号小的理发师。
你在队列中第N个，问你会被第几个理发师修理。


分析：
时间t时候，第i个理发师在修理第t/Mi+1个人，
第N个人理发的最早时间是min(M)*N/B，
最晚时间是max(M)*N/B。利用二分

假设时间T的时候，第N个人也正在修理中，但是第N+1个人还在等待中。
第N个人被T%Mi最小的理发师修理

"""
__author__ = 'huash'

import sys
import os

SMALL_DATASET = False

sys.stdin = open('input/sampleB.txt', 'r')

if SMALL_DATASET:
    sys.stdin = open('input/B-small-practice.in', 'r')
    sys.stdout = open('output/B-small-practice.out', 'w')
else:
    sys.stdin = open('input/B-large-practice.in', 'r')
    sys.stdout = open('output/B-large-practice.out', 'w')


T = int(input())
for ti in range(1, T + 1):
    B, N = [int(i) for i in input().split()]
    M = [int(i) for i in input().split()]

    res = 0
    if N <= B:
        res = N
    else:
        tmin = min(M) * (N // B - 1)
        tmax = max(M) * (N // B + 1)
        # print(tmin, tmax)
        while tmin <= tmax:
            t = tmin + (tmax - tmin) // 2
            maxCount = sum([(t//M[i] + 1) for i in range(len(M))])
            minCount = maxCount - sum([1 if t % M[i] == 0 else 0 for i in range(len(M))])
            if minCount < N <= maxCount:

                ith = N - minCount
                for i, m in enumerate(M):
                    if t % m == 0:
                        ith -= 1
                        if ith == 0:
                            res = i + 1
                            break
                break
            elif minCount >= N:
                tmax = t - 1
            else:
                tmin = t + 1




    print('Case #{}: {}'.format(ti, res))