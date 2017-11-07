"""

created by huash06 at 2015-04-30

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools


class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        """
        f(i, j, k) 表示s1的前i个字符和s2的前j个字符可以组成s3的前k个字符。
        f(0, 0, 0) = True 表示2个空字符串组成一个空字符串。
        如果f(len(s1), len(s2), len(s3) == True，表示s1和s2能够组成s3。

        如果f(i, j, k) = True
        1, if s1[i] == s3[k], f(i+1, j, k+1) = True
        2, if s2[j] == s3[k], f(i,  j+1, k+1) = True
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False

        # 直接使用三维数组内存使用过大，
        # 这里纪录所有能够匹配s3[:k]的i，j，即所有的f(i, j, k)==True的i和j
        match = collections.defaultdict(set)
        match[0].add((0, 0))
        g = [False] * (len(s3)+2)
        g[0] = True

        for k in range(len(s3)+1):
            for m in match[k]:
                ii = m[0]
                jj = m[1]
                if ii < len(s1) and s1[ii] == s3[k]:
                    match[k+1].add((ii+1, jj))
                if jj < len(s2) and s2[jj] == s3[k]:
                    match[k+1].add((ii, jj+1))
            # 删除不需要的纪录，保证内存不超标
            if k > 0:
                del match[k-1]

        return len(match[len(s3)]) > 0



s = Solution()
print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
print(s.isInterleave("baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab", "aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb", "babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab"))
print(s.isInterleave("abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb", "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc", "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"))