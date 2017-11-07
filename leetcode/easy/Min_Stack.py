# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 10:21

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""
__author__ = 'huash'

import sys
import os
import random

class MinStack:
    def __init__(self):
        self.data = []
        self.min_val = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.data.append(x)
        if not self.min_val or x < self.min_val[-1]:
            self.min_val.append(x)
        else:
            self.min_val.append(self.min_val[-1])

    # @return nothing
    def pop(self):
        if not self.data:
            return
        self.min_val.pop()
        self.data.pop()

    # @return an integer
    def top(self):
        if not self.data:
            return None
        return self.data[-1]

    # @return an integer
    def getMin(self):
        if not self.min_val:
            return None
        return self.min_val[-1]


s = MinStack()

for i in range(10):
    val = random.randint(1, 20)
    s.push(val)
    print('PUSH {}'.format(val))
    print('MIN {}'.format(s.getMin()))
    val = random.randint(1, 10)
    if val > 7:
        s.pop()
        print('POP')
        print('MIN {}'.format(s.getMin()))
while s.pop():
    print('POP')
    print('MIN {}'.format(s.getMin()))