# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-08 14:27


Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back,
peek/pop from front, size, and is empty operations are valid.

Depending on your language, queue may not be supported natively.
You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.

You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = []
        self.q2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q1.append(x)

    # @return nothing
    def pop(self):
        if len(self.q1) > 0:
            while len(self.q1) > 1:
                # pop(0) equals popFront in queue
                # append equals pushBack in queue
                self.q2.append(self.q1.pop(0))
            self.q1.pop()
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.pop(0))
            self.q2.pop()


    # @return an integer
    def top(self):
        if len(self.q1) > 0:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            ret = self.q1.pop()
            self.q2.append(ret)
            return ret
        elif len(self.q2) > 0:
            while len(self.q2) > 1:
                self.q1.append(self.q2.pop(0))
            ret = self.q2.pop()
            self.q1.append(ret)
            return ret
        else:
            return None


    # @return an boolean
    def empty(self):
        return len(self.q1) == 0 and len(self.q2) == 0


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
s.pop()
print(s.top())
s.push(5)
s.push(6)
print(s.top())