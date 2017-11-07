# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 16:49

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '({}, {})'.format(self.start, self.end)



class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals:
            return []
        # intervals = sorted(intervals, key=functools.cmp_to_key(self.compareInterval))
        # intervals = intervals.sort(cmp=self.compareInterval)
        # intervals = sorted(intervals, cmp=self.compareInterval)
        # intervals.sort(key=lambda x: x.start)
        intervals = sorted(intervals, key=lambda x: x.start)
        ret = [intervals[0]]

        for i in intervals[1:]:
            if ret[-1].end >= i.start:
                ret[-1].end = max(ret[-1].end, i.end)
            else:
                ret.append(i)
        return ret

    def compareInterval(self, i1, i2):
        return i1.start - i2.start




s = Solution()
ivs = []
ivs.append(Interval(1, 3))
ivs.append(Interval(2, 6))
ivs.append(Interval(8, 10))
ivs.append(Interval(15, 18))
i1 = s.merge(ivs)
for i in i1:
    print(i, end=', ')
