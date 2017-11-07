# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 13:29

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        """
        比较简单的递归。

        如果s1可以经过变换得到s2。
        假设s1被分割成的左右子树分别是s1[:i]和s1[i:]生成的，
        s1[:i]可能对应s2[:i]也可能对应s2[j:].
        s2被分割成的左右子树分别是s1[:j]和s2[j:]生成的。

        那么有两种情况:
        1. s1[:i]可以经过变换得到s2[:j]且s1[i:]可以经过变换得到s2[j:]
        2. 或者s1[:i]可以经过变换得到s2[j:]且s1[i:]可以经过变换得到s2[:j]


        :param s1:
        :param s2:
        :return:
        """
        if not s1 or not s2:
            return False
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        if ''.join(sorted(list(s1))) != ''.join(sorted(list(s2))):
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                return True
        return False





s = Solution()
print(s.isScramble('rg', 'gr'))
# print(s.isScramble('rgtae', 'great'))
# print(s.isScramble('rgeat', 'great'))
# print(s.isScramble('rgtae', 'gxeat'))