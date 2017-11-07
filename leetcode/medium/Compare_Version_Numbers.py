# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 09:24
"""
__author__ = 'huash'

import sys
import os



class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')

        len1 = len(v1)
        len2 = len(v2)

        if len1 > len2:
            for i in range(len1-len2):
                if int(v1[i]) > 0:
                    return 1
            v1 = v1[len1-len2:]
        elif len1 < len2:
            for i in range(len2-len1):
                if int(v2[i]) > 0:
                    return -1
            v2 = v2[len2-len1:]

        print(v1)
        print(v2)

        for i in range(len(v1)):
            val1 = int(v1[i])
            val2 = int(v2[i])
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
        return 0

s = Solution()
print(s.compareVersion('0.1', '0.0.1'))
print(s.compareVersion('0.1', '1.1'))
print(s.compareVersion('1.2', '13.7'))
print(s.compareVersion('1.2.3', '3.4'))
print(s.compareVersion('0.2.3', '3.4'))
print(s.compareVersion('0.1', '1.0'))
