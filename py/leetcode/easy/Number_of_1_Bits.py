# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-11 19:33
"""
__author__ = 'huash'

import sys
import os



class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = n & 1
        while n:
            n >>= 1
            if n & 1:
                count += 1
        return count



s = Solution()
for i in range(25):
    print('f({}) = {}'.format(i, s.hammingWeight(i)))