# -*- coding: utf-8 -*-

'''
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

'''

import collections
import time

class Solution(object):
    def findSubstringInWraproundString1(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0

        sbs = collections.defaultdict(int)

        for i in range(len(p)):
            s = p[i]

            if i + sbs[s] >= len(p):
                continue
            if p[i + sbs[s]] != chr((ord(p[i]) - ord('a') + sbs[s]) % 26 + ord('a')):
                continue

            l = 1
            for j in range(i + 1, len(p) + 1):
                l = j - i
                if j < len(p) and ord(p[j]) != ord(p[j - 1]) + 1 and not (p[j] == 'a' and p[j - 1] == 'z'):
                    break
            sbs[s] = max(sbs[s], l)

        # print(sbs)

        ret = sum(sbs.values())

        return ret

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        pattern = 'zabcdefghijklmnopqrstuvwxyz'
        cmap = collections.defaultdict(int)
        start = end = 0
        for c in range(len(p)):
            if c and p[c - 1:c + 1] not in pattern:
                for x in range(start, end):
                    cmap[p[x]] = max(end - x, cmap[p[x]])
                start = c
            end = c + 1
        for x in range(start, end):
            cmap[p[x]] = max(end - x, cmap[p[x]])
        return sum(cmap.values())





s = Solution()

print(s.findSubstringInWraproundString("zab"))
print(s.findSubstringInWraproundString("cac"))
print(s.findSubstringInWraproundString("a"))
print(s.findSubstringInWraproundString1("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcghijkl"))
print(s.findSubstringInWraproundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcghijkl"))
st = time.time()
print(s.findSubstringInWraproundString1("vwxyefghijklmnopqrsomnopqrstuvefghijklmklmnopqrsqrstefghijklmnopqpqrstuvwxyzidefghijbcefghijklmnopqrstuvwghijklmnopqrstuvwhijklmnopbcdefghijklmnopopqrstuvwxyzstuvwxyfghijklmnopqrstuvwxyzmnopqrstuvwxyzhijklmnopfghijklfghijklmnopfghijklmnopqrsttuvwxabcdefghijklmnjklmnopqrstuvwxijklmnopabcdefghijklmnopqopqrstuvfghijklmnopqrstuvefghijkklmnopqrstuvabcdefghijklmnopqabcdefklmnopqefghijklmnopqrmbcdefghmnopqrstulnopqrstklmnopqrstuvwstuvnopqrstuvwxytuvwxhijklmnopqrstuvwxyzijklmnopqrstuabcdefghipqrstulabcdefghijklmnopijklmnopqrsabcdefgcdefghijklmnopqfghijklmnopqrfghijklmnohijklmnopqrstuvwxyzabcdhijklmnopqrstuvghijkrstuvwxyzabcdefghijklmnopqrcdefghijklmfghijklmnopqrstuvghijlmnopopqrstuvwxyjklmndefghijklmnopqrstuvwjklmghijklmnopqrstuvwxyfghijklmdefghijklmnopqrstuvwxfghijklmnopqrshijklmnopqcdefghiabcdefghijklmnopqrsttuvwuvwxyzhijklmnofghijkllmnopqrstuvwxnopqrhijklmnopqrstuvwxyzjklmnopqrstuvwxefghiefghijklmnopqrtuvwxpqrstuvklmnabcdefghijklmnopklefghijklmnopqrstuvjklmnopqrsbcdefghijkcdefghijklmfghijklmnopqrstuv"))
print(s.findSubstringInWraproundString("vwxyefghijklmnopqrsomnopqrstuvefghijklmklmnopqrsqrstefghijklmnopqpqrstuvwxyzidefghijbcefghijklmnopqrstuvwghijklmnopqrstuvwhijklmnopbcdefghijklmnopopqrstuvwxyzstuvwxyfghijklmnopqrstuvwxyzmnopqrstuvwxyzhijklmnopfghijklfghijklmnopfghijklmnopqrsttuvwxabcdefghijklmnjklmnopqrstuvwxijklmnopabcdefghijklmnopqopqrstuvfghijklmnopqrstuvefghijkklmnopqrstuvabcdefghijklmnopqabcdefklmnopqefghijklmnopqrmbcdefghmnopqrstulnopqrstklmnopqrstuvwstuvnopqrstuvwxytuvwxhijklmnopqrstuvwxyzijklmnopqrstuabcdefghipqrstulabcdefghijklmnopijklmnopqrsabcdefgcdefghijklmnopqfghijklmnopqrfghijklmnohijklmnopqrstuvwxyzabcdhijklmnopqrstuvghijkrstuvwxyzabcdefghijklmnopqrcdefghijklmfghijklmnopqrstuvghijlmnopopqrstuvwxyjklmndefghijklmnopqrstuvwjklmghijklmnopqrstuvwxyfghijklmdefghijklmnopqrstuvwxfghijklmnopqrshijklmnopqcdefghiabcdefghijklmnopqrsttuvwuvwxyzhijklmnofghijkllmnopqrstuvwxnopqrhijklmnopqrstuvwxyzjklmnopqrstuvwxefghiefghijklmnopqrtuvwxpqrstuvklmnabcdefghijklmnopklefghijklmnopqrstuvjklmnopqrsbcdefghijkcdefghijklmfghijklmnopqrstuv"))
print((time.time() - st) * 1000)