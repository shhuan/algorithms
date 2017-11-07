# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-02 20:32

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        """
        设f(i, j)表示p的前i个字符可以匹配s的前j个字符。

        注意使用f(i, 0)表示p的前i个字符可以不匹配任何s的字符，
        例如a*b的前两个字符a*可以匹配空字符串

        :param s:
        :param p:
        :return:
        """
        if not p and not s:
            return True
        if not p:
            return False

        # change ** to *
        p = ''.join([x[1] for x in filter(lambda x: x[0] == 0 or x[1] != '*' or x[1] != p[x[0]-1], enumerate(p))])

        if len(p)-2*p.count('*') > len(s):
            return False
        if not s:
            return True

        match = [[False for c in range(len(s)+1)] for r in range(len(p)+1)]

        match[1][1] = True if p[0] == '.' or p[0] == s[0] else False
        match[0][0] = True

        pi = 2
        while pi < len(p)+1:
            cur = p[pi-1]
            if cur == '*':
                for si in range(len(s)+1):
                    if match[pi-2][si]:
                        match[pi][si] = True
                        for k in range(si+1, len(s)+1):
                            if s[k-1] == p[pi-2] or p[pi-2] == '.':
                                match[pi][k] = True
                            else:
                                break
            else:
                for si in range(len(s)):
                    if match[pi-1][si] and (cur == '.' or cur == s[si]):
                        match[pi][si+1] = True
            pi += 1

        return match[len(p)][len(s)]


p = "a***b*a***C"
p = ''.join([x[1] for x in filter(lambda x: x[0] == 0 or x[1] != '*' or x[1] != p[x[0]-1], enumerate(p))])
print(p)

s = Solution()
print(s.isMatch('', ''))
print(s.isMatch("", "."))
print(s.isMatch('', 'a*'))
print(s.isMatch('a', 'a*'))
print(not s.isMatch("aa","a"))
print(s.isMatch("aa","aa"))
print(not s.isMatch("aaa","aa"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("aa", ".*"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch('a', 'a*'))
print(s.isMatch('abaaa', 'abaa*'))
print(s.isMatch('ab', 'aba*'))
print(not s.isMatch('sssssssss','a*******'))