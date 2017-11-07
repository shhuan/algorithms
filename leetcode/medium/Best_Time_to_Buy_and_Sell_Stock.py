"""

created by huash06 at 2015-04-15

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools


class Solution:
    # @param prices, an integer[]
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0

        minprice = prices[0]
        profit = 0
        for p in prices:
            if p < minprice:
                minprice = p
            else:
                v = p - minprice
                profit = max(profit, v)
        return profit

s = Solution()
print(s.maxProfit([1, 4, 2]))
print(s.maxProfit([2, 4, 1]))
print(s.maxProfit([5, 1, 2, 7, 3, 9, 2, 11, 0, 12, 8]))