# -*- coding: utf-8 -*-
"""


Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2

"""


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """

        l1 = len(s1)
        l2 = len(s2)
        repeatCount = [0] * (l2+1)
        nextIndex = [0] * (l2+1)

        j, cnt = 0, 0
        for k in range(1, n1+1):
            for i in range(l1):
                if s1[i] == s2[j]:
                    j += 1
                    if j == l2:
                        j = 0
                        cnt += 1
            repeatCount[k] = cnt
            nextIndex[k] = j

            for start in range(k):
                if nextIndex[start] == j: # find a repetition
                    prefixCount = repeatCount[start]
                    patternCount = (repeatCount[k]-repeatCount[start])*((n1-start)//(k-start))
                    suffixCount = repeatCount[start+(n1-start)%(k-start)]-repeatCount[start]
                    return (prefixCount+patternCount+suffixCount) // n2

        return repeatCount[n1] // n2

s = Solution()

# print(s.getMaxRepetitions("abcd", 4, "ab", 2))

print(s.getMaxRepetitions("aaa", 3, "aa", 1))