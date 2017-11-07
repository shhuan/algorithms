# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-13 13:18

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n)
to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

"""
__author__ = 'huash06'

import sys
import os
import bisect

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        """
        把A中的元素全部移动到右边，然后从两个数组中挑选当前最小的元素放到数组左边
        :param A:
        :param m:
        :param B:
        :param n:
        :return:
        """

        # 这两句52ms， beats 84.97% of python coders
        # 但是应该不是题目考察的重点
        # A[m:] = B[:]
        # A.sort()

        # 68ms, 13.07% of python coders.
        # A[len(A)-m:] = A[:m]
        #
        # ai = n
        # bi = 0
        # i = 0
        # while ai < m+n and bi < n:
        #     if A[ai] <= B[bi]:
        #         A[i] = A[ai]
        #         ai += 1
        #     else:
        #         A[i] = B[bi]
        #         bi += 1
        #     i += 1
        # r = m+n-ai+i
        # A[i: r] = A[ai: m+n]
        # A[r: r+n-bi] = B[bi:]


        # 52 ms, 84.97% of python coders
        # 从数组B当中选出最大的未找到位置的元素，
        # 在数组A当中找到它可以插入的位置，
        # 把数组A当中插入位置之后的元素全部后移
        #   A = [1,6,7,0,0,0]
        #   B = [2,5,6]
        #   开始时挑出B[2]=6
        #   在A中插入在7之前，把7移到最后A=[1, 6, 0, 0, 0, 7]
        #   插入6，A=[1, 6, 0, 0, 0, 6, 7]
        #   挑出B的下一个元素B[1]=5
        #   在A中应该插入在6之前，把6移到最后 A=[1, 0, 0, 0, 6, 7]
        #   插入5，A=[1, 0, 5, 6, 6, 7]
        #   挑出B的下一个元素B[0]=2
        #   应该插入在1之后，没有元素右移
        #   插入2，A=[1, 2, 5, 6, 6, 7]
        #

        ai = m
        r = m + n
        for bi in range(n-1, -1, -1):
            i = bisect.bisect_right(A, B[bi], 0, ai)
            next_r = r-ai+i
            A[next_r: r] = A[i: ai]
            ai = i
            r = next_r - 1
            A[r] = B[bi]






s = Solution()

A = [1,6,7,0,0,0]
B = [2,5,6]
s.merge(A, 3, B, 3)
print(A)