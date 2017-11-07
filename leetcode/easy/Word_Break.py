# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 08:54

Given a string s and a dictionary of words dict, determine if s can be segmented into
a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

"""
__author__ = 'huash06'

import sys
import os


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s or not dict:
            return False
        # f(i) = f(j) if s[j+1:i+1] in dict, 0<=j<i
        valid = [False for i in range(len(s))]
        for i in range(len(s)):
            if s[:i+1] in dict:
                valid[i] = True
                continue
            for j in range(i):
                if valid[j] and s[j+1:i+1] in dict:
                    valid[i] = True
                    break

        return valid[len(s)-1]

s = Solution()

print(s.wordBreak('leetcode', ['leet', 'code']))
