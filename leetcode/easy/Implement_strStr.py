# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 13:49

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Update (2014-11-02):
The signature of the function had been updated to return the index instead of the pointer.
If you still see your function signature returns a char * or String,
please click the reload button  to reset your code definition.

"""
__author__ = 'huash06'

import sys
import os

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


s = Solution()
print(s.strStr('1232323223', '2'))
print(s.strStr('', ''))
print(s.strStr('aaa', 'aa'))