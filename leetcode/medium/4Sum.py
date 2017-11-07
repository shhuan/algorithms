# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 23:19



Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):

        print(list(enumerate(num)))
        two_sum = collections.defaultdict(list)
        res = set()
        for (n1, i1), (n2, i2) in itertools.combinations(enumerate(num), 2):
            two_sum[i1+i2].append({n1, n2})
        print(two_sum)
        for t in list(two_sum.keys()):
            if not two_sum[target-t]:
                continue
            for pair1 in two_sum[t]:
                for pair2 in two_sum[target-t]:
                    if pair1.isdisjoint(pair2):
                        res.add(tuple(sorted(num[i] for i in pair1 | pair2)))
            del two_sum[t]
        return [list(r) for r in res]


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))