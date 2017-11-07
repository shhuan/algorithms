# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-28 10:37

Given an array with n objects colored red, white or blue, sort them
so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's,
then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?




"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A or len(A) <= 1:
            return
        i0 = -1
        i1 = -1
        for i in range(len(A)):
            if A[i] == 1:
                i1 += 1
                A[i1], A[i] = A[i], A[i1]
            elif A[i] == 0:
                i0 += 1
                A[i0], A[i] = A[i], A[i0]
                if i1 >= i0:
                    i1 += 1
                    A[i1], A[i] = A[i], A[i1]
                else:
                    i1 = i0


a = [0, 1, 2, 0, 2, 2, 1, 1, 0, 2]
s = Solution()
s.sortColors(a)
print(a)