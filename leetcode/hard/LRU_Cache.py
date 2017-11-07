# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-02 22:33

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key
if the key exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.


使用双向链表和HashMap实现
"""
__author__ = 'huash'

import sys
import os
import collections



class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.dicts = {}
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        res = -1
        tmphead = self.dicts.get(key)
        if tmphead != None:
            res = tmphead.val
            self.movetohead(tmphead)

        return res

    def movetohead(self, tmphead):
        if self.head != tmphead:
            tmphead.pre.next = tmphead.next
            if self.tail != tmphead:
                tmphead.next.pre = tmphead.pre
            else:
                self.tail = self.tail.pre
            tmphead.next = self.head
            self.head.pre = tmphead
            self.head = tmphead
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        tmphead = self.dicts.get(key)
        if tmphead != None:
            tmphead.val = value
            self.movetohead(tmphead)

        else:
            tmphead = Node(key, value)

            if len(self.dicts) == self.capacity:
                self.dicts.pop(self.tail.key)
                if self.tail.pre:
                    self.tail.pre.next = None
                    self.tail = self.tail.pre
                else:
                    self.tail = tmphead

            if self.head != None:
                tmphead.next = self.head
                self.head.pre = tmphead
                self.head = tmphead
            else:
                self.head = tmphead
                self.tail = tmphead

            self.dicts[key] = tmphead


s = LRUCache(3)
kvs = [(4, 4), (3, 3), (4, 4), (2, 2), (3, 3), (1, 1), (4, 4), (2, 2)]

for k, v in kvs:
    s.set(k, v)

    print(s.data)
    print(s.lru)

s = LRUCache(1)
s.set(2, 1)
s.get(2)
s.set(3, 2)
s.get(2)
s.get(3)