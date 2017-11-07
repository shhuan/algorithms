# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 21:59

Given a string s and a dictionary of words dict, add spaces in s to
construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
__author__ = 'huash'

import sys
import os
import collections

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []
        if not self.wordBreak1(s, wordDict):
            return []
        minWordLen = min([len(x) for x in wordDict])
        return self.dfs(s, 0, wordDict, minWordLen, '')

    def dfs(self, s, si, wordDict, minWordLen, sentence):
        # print(si, sentence)
        if si >= len(s):
            return [sentence]
        if len(s)-si < minWordLen:
            return []

        res = []
        for j in range(si+minWordLen, len(s)+1):
            if s[si:j] in wordDict:
                res.extend(self.dfs(s, j, wordDict, minWordLen, sentence+' '+s[si:j] if sentence else s[si:j]))
        return res

    def wordBreak1(self, s, dict):
        if not s or not dict:
            return False

        valid = [False for i in range(len(s))]
        for i in range(len(s)):
            if s[:i+1] in dict:
                valid[i] = True
                continue
            for j in range(i):
                if valid[j] and s[j+1:i+1] in dict:
                    valid[i] = True
                    break

        return valid[len(s)-1]


    def dpBasedOnWordBreak1(self, s, wordDict):
        if not s or not wordDict:
            return []

        valid = collections.defaultdict(list)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                valid[i].append(-1)
            for j in range(i):
                if valid[j] and s[j+1:i+1] in wordDict:
                    valid[i].append(j)

        if not valid[len(s)-1]:
            return []
        return self.dfs2(s, len(s)-1, valid, '')

    def dfs2(self, s, si, valid, sentence):
        if si < 0:
            return [sentence]

        res = []

        for pi in valid[si]:
            res.extend(self.dfs2(s, pi, valid, s[pi+1:si+1]+' '+sentence if sentence else s[pi+1:si+1]))

        return res





s = Solution()
print(s.wordBreak('a', {}))
print(s.wordBreak('catsanddog', {"cat", "cats", "and", "sand", "dog"}))
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))

print(s.dpBasedOnWordBreak1('a', {}))
print(s.dpBasedOnWordBreak1('catsanddog', {"cat", "cats", "and", "sand", "dog"}))
print(s.dpBasedOnWordBreak1("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))



