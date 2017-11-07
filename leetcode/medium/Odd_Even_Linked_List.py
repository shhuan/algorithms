# -*- coding: utf-8 -*-

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

使用两个链表分别存奇数和偶数下标的结点，最后再合并
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        oh = ListNode(0)
        ot = oh
        eh = ListNode(0)
        et = eh
        h = head
        odd = True
        while h:
            if odd:
                ot.next = h
                ot = h
            else:
                et.next = h
                et = h
            hnext = h.next
            h.next = None
            h = hnext
            odd = not odd
        ot.next = eh.next

        return oh.next



def list2Nodes(l):
    if not l:
        return None
    result = ListNode(l[0])
    p = result
    for v in l[1:]:
        p.next = ListNode(v)
        p = p.next
    return result

def list2Str(head):
    if not head:
        return ''
    return str(head.val) + ', ' + list2Str(head.next)

s = Solution()

l = list2Nodes([1, 2, 3, 4, 5])
r = s.oddEvenList(l)
print list2Str(r)

l = list2Nodes([2,1,4,3,6,5,7,8])
r = s.oddEvenList(l)
print list2Str(r)




