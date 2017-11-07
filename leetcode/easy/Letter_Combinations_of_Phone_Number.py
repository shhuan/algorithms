# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-14 22:12

Letter Combinations of a Phone Number Total Accepted: 36037 Total Submissions: 138681 My Submissions Question Solution
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

__author__ = 'huash06'

import sys
import os


class Solution:
    # @param digits, a string
    # @return a string[]
    def letterCombinations(self, digits):
        if not digits:
            return []

        q = [('', digits)]
        result = list()

        while q:
            pre, dig = q.pop()
            if not dig:
                result.append(pre)
                continue
            rp = Solution.keymap[int(dig[0])]
            for ch in rp:
                q.append((pre+ch, dig[1:]))

        return result

    keymap = {
        1: [],
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z'],
        0: ['_']

    }



s = Solution()
print(s.letterCombinations('23'))