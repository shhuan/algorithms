# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 23:28

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

"""

__author__ = 'huash06'

import sys
import os


class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        if not s or len(s) < 11:
            return []

        allsq = set()
        result = set()
        for i in range(len(s)-9):
            sq = s[i:i+10]
            if sq in allsq:
                result.add(sq)
            else:
                allsq.add(sq)
        return list(result)

s = Solution()
print(s.findRepeatedDnaSequences('AAAAAAAAAAAA'))
print(s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))