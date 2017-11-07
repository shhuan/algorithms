# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-07 17:11
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections

import copy


class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        return self.dfs(k, n, 1, [])

    def dfs(self, k, n, i, pres):
        if n == 0 and k == 0:
            return [copy.copy(pres)]

        if k <= 0 or i > 9:
            return None

        ret = []
        pres.append(i)
        r2 = self.dfs(k - 1, n - i, i + 1, pres)
        if r2:
            ret.extend(r2)
        pres.pop()

        r1 = self.dfs(k, n, i + 1, pres)
        if r1:
            ret.extend(r1)

        return ret


s = Solution()

print(s.combinationSum3(3, 7))
print(s.combinationSum3(3, 9))