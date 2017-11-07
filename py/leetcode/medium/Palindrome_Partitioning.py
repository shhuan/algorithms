# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 21:18



Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

"""

__author__ = 'huash06'

import sys
import os


class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s:
            return []

        result = []
        for i in range(1, len(s)):
            if self.isPalindrome(s[:i]):
                pds = self.partition(s[i:])
                if pds:
                    for pd in pds:
                        result.append([s[0:i]]+pd)
        if self.isPalindrome(s):
            result.append([s])

        # print('result of {} is {}'.format(s, result))
        return result



    def isPalindrome(self, s):
        if not s:
            return False

        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                # print('{} is not a palinderome'.format(s))
                return False

        # print('{} is palinderome'.format(s))
        return True



s = Solution()
print(s.partition('aab'))