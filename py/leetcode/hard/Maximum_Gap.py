# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-28 19:27


Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

"""
__author__ = 'huash'

import sys
import os
# import py.lib.TreeViewer as TreeViewer
import math

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def __getattr__(self, item):
        if item == 'children':
            if (self.left and self.right) or (not self.left and not self.right):
                return [self.left, self.right]
            elif not self.left:
                return [TreeNode('X'), self.right]
            else:
                return [self.left, TreeNode('X')]

    def __str__(self):
        return str(self.val)


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        """
        桶排序，N个数字使用N个桶分别保存某个区间的最小值和最大值，
        每个区间的最小值和前一个区间的最大值的差就是一个候选结果。

        因为使用N个桶，所有桶之间的差值至少是(max-min)//N，而桶
        内部的数字的差值一定小于这个值，所以值考虑桶之间的差值即可。


        :param nums:
        :return:
        """
        
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        a, b = min(nums), max(nums)
        size = int(math.ceil((b-a)/(len(set(nums))-1)))
        print(a, b, size, (b-a)//size+1)
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in nums:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        print(bucket)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))

    def buildCartesianTree(self, nums):
        """
        建立笛卡尔树
        使用笛卡尔树是错误的做法，因为只能保证根比左右子树都大，但是不能够保证和左子树最接近的数字都在左子树中
        :param nums:
        :return:
        """
        q = []
        for nums in nums:
            node = None

            # 找到最前面一个比当前数字大的节点
            while q:
                node = q[-1]
                if node.val > nums:
                    break
                q.pop()

            newNode = TreeNode(nums)

            if node:
                if node.val > nums:
                    # 找到一个比当前数字大的节点，新建节点左为它的右子树，它之前的右子树作为当前节点的左子树
                    right = node.right
                    node.right = newNode
                    newNode.left = right
                else:
                    # 如果所以的节点都比当前数字小，之前构建的整个树作为新建节点的左子树
                    newNode.left = node
            q.append(newNode)
        return q[0]




# print(math.log10(10))
# print(math.log10(13))
# print(math.log10(111))
s = Solution()
print(s.maximumGap([1, 10000000]))
print(s.maximumGap([1,1,1,1,1,5,5,5,5,5]))
print(s.maximumGap([3, 6, 9, 1]))
print(s.maximumGap([5, 2, 4]))
print(s.maximumGap([1, 2, 5, 4, 7, 11, 9]))
print(s.maximumGap([1]))
print(s.maximumGap([]))
print(s.maximumGap([10]))
print(s.maximumGap([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]))