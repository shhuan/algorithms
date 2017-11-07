# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:48

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        pre = ''
        prec = 0
        i = 0
        for v in A:
            if v != pre:
                pre = v
                prec = 1
            else:
                prec += 1
            if prec <= 2:
                A[i] = v
                i += 1
        return i
