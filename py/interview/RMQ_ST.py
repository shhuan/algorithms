# -*- coding: utf-8 -*-

"""
Microsoft

写出RMQ的ST实现



M[i][j]表示从i开始的2^j次方个元素，即A[i, i+2^j-1]中最小元素的下标

M[i][j] = min{M[i][j-1], M[i+2^(j-1)][j-1]}


"""
__author__ = 'huangshuangquan'

import math
import random
import datetime

M = None
A = None


def init(vals):
    global M
    global A

    A = [val for val in vals]
    N = len(vals)
    # 区间最大长度是 int(math.log(N, 2)) + 1
    R = int(math.log(N, 2)) + 1
    # 空间复杂度R*N，即N*log(N)
    M = [[0 for c in range(R)] for r in range(N)]

    # 注意初始化长度为1的区间
    for i in range(N):
        M[i][0] = i

    # 一定要注意先计算小区间，才能计算大区间
    gap = 1
    for j in range(1, R + 1):
        gap <<= 1
        for i in range(0, len(vals) - gap + 1):
            ri = i + pow(2, j - 1)
            # 不要写掉A
            if A[M[i][j - 1]] < A[M[ri][j - 1]]:
                M[i][j] = M[i][j - 1]
            else:
                M[i][j] = M[ri][j - 1]


def rmq(left, right):
    global M
    global A

    # 注意条件检查
    if left == right:
        return A[left]
    elif left > right:
        return None

    l = int(math.log(right - left, 2))
    v1 = A[M[left][l]]
    # 注意起始位置+1
    v2 = A[M[right - (1 << l) + 1][l]]

    return min(v1, v2)


def brutal(vals, left, right):
    return min(vals[left: right + 1])


if __name__ == "__main__":

    MAXN = 100000

    N = random.randint(9 * MAXN // 10, MAXN)
    vals = [random.randint(1, 1000000) for _ in range(N)]
    init(vals)

    queries = []
    for i in range(MAXN):
        l = random.randint(0, N-1)
        r = random.randint(l, N-1)
        queries.append((l, r))
    print("==========starting===========")
    t0 = datetime.datetime.now()
    result = []
    for l, r in queries:
        # v1 = brutal(vals, l, r)
        # v2 = rmq(l, r)
        # if v1 != v2:
        #     print(l, r, v1, rmq(l, r))
        print(rmq(l, r))
    t1 = datetime.datetime.now()
    print("=============={} ms==============".format(t1-t0))