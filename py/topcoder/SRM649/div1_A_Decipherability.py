# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-06-19 14:36


Problem Statement
You have a string s that contains at least K characters. Cat Snuke will remove exactly K characters from the string.
Afterwards, Snuke will show you the new string and you have to guess the original indices of all removed characters.
You win the game if you guess all of them correctly.

For example, suppose that s="snuke" and K=2. Snuke removed two characters and showed you the string "nue".
In this situation you can easily deduce that Snuke must have removed the characters s[0] and s[3].
You announce that the indices of removed characters are 0 and 3, and you win the game.

You are given the s and the K. Return "Certain" (quotes for clarity) if you can always be sure to win the game,
regardless of which characters Snuke removes. Otherwise, return "Uncertain". Note that the return value is case-sensitive.


Definition
Class: Decipherability
Method: check
Parameters: string, integer
Returns: string
Method signature: def check(self, s, K):


Limits
Time limit (s): 2.000
Memory limit (MB): 256


Constraints
- K will be between 1 and 50, inclusive.
- The length of s will be between K and 50, inclusive.
- Every character in s will be a lowercase letter ('a'-'z').

如果s[i]==s[j]，那么同时移除[i+1,j-1]之间的所有元素，然后移除s[i]或者s[j]得到的
结果一样，即只要存在s[i]==s[j] and j-i <= K，结果不确定

"""
__author__ = 'huash06'


import datetime
import sys
import functools
import collections

class Decipherability:
    def check(self, s, K):
        N = len(s)
        if K >= N:
            return 'Certain'

        for i in range(N):
            for j in range(i+1, N):
                if s[i] == s[j] and j - i <= K:
                    return 'Uncertain'

        return 'Certain'



s = Decipherability()
print(s.check('snuke', 2))
print(s.check('aba', 1))
print(s.check('aba', 2))
print(s.check('abcdabcd', 3))
print(s.check('koukyoukoukokukikou', 2))
print(s.check('wolfsothe', 8))
print(s.check('aa', 2))

# @functools.lru_cache(maxsize=None)
# def comp(n, i):
#     if i >= n:
#         return 1
#     if i == 0:
#         return 1
#     if i == 1:
#         return n
#     return comp(n-1, i)+comp(n-1,i-1)
# print(comp(5, 2))
# c = collections.defaultdict(list)
# for i in range(51):
#     for j in range(i):
#      c[comp(i, j)].append((i, j))
#
# cm = max(c.keys())
# print(cm, c[cm])
