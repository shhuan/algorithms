# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 10:43

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
__author__ = 'huash06'

import sys
import os

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows <= 0:
            return []
        result = [[1]]
        for i in range(numRows-1):
            row = [1]
            for j in range(len(result[i])-1):
                row.append(result[i][j]+result[i][j+1])
            row.append(1)
            result.append(row)
        return result



s = Solution()
triangle = s.generate(5)
for row in triangle:
    print(''.join(list(map(str, row))))
