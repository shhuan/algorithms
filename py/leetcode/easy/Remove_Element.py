# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 13:46

Given an array and a value, remove all instances of that value in place and return the new length.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

"""
__author__ = 'huash06'

import sys
import os


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return 0

        l = 0
        for i in range(len(A)):
            if A[i] == elem:
                continue
            A[l] = A[i]
            l += 1
        print(A[:l])
        return l


s = Solution()
print(s.removeElement([1,1,2,3,2,2,4], 2))
print(s.removeElement([], 2))