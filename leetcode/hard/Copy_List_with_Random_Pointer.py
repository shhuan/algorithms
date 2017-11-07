# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-02 23:23

A linked list is given such that each node contains an additional
random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
__author__ = 'huash'

import sys
import os

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    def output(self):
        print('({}, {})'.format(self.label, self.random.label if self.random else 'Nan'), end='->')
        if self.next:
            self.next.output()

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        res = RandomListNode(0)
        mirror = {}
        h = head
        rh = res
        while h:
            rhnext = mirror.get(h)
            if not rhnext:
                rhnext = RandomListNode(h.label)
                mirror[h] = rhnext
            rh.next = rhnext
            rnd = h.random
            if rnd:
                resrnd = mirror.get(rnd)
                if not resrnd:
                    resrnd = RandomListNode(rnd.label)
                    mirror[rnd] = resrnd
                rh.next.random = resrnd
            rh = rh.next
            h = h.next
        res = res.next

        return res


s = Solution()

l = RandomListNode(0)
l1 = RandomListNode(1)
l2 = RandomListNode(2)
l3 = RandomListNode(3)
l.next = l1
l1.next = l2
l2.next = l3

l.random = l3
l1.random = l1
# l2.random =
l3.random = l1

l.output()
print()

lc = s.copyRandomList(l)
lc.output()








