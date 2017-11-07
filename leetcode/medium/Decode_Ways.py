# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 09:44

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

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
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        elif int(s[0]) > 2 and s[1] == '0':
            return 0

        p1 = 1
        p2 = 2 if int(s[:2]) in range(11, 27) and s[1] != '0' else 1
        p = p2
        for i in range(2, len(s)):
            if (int(s[i-1]) > 2 or s[i-1] == '0') and s[i] == '0':
                return 0
            if int(s[i-1: i+1]) in range(11, 27) and \
               int(s[i-1 : i+1]) != 20:
                p = p1 + p2
            elif s[i] == '0':
                p = p1
            else:
                p = p2
            p1 = p2
            p2 = p
        return p