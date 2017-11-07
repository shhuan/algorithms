# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-09 17:16
"""
__author__ = 'huash'

import sys
import os
import math
import functools
from functools import lru_cache
import datetime
import random
startTime = datetime.datetime.now()

# sys.stdin = open('input/sampleE.txt', 'r')
# sys.stdout = open('output/-small-practice.out', 'w')


N, K, Q = list(map(int, input().split()))

A = [0]*(N+1)
MOD = pow(10, 9) + 7
a, b, c, d, e, f, r, s, t, m, A[1] = list(map(int, input().split()))
L1, La, Lc, Lm, D1, Da, Dc, Dm = list(map(int, input().split()))

# generate tastes of N items
# A.append(A1)
# A[1] = A1
AL = 1
AR = N
exists = {A[1]}
for x in range(2, N+1):
    if pow(t, x) % s <= r:
        Ax = (a*A[x-1]*A[x-1] + b*A[x-1] + c) % m
    else:
        Ax = (d*A[x-1]*A[x-1] + e*A[x-1] + f) % m
    # A.append(Ax)
    if Ax in exists:
        AL = A[1:x].index(Ax)
        AR = x - 1
        break
    A[x] = Ax
    exists.add(Ax)

APRE = A[1:AL+1]
A = A[AL+1: AR+1]
ALEN = len(A)
# print(A[:200])
# print(APRE)
# print(A)
sys.stderr.write('AGen Cost: {}\n'.format(datetime.datetime.now()-startTime))

# segment tree
# M[i] holds the minimum value position in the interval assigned to node i.
M = [-1] * (2*int(math.pow(2, int(math.log2(ALEN))+1)))

def initialize(node, b, e):
    if b == e:
        M[node] = b
    else:
        # compute the values in the left and right subtrees
        initialize(2*node, b, (b+e)//2)
        initialize(2*node+1, (b+e)//2+1, e)
        # search for the minimum value in the first and second half of the interval
        if A[M[2*node]] <= A[M[2*node+1]]:
            M[node] = M[2*node]
        else:
            M[node] = M[2*node+1]


@lru_cache(maxsize=None)
def query(node, b, e, i, j):
    # if the current interval doesn't intersect the query interval
    if i > e or j < b:
        return -1
    # if the current interval is included in the query interval
    if b >= i and e <= j:
        return M[node]

    # compute the minimum position in the left and right part of the interval
    p1 = query(2*node, b, (b+e)//2, i, j)
    p2 = query(2*node+1, (b+e)//2+1, e, i, j)

    # return the position where the overall minimum is
    if p1 == -1:
        return p2
    elif p2 == -1:
        return p1
    elif A[p1] <= A[p2]:
        return p1
    else:
        return p2


initialize(1, 0, ALEN-1)
# print(M)
sys.stderr.write('Init Cost: {}\n'.format(datetime.datetime.now()-startTime))


# Sparse Table
# LOG = [(0 if i <=0 else int(math.log2(i))) for i in range(N+1)]
# M = [[0 for c in range(LOG[N]+2)] for r in range(N+2)]
# for i in range(N):
#     M[i][0] = i
# for j in range(1, LOG[N]+1):
#     for i in range(N+2-(1 << j)):
#         k = i+(1 << (j-1))
#         if A[M[i][j-1]] < A[M[k][j-1]]:
#             M[i][j] = M[i][j-1]
#         else:
#             M[i][j] = M[k][j-1]

# for row in M:
#     print(row)

def generateDish(l, r):
    return 1
    # us ST, not fast enough
    # k = LOG[r-l+1]
    # t = r-pow(2, k)+1
    # if A[M[l][k]] <= A[M[t][k]]:
    #     return A[M[l][k]]
    # else:
    #     return A[M[t][k]]
    # print(l, r)
    # if r < AL:
    #     return min(APRE[l: r+1])
    #
    # apreMin = 10000000000
    #
    # if l < AL:
    #     l = 0
    #     apreMin = min(APRE[l:AL+1])
    # else:
    #     l -= AL
    #     l %= ALEN
    # r -= AL
    # r %= ALEN
    # if l > r:
    #     return min(A[query(1, 0, ALEN-1, r, AR)], A[query(1, 0, ALEN-1, 0, l)])
    # return min(A[query(1, 0, ALEN-1, l, r)], apreMin)
    # return min(A[l: r+1])

# generate tastes of N dishes
# Dishes = list()
sumdishes = 0
product = 1
dishes = list()
# l1 = L1
# d1 = D1
queries = [(L1, D1)]
qset = {(L1, D1)}
QL = 0
for i in range(1, Q+1):
    L1 = (La * L1 + Lc) % Lm
    D1 = (Da * D1 + Dc) % Dm
    L = L1 + 1
    R = min(L + K - 1 + D1, N)
    print(L, R)
    # dish = generateDish(L-1, R-1)
    # dishes.append(dish)
    # if (L1, D1) in qset:
    #     break
    #     QL = queries.index((L1, D1))
    # queries.append((L1, D1))
    # qset.add((L1, D1))
    # if dupc > 3:
    #     break
    # sumdishes += dish
    # product *= dish
    # product %= MOD
    # Dishes.append(generateDish(L-1, R-1))
# print(dishes[:20])
# print('Query Cost: {}'.format(datetime.datetime.now()-startTime))

# mlamba = lambda x, y: (x*y) % MOD
# sumdishes = sum(dishes[:QL]) if QL > 0 else 0
# preproduct = functools.reduce(mlamba, dishes[:QL]) if QL > 0 else 1
# dishes = dishes[QL:]
#
# sumdishes += sum(dishes[QL+1:]) * (Q // len(dishes)) + sum(dishes[:Q % len(dishes)])
# product = functools.reduce(lambda x, y: (x*y) % MOD, dishes)
# if Q // len(dishes) <= 0:
#     product = 1
# else:
#     for i in range(Q//len(dishes)-1):
#         product = (product*product) % MOD
# for i in range(Q % len(dishes)):
#     product = (product*dishes[i]) % MOD
# # print(A)
# # print(Dishes)
# product = (preproduct*product) % MOD
# print('{} {}'.format(sumdishes, product))
#
# sys.stderr.write('Time Cost: {}\n'.format(datetime.datetime.now()-startTime))
