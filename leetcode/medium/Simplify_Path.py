# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 11:03

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import re

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        if not path:
            return ''
        start = '/' if path[0] == '/' else ''
        path = path.split('/')
        q = []
        for p in path:
            if p == '..':
                if q:
                    q.pop()
            elif p == '.':
                pass
            elif p == '':
                pass
            else:
                q.append(p)
        path = '/'.join(q)
        return start+path


s = Solution()
print(s.simplifyPath('//a//b/./c'))
print(s.simplifyPath('/./a/./c'))
print(s.simplifyPath('../a/b//c/./../d'))
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath('/home/'))
print(s.simplifyPath('/../'))
print(s.simplifyPath('/home//foo'))
print(s.simplifyPath('////'))