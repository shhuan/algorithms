# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 15:24

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


f(n) = f(n-1)+f(n-2)

"""
__author__ = 'huash06'

import sys
import os

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 1:
            return 1
        elif n == 2:
            return 2

        s = [0]*(n+1)
        s[1] = 1
        s[2] = 2
        for i in range(3, n+1):
            s[i] = s[i-1]+s[i-2]
        return s[n]

s = Solution()
for i in range(10):
    print(s.climbStairs(i))


