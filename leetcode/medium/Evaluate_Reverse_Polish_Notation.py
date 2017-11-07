# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 20:11

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if not tokens:
            return 0

        q = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                rv = q.pop()
                lv = q.pop()
                if token == '+':
                    q.append(lv + rv)
                elif token == '-':
                    q.append(lv - rv)
                elif token == '*':
                    q.append(lv * rv)
                elif token == '/':
                    # 注意地板除法
                    negative = False
                    if lv < 0:
                        negative = not negative
                        lv = -lv
                    if rv < 0:
                        negative = not  negative
                        rv = -rv
                    dv = lv // rv
                    if negative:
                        dv = -dv
                    q.append(dv)
            else:
                q.append(int(token))
        return q[0]


s = Solution()
print(s.evalRPN(["4","-2","/","2","-3","-","-"]))
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(s.evalRPN(["18"]))