# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 22:33

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


f(n) = sum{f(i-1)*f(n-i), 1<=i<=n}
f(0) = 1

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
    # @param n, an integer
    # @return an integer
    @functools.lru_cache(maxsize=None)
    def numTrees(self, n):
        Solution.CACHE[0] = 1
        Solution.CACHE[1] = 1
        Solution.CACHE[2] = 2
        Solution.CACHE[3] = 5

        if Solution.CACHE[n] > 0:
            return Solution.CACHE[n]

        result = 0
        for i in range(1, n+1):
            result += self.numTrees(i-1)*self.numTrees(n-i)
        Solution.CACHE[n] = result
        return result

    CACHE = [0]*50




s = Solution()
for i in range(25):
    print('f({}) = {}'.format(i, s.numTrees(i)))
