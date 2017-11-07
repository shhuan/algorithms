# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-09 10:03


计算一个集合的所有子集的最大值－最小值的和。

1. 把S排序后，以S[j],S[i]，(j>i)的值为集合的最大值最小值的集合的数量是pow(2,j-i-1)。
    时间复杂度O(N^2)，过不了小数据集合
2. 在（1）的基础上，对于任意S[i]它做了pow(2, N-i-2)次最小值，做了pow(2, i-1)次最大值，
    f(i) = S[i]＊两者的差值就是S[i]。
    最终结果result = sigma(f(i))。
    时间复杂度是O(N*lgN)，能够过掉小数据集合
3. 由于时间复杂度已经是O(O*lgN)，更快的方式只有桶排序了。
    把数据分配到(maxV-minV)//N+1个桶中，对于每个桶中的某个元素，它排序后的位置是前面的桶
    里面的元素个数加上它在桶里面的位置，时间复杂度O(1)。
    所以划分桶O(N)，求每个元素的f(i)时间是(1)，N个元素的f(i)时间是O(N)，总时间O(N)

    !!!实验中发现指数计算太慢，使用一个数组提前计算。






"""
__author__ = 'huash'

import sys
import os
import random
import datetime
import math
# sys.stdin = open('input/sampleB.txt', 'r')
# sys.stdin = open('input/sampleB-mid.txt', 'r')

SOLVE2 = False
# if SOLVE2:
#     sys.stdout = open('output/sampleB-small-1-out.txt', 'w')
# else:
#     sys.stdout = open('output/sampleB-small-2-out.txt', 'w')

MOD = 1000000007
POWER2 = [0]*100000
POWER2[0] = 1
for i in range(1, 100000):
    v = POWER2[i-1] << 1
    POWER2[i] = v % MOD

def solve1(N, S):
    if len(S) <= 1:
        return 0

    S = sorted(S)
    res = 0
    for l in range(N):
        for r in range(l+1, N):
            tmp = S[r]-S[l]
            tmp *= pow(2, r-l-1)
            res = (res + tmp % MOD) % MOD
    return res

def solve2(N, S):
    if len(S) <= 1:
        return 0

    S = sorted(S)
    res = 0

    res = S[0] * ((pow(2, N-1) - 1) % MOD)
    res %= MOD
    res = -res
    res += S[N-1] * ((pow(2, N-1)-1) % MOD)
    for i in range(1, N-1):
        v = S[i]
        tmp = 0
        if N-i-1 < i:
            tmp = S[i] * (pow(2, N-i-1) % MOD) * ((pow(2, 2*i-N+1) - 1) % MOD)
            tmp %= MOD
        elif N-i-1 > i:
            tmp = S[i] * (pow(2, i) % MOD) * ((pow(2, N-2*i-1) - 1) % MOD)
            tmp = 0 - tmp
        res = (res + tmp) % MOD
    return res

def solve3(N, S):
    if len(S) <= 1:
        return 0

    startTime = datetime.datetime.now()
    smin = min(S)
    smax = max(S)
    bucketSize = int(math.ceil((smax-smin)/(len(set(S))-1)))
    buckets = [[] for i in range((smax-smin)//bucketSize+1)]
    for v in S:
        buckets[(v-smin)//bucketSize].append(v)
    for bucket in buckets:
        bucket.sort()

    partitionTime = datetime.datetime.now()-startTime
    sys.stderr.write('Partition Time:{}\n'.format(partitionTime))
    startTime = datetime.datetime.now()
    res = 0

    # 和solve2一样，整个序列的最小和最大值要单独处理
    res = smin * ((pow(2, N-1) - 1) % MOD)
    res %= MOD
    res = -res
    res += smax * ((pow(2, N-1)-1) % MOD)


    # 记录下POWER

    # i是当前元素在排好序的数组中的下标记
    i = -1
    for bucket in buckets:
        for bi, bv in enumerate(bucket):
            i += 1
            if i <= 0 or i >= N-1:
                continue
            # 以下部分和solve2一样，只是S[i]换成bv
            tmp = 0
            if N-i-1 < i:
                # tmp = bv * (pow(2, N-i-1) % MOD) * ((pow(2, 2*i-N+1) - 1) % MOD)
                tmp = bv * POWER2[N-i-1] * (POWER2[2*i-N+1] - 1)
                tmp %= MOD
            elif N-i-1 > i:
                # tmp = bv * (pow(2, i) % MOD) * ((pow(2, N-2*i-1) - 1) % MOD)
                tmp = bv * POWER2[i] * (POWER2[N-2*i-1] - 1)
                tmp = 0 - tmp
            res = (res + tmp) % MOD

    calTime = datetime.datetime.now()-startTime
    sys.stderr.write('Calculationg Time:{}, %{}\n'.format(calTime, 100*calTime/(calTime+partitionTime)))

    return res


def caseGenerator(caseCount, caseSize, maxV, name):
    f = open('input/{}.txt'.format(name), mode='w')
    f.write(str(caseCount))
    f.write('\n')
    for i in range(caseCount):
        N = random.randint(caseSize//2+1, caseSize)
        f.write(str(N))
        f.write('\n')
        sys.stderr.write('Case {}, N={}\n'.format(i+1, N))
        count = -1
        for j in range(N):
            f.write(str(random.randint(0, maxV)))
            f.write(' ')

            if j - count >= 100:
                count = j
                sys.stderr.write('Generated {}...\n'.format(j+1))
        f.write('\n')
    sys.stderr.write('Case generate finished')

# caseGenerator(10, 1000, 1000000000, 'sampleB-small')
T = int(input())
for ti in range(1, T + 1):
    N = int(input())
    readStart = datetime.datetime.now()
    S = map(int, input().split())
    sys.stderr.write('Read Cost: {}\n'.format(datetime.datetime.now() - readStart))
    if SOLVE2:
        print(solve2(N, S))
    else:
        res = solve3(N, list(S))
        print(res)
        sys.stderr.write('Time Cose:{}, answer: {}\n'.format(datetime.datetime.now()-readStart, res))
