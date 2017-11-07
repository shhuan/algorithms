# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 10:14

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections



class Solution:
    # @param n, an integer
    # @return a string[]
    def generateParenthesis(self, n):
        if n <= 0:
            return ''

        return self.dfs('', n*2, 0, 0)

    def dfs(self, parentheses, targetCount, count, leftCount):
        if count >= targetCount:
            return [parentheses]

        if leftCount == targetCount-count:
            return [parentheses+')'*(targetCount-count)]

        result = []
        if leftCount <= 0:
            result.extend(self.dfs(parentheses+'(', targetCount, count+1, leftCount+1))
        else:
            result.extend(self.dfs(parentheses+'(', targetCount, count+1, leftCount+1))
            result.extend(self.dfs(parentheses+')', targetCount, count+1, leftCount-1))
        return result



s = Solution()
print(s.generateParenthesis(3))