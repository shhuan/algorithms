# -*- coding: utf-8 -*-

"""


Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""

import collections
import heapq

class LFUCache(object):
    def __init__(self, capacity):
        """

        :type capacity: int
        """
        self.cap = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.connect(self.tail)
        # use to record the first ListNode of this count number
        self.cnt = {0: self.tail}
        # key: key , value:[ListNode, visit count]
        self.kv = {None: [self.tail, 0]}

    def moveforward(self, key):
        node, cnt = self.kv[key]
        self.add('tmp', node.val, cnt + 1)
        self.remove(key)
        self.kv[key] = self.kv['tmp']
        self.kv[key][0].key = key
        del self.kv['tmp']

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.kv:
            return -1
        self.moveforward(key)
        return self.kv[key][0].val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            return
        if key in self.kv:
            self.kv[key][0].val = value
            self.moveforward(key)
            return
        if len(self.kv) > self.cap:
            self.remove(self.tail.prev.key)
        self.add(key, value, 0)

    def remove(self, key):
        node, cnt = self.kv[key]
        if self.cnt[cnt] != node:
            node.prev.connect(node.next)
        elif self.kv[node.next.key][1] == cnt:
            node.prev.connect(node.next)
            self.cnt[cnt] = self.cnt[cnt].next
        else:
            node.prev.connect(node.next)
            del self.cnt[cnt]
        del self.kv[key]

    def add(self, key, value, cnt):
        if cnt in self.cnt:
            loc = self.cnt[cnt]
        else:
            loc = self.cnt[cnt - 1]
        node = ListNode(key, value)
        loc.prev.connect(node)
        node.connect(loc)
        self.cnt[cnt] = node
        self.kv[key] = [node, cnt]




cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
print(cache.get(3))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))