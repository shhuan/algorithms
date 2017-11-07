"""

created by huash06 at 2015-04-29

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools
import random
import datetime
from operator import attrgetter
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def output(self):
        # print(self.val, end='->')
        # sys.stdout.write('{}->'.format(self.val))
        # if self.next:
        #     self.next.output()
        res = []
        h = self
        while h:
            res.append(h.val)
            h = h.next
        print(', '.join(map(str, res)))

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists:
            return []

        head = lists[0]
        for i in range(1, len(lists)):
            h1 = head
            h2 = lists[i]
            tmp = ListNode(0)
            h = tmp
            while h1 and h2:
                if h1.val > h2.val:
                    h.next = h2
                    h2 = h2.next
                else:
                    h.next = h1
                    h1 = h1.next
                h = h.next
            if h1:
                h.next = h1
                h = h1
                while h.next:
                    h = h.next
            if h2:
                h.next = h2
                h = h2
                while h.next:
                    h = h.next
            head = tmp.next
        return head
    def mergeKLists_Builtin(self, lists):
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None

    def mergeKLists_Heap(self, lists):
        if not lists:
            return None

        dummyNode = cur = ListNode(0)
        minHeap = [(l.val, l) for l in lists if l]
        heapq.heapify(minHeap)

        while minHeap:
            cur.next = heapq.heappop(minHeap)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(minHeap, (cur.next.val, cur.next))

        return dummyNode.next

sys.setrecursionlimit(2000)
s = Solution()
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)


l2 = ListNode(6)
l2.next = ListNode(7)
l2.next.next = ListNode(9)


l3 = ListNode(4)
l3.next = ListNode(6)
l3.next.next = ListNode(11)

res = s.mergeKLists([l1, l2, l3])
res.output()
print('')

lists = [None] * 1000
for i in range(len(lists)):
    l = ListNode(1)
    h = l
    pre = 1
    for j in range(1):
        v = random.randint(pre, pre+1000)
        h.next = ListNode(v)
        pre = v
        h = h.next
    lists[i] = l

startTime = datetime.datetime.now()
res = s.mergeKLists(lists)
# res.output()
print('Time Cost: {}'.format(datetime.datetime.now()-startTime))


startTime = datetime.datetime.now()
res = s.mergeKLists_Builtin(lists)
print('Time Cost: {}'.format(datetime.datetime.now()-startTime))

startTime = datetime.datetime.now()
res = s.mergeKLists_Heap(lists)
print('Time Cost: {}'.format(datetime.datetime.now()-startTime))