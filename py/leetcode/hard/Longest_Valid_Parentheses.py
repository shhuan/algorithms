"""

created by huash06 at 2015-04-30


Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools
import random

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        """

        使用一个stack数组存储从当前位置往左的最后一个没匹配的左边括号的位置，
        使用lasts数组存储和位置匹配的左括号的位置。
        假设计算到位置i是右括号，它能够和stack最上面的位置匹配，同时更新lasts[i] = stack[-1]。
        如果stack[-1]的左边个括号能够和以前的括号匹配，那么last[i]也应当能够匹配之前的括号

        :param s:
        :return:
        """
        if not s:
            return 0

        lasts = [i for i in range(len(s))]
        res = 0
        q = []
        for i, ch in enumerate(s):
            if ch == '(':
                q.append(i)
            else:
                if q:
                    last = q.pop()
                    lasts[i] = last
                    if last > 1 and lasts[last-1] != last - 1:
                        lasts[i] = lasts[last-1]
            if lasts[i] != i:
                res = max(res, i-lasts[i]+1)
        # print(lasts)
        return res


s = Solution()
# print(s.longestValidParentheses('()'))

print(s.longestValidParentheses('()((()())('))
print(s.longestValidParentheses('()()'))