# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 18:25

Count the number of prime numbers less than a non-negative number, n

Hint: The number n could be in the order of 100,000 to 5,000,000.



"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime
import math
import ctypes

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0

        primes = [True] * (n+1)
        primes[0] = False
        primes[1] = False
        for i in range(2, int(math.sqrt(n))+2):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False
        return primes.count(True)-1

s = Solution()
for i in range(4500000, 4500010):
    print('f({}) = {}'.format(i, s.countPrimes(i)))
