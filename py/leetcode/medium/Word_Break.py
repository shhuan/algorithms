# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:04

Given a string s and a dictionary of words dict, determine if s can be segmented
into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".


f(i,j)表示s[i:j+1]能够被分割， 有两种情况f(i,j) == True
 1. s[i:j+1]是一个完整的单词
 2. s[i,k] 和 s[k+1, j] 都能够被分割

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s or not dict:
            return False

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
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", {"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"}))