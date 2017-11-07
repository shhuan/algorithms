# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 21:22

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if not S:
            return []
        ret = [[]]
        S = list(sorted(S))
        for n in range(1, len(S)+1):
            sn = self.subsetN(S, n, 0, [])
            print('s{} = {}'.format(n, sn))
            ret.extend(sn)
        return ret

    def subsetN(self, S, n, c, s):
        if n == 0:
            return []
        if len(s) == n:
            return [s]
        if len(S) - c < n - len(s):
            return []
        r1 = self.subsetN(S, n, c+1, s+[S[c]])
        r2 = self.subsetN(S, n, c+1, s)
        return r1 + r2



print([1, 2, 3] + [4, 5])
print([1, 2, 3].extend([4, 5]))
print([1, 2] + [])
print([1, 2].extend([]))
s = Solution()
print(s.subsets([1, 3, 2]))