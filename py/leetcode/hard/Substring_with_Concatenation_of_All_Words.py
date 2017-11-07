"""

created by huash06 at 2015-04-30


You are given a string, s, and a list of words, words,
that are all of the same length. Find all starting indices of substring(s)
in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        res = []
        wl = len(words[0])
        si = 0
        wc = collections.defaultdict(int)
        for word in words:
            wc[word] += 1

        while si < len(s)-wl*len(words)+1:
            if self.isMatch(s, si, words, wl, wc):
                res.append(si)
                # si += wl*len(words)
                # si += wl * len(wc)
            # else:
            #     si += 1
            si += 1
        return res

    def isMatch(self, s, si, words, wl, wc):
        match = collections.defaultdict(int)
        for i in range(si, si+len(words)*wl, wl):
            word = s[i: i+wl]
            if word in words:
                match[word] += 1
                if match[word] > wc[word]:
                    return False
            else:
                return False

        return len(list(filter(lambda x: x[1] < wc[x[0]], match.items()))) == 0


s = Solution()
print(s.findSubstring("aaaaaaaa", ["aa", "aa", "aa"]))
# print(s.findSubstring('aaa', ['a', 'a']))
# print(s.findSubstring('a', ['a']))
# print(s.findSubstring('barfoothefoobarman', ['foo', 'bar']))
# print(s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))