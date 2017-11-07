# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 17:43

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        """
        p1, p2, p3, p4 分别表示操作1次，2次，3次，4次后的利润。
        2次操作完成一次交易。
        :param prices:
        :return:
        """
        if not prices:
            return 0

        p1 = -prices[0]
        p2 = 0
        p3 = -1000000
        p4 = 0

        for d in range(1, len(prices)):
            p4 = max(p4, p3+prices[d])
            p3 = max(p3, p2-prices[d])
            p2 = max(p2, p1+prices[d])
            p1 = max(p1, -prices[d])

        return max(0, p2, p4)

s = Solution()
print(s.maxProfit([1]))
print(s.maxProfit([1, 5, 3, 7]))
print(s.maxProfit([1, 3, 5]))
print(s.maxProfit([1, 5, 2, 3]))