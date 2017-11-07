# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:49

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return self.impl(1, n, k, [])


    def impl(self, index, n, k, pres):
        if k == 0:
            return [pres]
        if index > n or n-index+1 < k:
            return []

        ret = self.impl(index+1, n, k, pres)
        ret.extend(self.impl(index+1, n, k-1, pres+[index]))

        return ret