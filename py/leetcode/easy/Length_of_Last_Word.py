# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 16:10

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.


"""
__author__ = 'huash06'

import sys
import os


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if not s:
            return 0

        count = 0
        pcount = 0
        for i in range(len(s)):
            if s[i].isspace():
                pcount = count if count > 0 else pcount
                count = 0
            else:
                count += 1
        return pcount if count == 0 else count

s = Solution()
print(s.lengthOfLastWord(''))
print(s.lengthOfLastWord('a '))
print(s.lengthOfLastWord('ada  dsad'))
print(s.lengthOfLastWord("b   a    "))