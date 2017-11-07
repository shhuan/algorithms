# -*- coding: utf-8 -*-

"""
created by 'huangshuangquan' at 2015/9/3 18:20

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.


"""
__author__ = 'huangshuangquan'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True

        if not s or not t:
            return False

        if len(s) != len(t):
            return False

        sc = collections.defaultdict(int)
        tc = collections.defaultdict(int)

        for ch in s:
            sc[ch] += 1

        for ch in t:
            tc[ch] += 1

        for ch in sc:
            if sc[ch] != tc[ch]:
                return False

        return True