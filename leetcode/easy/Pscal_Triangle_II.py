# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 10:28

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""
__author__ = 'huash06'

import sys
import os

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return None
        rows = [[0 for c in range(rowIndex+1)] for r in range(2)]
        rows[0][0] = 1
        for i in range(rowIndex):
            r = (i+1) & 1
            rows[r][0] = 1
            for j in range(1, i+1):
                rows[r][j] = rows[i & 1][j-1] + rows[i & 1][j]
            rows[r][i+1] = 1
        return rows[rowIndex & 1][:rowIndex+1]

s = Solution()
for i in range(10):
    print(''.join(list(map(str, s.getRow(i)))))
