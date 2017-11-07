# -*- coding: utf-8 -*-
"""
BIT INDEX TREE


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.


"""
import  math

class NumArrayST(object):
    """
    稀疏表 Sparse Table
    """
    def __init__(self, nums):
        self.nums = nums

        if not nums:
            return

        N = len(nums)
        K = int(math.log(N, 2))+1
        ST = [[0 for _ in range(K)] for _ in range(N)] # ST[i][j]表示从i开始长度为2**j的和

        for i in range(N):
            ST[i][0] = nums[i]

        for k in range(1, K):
            for i in range(N):
                if i + 2**k > N:
                    break
                # s(i,k) = s(i, i+2**k) = s(i,i+2**(k-1)) + s(i+2**(k-1), i+2**k)
                ST[i][k] = ST[i][k-1] + ST[i+2**(k-1)][k-1]

        self.ST = ST


    def update(self, index, val):
        # 需要更新ST[i][k]，如果i<=index<i+2**k
        # TLE

        d = val - self.nums[index]
        self.nums[index] = val
        N = len(self.ST)

        for i in range(index+1):
            for k in range(int(math.log(index-i+1, 2)), int(math.log(N-i, 2)) + 1):
                if index < i + 2**k <= N:
                    self.ST[i][k] += d


    def sumRange(self, start, end):
        if start > end:
            return 0

        end += 1

        k = int(math.log(end-start, 2))
        s = 0
        i = start
        while k >= 0:
            s += self.ST[i][k]
            i = i + 2**k
            if i >= end:
                break
            k = int(math.log(end-i, 2))

        return s


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.nums = nums

        N = len(nums)

        BIT = [0] * (N+1) # BIT[i] 表示sum(nums[i-lowbit(i):i])，不包含第i项，BIT[i]用于求前i项（不包含nums[i]）的和

        # 重点，BIT长度是N+1，表示不包含nums[i]的和，这样可以把0统一进来
        for i in range(N+1):
            BIT[i] = sum(nums[i - (i & -i): i])

        self.BIT = BIT

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        if not self.nums:
            return

        d = val - self.nums[i]
        self.nums[i] = val

        # 重点
        x = i + 1
        while x < len(self.BIT):
            self.BIT[x] += d
            x += x & -x


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums or i > j:
            return 0

        def presum(x):
            if x <= 0:
                return 0

            s = 0
            # 因为self.BIT[0]表示前0项的和，所以不用加
            while x > 0:
                s += self.BIT[x]
                x -= x & -x
            return s

        return presum(j+1) - presum(i)






        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)

s = NumArrayST([5, 18, 13])
print(s.sumRange(0, 2))
s.update(1, -1)
s.update(2, 3)
s.update(0, 5)
s.update(0, -4)
print(s.sumRange(0, 2))

s = NumArrayST([9, -8])
s.update(0, 3)
print(s.sumRange(1, 1))
print(s.sumRange(0, 1))
s.update(1, -3)
print(s.sumRange(0, 1))

s = NumArrayST([1, 9, 5, 7, 3])
print(s.sumRange(4, 4))
print(s.sumRange(2, 4))
print(s.sumRange(3, 3))

s = NumArrayST([1, 3, 5])
print(s.sumRange(0, 2))
s.update(1, 2)
print(s.sumRange(0, 2))

s = NumArray([-1])
print(s.sumRange(0, 0))
s.update(0, 1)
print(s.sumRange(0, 0))
