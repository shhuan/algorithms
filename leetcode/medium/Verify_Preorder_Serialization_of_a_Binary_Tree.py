# -*- coding: utf-8 -*-

"""


One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

"""

import time
class Solution(object):

    def isValidSerialization(self, preorder):
        stack = []
        top = -1
        preorder = preorder.split(',')
        for s in preorder:
            stack.append(s)
            top += 1
            while (self.endsWithTwoHashes(stack, top)):
                h = stack.pop()
                top -= 1
                h = stack.pop()
                top -= 1
                if top < 0:
                    return False
                h = stack.pop()
                stack.append('#')
                # print stack
        if len(stack) == 1:
            if stack[0] == '#':
                return True
        return False

    def endsWithTwoHashes(self, stack, top):
        if top < 1:
            return False
        if stack[top] == '#' and stack[top - 1] == '#':
            return True
        return False
    def isValidSerialization2(self, preorder):
        """
        TLE
        :type preorder: str
        :rtype: bool
        """

        memo = {}

        def check(a, l, r):
            if l >= r:
                return False

            if l == r - 1:
                return a[l] == '#'

            if a[l] == '#':
                return False

            k = (l, r)
            if k in memo:
                return memo[k]

            for m in range(l + 2, r + 1, 2):
                if a[m-1] == a[r-1] == '#':
                    if check(a, l + 1, m) and check(a, m, r):
                        memo[k] = True
                        return True

            memo[k] = False
            return False

        preorder = preorder.split(',')
        return check(preorder, 0, len(preorder))



s = Solution()
print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
t0 = time.time()
print(s.isValidSerialization("9,9,9,9,#,9,9,9,9,#,#,9,9,9,9,#,#,9,#,9,9,#,#,#,9,#,9,#,#,9,9,#,#,#,9,#,#,9,#,9,#,9,#,#,9,9,#,9,#,#,#,9,9,9,9,9,#,9,#,#,9,#,9,#,#,9,9,9,#,#,#,9,#,#,9,9,9,9,#,9,#,#,9,9,#,#,#,#,#,9,9,9,9,9,9,#,#,#,9,9,#,#,9,9,#,9,#,#,9,9,#,#,9,#,#,9,9,9,9,#,#,#,9,9,9,9,9,#,#,#,#,9,#,#,#,9,9,9,#,9,#,9,9,#,#,#,9,#,9,#,9,9,#,#,#,9,#,9,9,#,#,#,9,9,9,#,#,9,#,#,9,9,9,9,#,#,9,9,#,#,9,9,#,#,9,#,9,#,#,9,9,9,9,#,9,#,9,#,#,9,#,#,9,#,#,9,#,#,9,#,9,9,9,9,#,#,#,9,9,#,#,9,#,#,9,9,#,#,#,9,9,9,9,9,#,9,9,#,9,#,#,9,9,#,9,#,#,9,#,#,9,9,9,9,9,9,9,9,9,#,#,#,#,#,#,9,#,9,9,#,#,#,9,#,9,#,9,#,#,9,9,9,9,#,9,9,#,#,9,9,9,#,#,#,#,#,#,#,9,9,9,#,#,9,#,#,9,9,#,#,9,#,#,9,9,9,#,#,#,9,9,#,9,9,#,#,9,#,#,9,9,9,9,#,#,#,9,9,#,#,9,9,#,9,#,9,#,#,9,#,#,9,9,9,#,9,#,#,9,#,#,9,#,9,#,#,9,9,9,9,9,9,#,#,9,#,#,#,9,9,#,9,9,#,9,9,#,#,#,9,9,#,#,#,9,#,#,9,9,9,#,#,9,#,#,9,9,9,9,#,9,#,9,#,#,9,9,#,#,#,9,#,#,9,#,#,9,9,#,9,9,9,9,#,#,9,#,#,9,9,#,9,#,#,#,9,9,#,9,#,#,9,#,#,9,9,#,#,9,#,9,9,#,#,9,9,9,#,#,9,9,#,#,#,9,#,9,#,9,9,#,#,#,9,9,9,#,#,9,#,#,9,#,#,9,9,9,9,9,9,9,9,9,9,#,#,#,9,#,#,9,#,#,9,9,9,9,#,#,9,#,#,9,9,9,#,#,9,#,#,9,9,#,9,#,#,9,#,#,9,#,#,#,9,9,#,9,#,#,9,#,9,#,#,9,9,9,9,9,#,9,#,#,9,#,#,9,9,9,9,9,9,#,#,9,#,#,9,9,#,#,9,#,9,#,9,9,#,#,#,9,#,9,9,9,9,#,#,#,#,9,9,9,9,#,#,#,9,#,#,9,#,#,9,9,9,9,9,#,#,#,#,#,9,#,9,9,9,#,9,#,#,9,9,#,#,#,9,9,#,#,#,#,#,9,9,9,9,#,9,9,9,9,9,9,#,9,#,9,#,#,#,9,#,#,9,#,#,#,#,9,9,9,#,9,#,#,#,#,9,#,9,9,9,#,#,9,#,#,9,9,#,#,9,9,#,9,#,#,9,#,#,9,9,9,9,9,#,#,9,9,9,9,9,#,#,9,#,#,9,9,9,9,#,#,#,#,9,#,#,9,#,9,#,#,9,9,9,#,#,9,9,9,9,9,#,9,#,#,9,#,9,#,#,9,#,#,#,9,9,9,9,9,#,#,#,#,9,9,9,#,#,#,#,9,9,#,#,#,9,9,9,9,#,9,#,#,9,#,#,9,9,#,#,9,#,9,#,#,9,#,#,9,9,9,#,#,9,9,9,9,9,#,#,9,#,#,9,9,#,#,9,9,#,#,#,9,#,9,9,#,9,#,9,9,#,#,9,#,#,#,9,9,9,#,9,#,#,#,#,9,9,#,9,#,#,9,#,#,9,9,#,#,#,9,9,9,#,9,9,#,#,9,9,#,#,#,9,#,9,9,9,#,#,9,#,#,#,9,9,9,9,#,#,9,#,#,9,9,#,#,9,9,#,#,9,#,#,9,9,9,9,9,#,#,9,#,#,9,#,#,9,9,#,#,9,9,#,9,9,9,#,#,#,#,#,9,9,9,9,#,#,9,9,#,#,9,#,#,9,#,#,9,#,#,9,#,9,9,#,9,#,#,9,9,#,9,9,9,9,#,9,9,#,#,#,9,9,#,9,9,#,9,#,#,9,#,#,9,#,#,9,9,#,#,9,#,#,#,9,9,9,#,#,#,9,9,9,#,#,9,#,#,9,9,#,#,#,9,9,9,#,#,#,9,9,9,#,#,9,9,9,9,9,#,#,9,#,#,9,9,#,#,#,9,#,#,9,9,9,9,#,9,#,#,9,9,#,#,9,#,#,9,#,9,#,#,9,9,#,#,9,#,#,9,9,9,#,9,#,#,9,#,#,9,9,#,9,9,#,#,9,9,#,#,9,#,#,9,#,#"))
print(time.time() - t0)
