# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-17 16:53
"""
__author__ = 'huash06'

import datetime
import sys
import math


class CartInSupermarketEasy:
    def calc(self, N, K):
        res = N
        for k in range(1, K + 1):
            # y = int(math.floor(math.log2(k+1)))

            y = int(math.log(k + 1, 2))
            p2y = 1 << y
            z = k - (p2y - 1)
            # t = math.ceil(N/(p2y+z))+y+1

            n = N - (p2y-z) if z > 0 else N
            t = n // (p2y + z) if n % (p2y + z) == 0 else n // (p2y + z) + 1
            t += y + (1 if z != 0 else 0)

            res = min(res, t)

        return res

    def dp(self, N, K):
        f = [[0 for c in range(K + 1)] for c in range(N + 1)]

        for n in range(N + 1):
            f[n][0] = n

        for n in range(1, N + 1):
            mk = min(K, n)
            for kc in range(1, mk+1):
                t = f[n - 1][kc] + 1
                for n1 in range(1, n):
                    n2 = n - n1
                    for k1 in range(kc):
                        k2 = kc - k1 - 1
                        t = min(t, 1 + max(f[n1][k1], f[n2][k2]))
                f[n][kc] = t
            for kc in range(mk+1, K+1):
                f[n][kc] = f[n][mk]
        return f[N][K]

s = CartInSupermarketEasy()
# print(s.calc(4, 1))
# print(s.calc(5, 0))
print(s.calc(5, 2))
print(s.calc(15, 4))
print(s.calc(7, 100))
print(s.calc(45, 5))
print(s.calc(100, 100))
print(s.calc(1, 2))
print(s.calc(7, 2))
st = datetime.datetime.now()
s.dp(100, 100)
print('Time Cost: {}'.format(datetime.datetime.now()-st))
s.dp(2, 1)
for i in range(100):
    for j in range(i + 2):
        c1 = s.calc(i, j)
        c2 = s.dp(i, j)
        if c1 != c2:
            print(i, j, c1, c2)