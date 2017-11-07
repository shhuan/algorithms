# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-07 13:29

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections



class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:
            return 0
        rpn = self.toRPN(s)
        # print(rpn)
        return self.calRPN(rpn)

    def toRPN(self, s):
        stack = []
        ret = []
        for i in range(len(s)):
            ch = s[i:i+1]
            if not stack:
                if not ch.isspace():
                    stack.append(ch)
                continue
            if ch.isdigit():
                if stack[-1].isdigit():
                    stack[-1] += ch
                else:
                    stack.append(ch)
            else:
                if stack[-1].isdigit():
                    ret.append(stack.pop())
                if ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    while stack:
                        top = stack.pop()
                        if top != '(':
                            ret.append(top)
                        else:
                            break
                elif ch == '+' or ch == '-':
                    while stack and (stack[-1] == '+' or stack[-1] == '-'):
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
        return int(stack[0])


s = Solution()
print(s.calculate("1 + 1"))
print(s.calculate(" 2-1 + 2 "))
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))

print(s.calculate("(132+(14+15+22)-33)+(6+8)"))
print(s.calculate(' 0 '))





