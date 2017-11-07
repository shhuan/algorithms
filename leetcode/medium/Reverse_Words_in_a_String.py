# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 22:23

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(list(filter(lambda x: x, reversed(s.strip().split(' ')))))


s = Solution()

print(s.reverseWords('   the   sky   is   blue '))