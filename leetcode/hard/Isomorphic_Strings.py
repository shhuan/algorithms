# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-03 19:37

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):

        cmap = {}
        for i in range(len(s)):
            if s[i] in cmap:
                if cmap[s[i]] != t[i]:
                    return False
            else:
                cmap[s[i]] = t[i]

        if len(set(cmap.values())) != len(cmap.values()):
            return False

        return True

s = Solution()
print(s.isIsomorphic('egg', 'add'))
print(s.isIsomorphic('foo', 'bar'))
print(s.isIsomorphic('paper', 'title'))