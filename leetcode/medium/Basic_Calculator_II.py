# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-07 15:21

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections
import re



class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:
            return 0
        exp = self.prepare(s)
        # print(exp)
        rpn = self.toRPN(exp)
        # print(rpn)
        return self.calRPN(rpn)


    def prepare(self, s):
        if not s:
            return None

        s = re.sub('\\s+', '', s)
        exp = []
        i = 0
        for j in range(len(s)):
            ch = s[j:j+1]
            if not ch.isdigit():
                if i != j:
                    exp.append(s[i:j])
                exp.append(ch)
                i = j + 1
        if i < len(s):
            exp.append(s[i: len(s)])

        return exp

    def toRPN(self, s):
        stack = []
        ret = []
        for ch in s:
            if ch.isdigit():
                ret.append(ch)
            else:
                if ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    while stack:
                        top = stack.pop()
                        if top != '(':
                            ret.append(top)
                        else:
                            break
                elif ch in {'+', '-'}:
                    while stack and stack[-1] in {'+', '-', '*', '/'}:
                        ret.append(stack.pop())
                    stack.append(ch)
                elif ch in {'*', '/'}:
                    while stack and stack[-1] in {'*', '/'}:
                        ret.append(stack.pop())
                    stack.append(ch)
        while stack:
            ret.append(stack.pop())
        return ret

    def calRPN(self, rpn):
        stack = []
        for s in rpn:
            if not stack:
                stack.append(s)
                continue
            if s.isdigit():
                stack.append(s)
            else:
                rv = int(stack.pop())
                lv = int(stack.pop())
                if s == '+':
                    stack.append(lv+rv)
                elif s == '-':
                    stack.append(lv - rv)
                elif s == '*':
                    stack.append(lv * rv)
                elif s == '/':
                    stack.append(lv // rv)
        return int(stack[0])


s = Solution()
print(s.calculate("1 + 1"))
print(s.calculate(" 2-1 + 2 "))
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))

print(s.calculate("(132+(14+15+22)-33)+(6+8)"))
print(s.calculate(' 0 '))

print(s.calculate('3+2*2'))
print(s.calculate(' 3/2 '))
print(s.calculate(' 3+5 / 2 '))

