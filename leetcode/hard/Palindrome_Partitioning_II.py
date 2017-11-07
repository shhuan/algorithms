# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 20:58

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
__author__ = 'huash'

import sys
import os

class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        # print(s)
        if not s or self.isPalindrome(s):
            return 0

        pad = [[False for c in range(len(s))] for r in range(len(s))]
        for i in range(len(s)):
            for j in range(i, (len(s))):
                if self.isPalindrome(s[i:j+1]):
                    pad[i][j] = True

        cut = [[1000000 for c in range(len(s))] for r in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                if pad[i][j]:
                    cut[i][j] = 0

        for gap in range(2, len(s)):
            for i in range(len(s)-gap):
                j = i + gap
                c = min(j-i, cut[i][j])
                for k in range(i, j):
                    c = min(c, cut[i][k] + cut[k+1][j] + 1)
                cut[i][j] = c
        return cut[0][len(s)-1]


    def calSpan(self, s, a, b):
        """
        更快的判断s[a: b+1]是否是回文的方法
        :param s:
        :param a:
        :param b:
        :return:
        """
        while a >= 0 and b < len(s) and s[a] == s[b]:
            a -= 1
            b += 1
        return b - 1 - (a + 1)

    def minCut2(self, s):
        if not s:
            return 0

        span = [0] * (len(s) * 2)
        for i in range(len(s)):
            a, b = i, i
            span[a + b] = self.calSpan(s, a, b)
            if i < len(s) - 1:
                a, b = i, i+1
                span[a + b] = self.calSpan(s, a, b)
        # print(span)

        cut = [i for i in range(len(s))]
        for j in range(len(s)):
            # if self.isPalindrome(s, 0, j):
            if span[j] >= j:
                cut[j] = 0
                continue
            for i in range(j+1):
                # if self.isPalindrome(s, i, j):
                if span[i+j] >= j - i:
                    cut[j] = min(cut[j], cut[i-1] + 1)
        # print(cut)
        return cut[len(s)-1]


    def isPalindrome(self, s, ss, se):
        if not s:
            return True
        for i in range((se-ss) // 2 + 1):
            if s[ss+i] != s[se-i]:
                return False
        return True


s = Solution()
print(s.isPalindrome('abbcbbe', 1, 4))
# print(s.minCut('aab'))
# print(s.minCut('aabaa'))
# print(s.minCut('abc'))
# print(s.minCut('aaabaa'))
# print(s.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))
# print(s.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))



print(s.minCut2('aab'))
print(s.minCut2('aabaa'))
print(s.minCut2('abc'))
print(s.minCut2('aaabaa'))
print(s.minCut2("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"))
print(s.minCut2("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))
print(s.minCut2("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))