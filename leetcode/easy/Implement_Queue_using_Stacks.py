# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-07 21:29


Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top,
peek/pop from top, size, and is empty operations are valid.

Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.

You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.data1 = []
        self.data2 = []

    def __str__(self):
        return '{} {}'.format(self.data1, self.data2)

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data1.append(x)

    # @return nothing
    def pop(self):
        if self.data2:
            self.data2.pop()
        else:
            while self.data1:
                self.data2.append(self.data1.pop())
            if self.data2:
                self.data2.pop()

    # @return an integer
    def peek(self):
        if self.data2:
            return self.data2[-1]
        else:
            while self.data1:
                self.data2.append(self.data1.pop())
            if self.data2:
                return self.data2[-1]
        return None

    # @return an boolean
    def empty(self):
        return len(self.data1) == 0 and len(self.data2) == 0


q = Queue()

q.push(1)
q.push(2)
q.push(3)
q.pop()
print(q)
print(q.peek())
q.push(4)
q.pop()
print(q)
