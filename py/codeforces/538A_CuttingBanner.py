"""

created by huash06 at 2015-05-19

此题过于无聊

"""
__author__ = 'huash06'

import os
import sys
import functools
import collections
import itertools


class Solution:
    def __init__(self):
        self.banner = None

    def readInput(self):
        self.banner = input()

    def readMockInput(self):
        """
        只能划分成三段，取中间一段或者前后两段拼接
        :return:
        """
        # self.banner = 'CODEWAITFORITFORCES'
        # self.banner = 'CODEFZORCES'
        self.banner = 'CCODEFORCESODECODEFORCCODEFORCESODCODEFORCESEFCODEFORCESORCODEFORCESCESCESFORCODEFORCESCES'

    def solve(self):
        expect = 'CODEFORCES'
        for l in range(0, len(expect)+1):
            r = len(expect)-l
            if self.banner[:l]+self.banner[len(self.banner)-r:] == expect:
                print('YES')
                return
        print('NO')
    def solve1(self):
        """
        任意多个字符串片段拼接，不合题意
        :return:
        """
        expect = 'CODEFORCES'

        if len(self.banner) < len(expect):
            print('NO')
            return

        match = 0
        i = 0
        while i < len(self.banner):
            if match >= len(expect):
                print('YES')
                return

            mis = []
            for ei in range(match+1):
                if expect[ei] == self.banner[i]:
                    mis.append(ei)

            if mis:
                for mi in mis:
                    for j in range(i, i+len(expect)-mi):
                        if self.banner[j] == expect[mi]:
                            mi += 1
                            match = max(mi, match)
                            i = j
                        else:
                            break
            i += 1
        if match >= len(expect):
            print('YES')
        else:
            print('NO')



s = Solution()
s.readInput()
# s.readMockInput()
s.solve()