# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 18:31

Write a function to find the longest common prefix string amongst an array of strings.


"""
__author__ = 'huash'

import sys
import os


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):

        # 44ms
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or ch != s[i]:
                    return strs[0][:i]

        return strs[0]


    def longestCommonPrefix2(self, strs):
        # 64m
        return strs[0][:max(filter(lambda i: i == 0 or len(set([s[:i] for s in strs])) == 1, [i for i in range(max(min([len(s) for s in strs])+1, 1))]))] if strs else ''



s = Solution()

print(s.longestCommonPrefix(['12123333', '1212', '1212x2q', '1212e21', '1212de21e12', '1212dwqdq', '1212dqdw']))
print(s.longestCommonPrefix(['111122']))
print(s.longestCommonPrefix(["a", "b"]))
print(s.longestCommonPrefix([""]))
print(s.longestCommonPrefix(["a"]))
print(s.longestCommonPrefix([]))