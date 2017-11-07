# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-15 21:54


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple
transactions at the same time (ie, you must sell the stock before you buy again).



f(i, 1) 表示第i天持有股票时的最大利润，
f(i, 0) 表示第i天不持有股票时的最大利润，

f(i, 1) = max{f(i-1, 1), f(i-1, 0)-prices[i]}
f(i, 0) = max{f(i-1, 0), f(i-1, 1)+prices[i]}


"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect


class Solution:
    # @param prices, an integer[]
    # @return an integer
    def maxProfit(self, prices):

        if not prices:
            return 0

        # 不持有股票
        p00 = 0

        # 持有股票
        p11 = -prices[0]

        for p in prices:
            p11 = max(p11, p00-p)
            p00 = max(p00, p11+p)

        return p00

    def maxProfit2(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i]-prices[i-1])
        return profit


s = Solution()
print(s.maxProfit([1]))
print(s.maxProfit([1, 5, 3, 7]))
print(s.maxProfit([1, 3, 5]))
print(s.maxProfit([1, 5, 2, 3]))

print(s.maxProfit2([1]))
print(s.maxProfit2([1, 5, 3, 7]))
print(s.maxProfit2([1, 3, 5]))
print(s.maxProfit2([1, 5, 2, 3]))

