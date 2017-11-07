# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-12 08:28
"""
__author__ = 'huash06'

import datetime
import sys
import collections


class BridgeBuildingDiv2:
    def minDiameter(self, a, b, K):

        return self.dfs(a, b, K, [0]*(len(a)+1), 0)


    def dfs(self, a, b, k, ve, index):
        if index > len(a):
            return self.dist(a, b, ve)

        if k <= 0:
            return self.dist(a, b, ve)

        ve[index] = 1
        res = self.dfs(a, b, k-1, ve, index+1)
        ve[index] = 0
        res = min(self.dfs(a, b, k, ve, index+1), res)

        return res

    def dist(self, a, b, ve):

        la = len(a) + 2
        lb = len(b) + 2
        bbase = la
        l = la + lb
        d = [[10000000 for c in range(l)] for r in range(l)]

        for i, v in enumerate(a):
            d[i][i+1] = v
            d[i+1][i] = v
        for i, v in enumerate(b):
            d[i+bbase+1][i+bbase] = v
            d[i+bbase][i+bbase+1] = v

        for i, v in enumerate(ve):
            if v == 1:
                d[i][i+bbase] = 0
                d[i+bbase][i] = 0

        for k in range(l):
            for i in range(l):
                for j in range(l):
                    if d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k]+d[k][j]
        res = 0
        for i in range(l):
            for j in range(l):
                if d[i][j] < 10000000:
                    res = max(res, d[i][j])
        # print(a, b, ve, res, d)
        return res


s = BridgeBuildingDiv2()
print(s.minDiameter([2,1,1,1,2], [1,9,1,9,1], 4))
print(s.minDiameter([1,50,1,50,1,50,1,50], [50,1,50,1,50,1,50,1],9))