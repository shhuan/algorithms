# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-11 19:00


Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""
__author__ = 'huash'

import sys
import os

class Solution:
    def isValid(s):
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif ch == '(' or \
                ch == '[' or \
                    ch == '{':
                stack.append(ch)
            else:
                top = stack.pop()
                if (ch == ')' and top != '(') or \
                        (ch == ']' and top != '[') or \
                        (ch == '}' and top != '{'):
                    return False
        return True if not stack else False

s = Solution()
print(s.isValid('()'))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))


