"""

created by huash06 at 2015-04-30

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        if not s or not t:
            return ''

        left = 0
        right = 0
        resleft = -1
        resright = len(s)
        count = collections.defaultdict(int)
        expect = collections.defaultdict(int)
        for ch in t:
            expect[ch] += 1
        foundCount = 0
        while right < len(s):
            if s[right] in t:
                ch = s[right]
                count[ch] += 1
                foundCount += 1
                if count[ch] >= expect[ch]:
                    while left < right:
                        if s[left] in t:
                            ch = s[left]
                            if count[ch] > expect[ch]:
                                left += 1
                                count[ch] -= 1
                                foundCount -= 1
                            else:
                                break
                        else:
                            left += 1
                if foundCount >= len(t):
                    found = True
                    for ch, c in expect.items():
                        if count[ch] < c:
                            found = False
                            break

                    if found and right - left < resright - resleft:
                            resleft = left
                            resright = right
            right += 1
        if resleft < 0:
            return ''

        return s[resleft: resright+1]


s = Solution()
print(s.minWindow('caae', 'cae'))
print(s.minWindow('ADOBECODEBANC', 'ABC'))
print(s.minWindow('a', 'a'))
print(s.minWindow('ab', 'a'))
print(s.minWindow('ab', 'b'))
print(s.minWindow('aa', 'aa'))