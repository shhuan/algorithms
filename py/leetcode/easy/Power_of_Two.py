# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-07 22:15

Given an integer, write a function to determine if it is a power of two.



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
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        i = 1
        count = 0
        for _ in range(len(bin(n))):
            if n & i > 0:
                count += 1
            i <<= 1
            if count > 1:
                return False
        return count == 1


s = Solution()
print(bin(12))
print(s.isPowerOfTwo(7))
print(s.isPowerOfTwo(8))
print(s.isPowerOfTwo(0))
