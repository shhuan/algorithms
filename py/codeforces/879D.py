# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/10/28 16:57

"""

N, K, M = map(int, input().split())

A = [int(x) for x in input().split()]
#
#
# N, K, M = 100000, 5, 1000000000
#
# A = []
# while len(A) < N:
#     a = [random.randint(1, 2)] * random.randint(10, 50)
#     A += a
# A = A[:N]

p = A[0]
c = 1
a = []
for i in range(1, N):
    v = A[i]
    if v != p:
        a.append((p, c))
        p = v
        c = 1
    else:
        c += 1
a.append((p, c))
A = a


def merge(a, k, m):
    # merge 2 a
    if not a:
        return False, []

    t0 = time.time()
    p0, c0 = a[0]
    p1, c1 = a[-1]
    c = c0 + c1
    if p0 == p1 and c >= k:
        if c % k == 0:
            ans = group(a[:-1] + a[1:], k, m)
            # print("merge ", len(a), " cost ", time.time() - t0, " => ", len(ans))
            return True, ans
        else:
            ans = group(a[:-1] + [(p1, (c0+c1) % k)] + a[1:], k, m)
            # print("merge ", len(a), " cost ", time.time() - t0, " => ", len(ans))
            return True, ans

    return False, a


def group(a, k, m):
    global removed
    if not a:
        return []

    ans = []
    for p, c in a:
        if p == '#':
            ans.append((p, c))
            continue
        if not ans:
            c %= k
            if c > 0:
                ans.append((p, c))
        else:
            p0, c0 = ans[-1]
            if p == p0:
                ans.pop()
                c = (c+c0) % k
                if c > 0:
                    ans.append((p, c))
            else:
                c %= k
                if c > 0:
                    ans.append((p, c))

    n = len(ans)
    if n > 2*m:
        c = 0
        for i in range(m, n-m):
            c += ans[i][1]

        return ans[:m] + [('#', c)] + ans[n-m:]
    return ans


A = group(A, K, 1000000)

if len(A) == 1:
    p, c = A[0]
    c = (c*M) % K
    print(c)
    exit(0)


rem = []

found = True
while M > 1 and found:
    found, a = merge(A, K, int(math.log(M, 2))+1)
    if found:
        rem = A * (M % 2) + rem
        A = a
        M //= 2
        found = True

rem = group(rem, K, 1000000)
if not rem:
    print(sum([c for _, c in A] or [0]) * M)
else:
    if M > 0:
        ans = sum([c for _, c in A] or [0]) * (M-1)
        A = group(A + rem, K, 1000000)
        ans += sum([c for _, c in A] or [0])
        print(ans)
    else:
        print(sum([c for _, c in rem] or [0]))

