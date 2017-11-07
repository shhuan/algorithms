# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:50

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        l = 0
        r = len(A)-1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        lower = r+1 if 0 <= r+1 < len(A) and A[r+1] == target else -1
        if lower < 0:
            return [-1, -1]
        l = 0
        r = len(A)-1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        upper = l-1 if 0 <= l-1<len(A) and A[l-1] == target else -1
        return [lower, upper]