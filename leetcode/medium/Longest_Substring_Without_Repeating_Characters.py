# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 22:03

Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        """
        100ms, Your runtime beats 84.85% of python submissions.
        :param s:
        :return:
        """
        if not s:
            return 0

        charIndex = {}
        count = 0
        left = 0
        for i, ch in enumerate(s):
            if ch not in charIndex:
                count = max(count, i-left+1)
            else:
                if charIndex[ch]+1 > left:
                    left = charIndex[ch]+1
                else:
                    count = max(count, i-left+1)
            charIndex[ch] = i

        return count



s = Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"), 5)
print(s.lengthOfLongestSubstring('aab'), 2)
print(s.lengthOfLongestSubstring('ohomm'), 3)
print(s.lengthOfLongestSubstring('eee'), 1)
print(s.lengthOfLongestSubstring('abcabcbb'), 3)
print(s.lengthOfLongestSubstring('abcedfg'), 7)
print(s.lengthOfLongestSubstring('abdcefgdajdioeqjdjieqwji'))
print(s.lengthOfLongestSubstring('assaasdewasadasas'))
