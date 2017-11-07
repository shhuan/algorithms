# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 10:02


The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @return a string
    def convert(self, s, numRows):
        if not s:
            return ''
        if numRows <= 1:
            return s

        g = [''] * numRows
        si = 0
        while True:
            if si >= len(s):
                break
            for ri in range(numRows):
                g[ri] += s[si]
                si += 1
                if si >= len(s):
                    break
            if si >= len(s):
                break

            for ri in range(numRows-2, 0, -1):
                g[ri] += s[si]
                si += 1
                if si >= len(s):
                    break
        return ''.join(g)


s = Solution()
print(s.convert('PAYPALISHIRING', 3))