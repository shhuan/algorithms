# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 18:37

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""
__author__ = 'huash'

import sys
import os



class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):

        if not s:
            return True

        cs = s.upper()
        vs = ''
        for ch in cs:
            if ch.isalnum() or ch.isalpha():
                vs += ch
        return vs == ''.join((reversed(vs)))


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome('1a2'))