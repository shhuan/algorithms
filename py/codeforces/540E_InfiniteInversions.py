# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-19 11:31


对一个1, 2, 3, ... ,到无限大的连续递增序列做N次交换操作，
每次交换a,b把位置a和位置b的两个数字交换。

计算交换后的逆序对的数量。


分析：
逆序对由两个部分组成：
1. 参与交换的数字组成的逆序对
2. 参与交换的每个数字和其他数字组成的逆序对

计算逆序对的方法有mergesort 和 Fenwick tree，可以计算出1.
对于2，每个数字的值和它的位置之间这个区间的所有没有参与交换的数字都能组成一个逆序对。
所以abs(index-val)-1-swapped，计算swapped使用二叉查找就可以。





归并排序求逆序对
设数组为A，在排序合并的时候有左右两个数组L，R。
逆序对个数f(A) = f(L) + f(R) + s(L, R)。
s(L, R)是大数在L中，小数在R中的逆序对的数量。
因为L和R已经排好序，可以在合并的时候直接算出s(L, R)

li = 0
ri = 0
ai = 0
count = 0
while li < len(L) and ri < len(R):
    if L[li] <= R[ri]:
        A[ai] = L[li]
        li += 1
    else:
        A[ai] = R[ri]
        ri += 1
        # L[li:]所以的数字都大于R[ri]，构成len(L)-li+1个逆序对
        count += len(L)-li+1
    ai += 1


"""
import random
import datetime
import sys
import bisect

__author__ = 'huash06'

# N = int(input())

class Solution:
    def __init__(self):
        self.vals = {}
        self.tmparr = []

    def solve(self):
        startTime = datetime.datetime.now()
        sortedVals = sorted(self.vals.items(), key=lambda x: x[0])
        sortedIndice = [x[0] for x in sortedVals]
        # print(sortedVals)

        ivs = [x[1] for x in sortedVals]
        # print(ivs)
        # ivs = list(self.vals.values())
        sys.stderr.write('Sort Time: {}\n'.format(datetime.datetime.now()-startTime))
        startTime = datetime.datetime.now()
        res = self.inversionCount(ivs, 0, len(ivs))
        # print(res)
        sys.stderr.write('Inversion Time: {}\n'.format(datetime.datetime.now()-startTime))


        for si in sortedIndice:
            index = si
            val = self.vals[si]



            tmp = 0
            if index > val:
                # previous
                # 如果位置index的数字小于index，计算它前面有多少比它大的数字。
                # 除掉其中属於交换位置的数字
                tmp += index - val - 1

                if tmp > 0:
                    # how many sorted vals in (val, index)
                    # for sv in sortedVals:
                    #     i = sv[0]
                    #     v = sv[1]
                    #     if i > index:
                    #         break
                    #     if val < i < index:
                    #         tmp -= 1
                    tmp -= self.countSwaps(sortedIndice, val, index)

            elif index < val:
                # after
                # 如果位置index的数字于index，计算它后面有多少比它小的数字。
                # 除掉其中属於交换位置的数字
                tmp += val - index - 1
                if tmp > 0:
                    # how many sorted vals in (index, val)
                    # for sv in sortedVals:
                    #     i = sv[0]
                    #     v = sv[1]
                    #     if i > val:
                    #         break
                    #     if index < i < val:
                    #         tmp -= 1
                    tmp -= self.countSwaps(sortedIndice, index, val)

            res += tmp



        # print(sortedVals)
        print(res)

    def readMockInput(self):
        N = 100000
        for i in range(N):
            # a, b = [int(x) for x in input().split()]
            a, b = random.randint(1, 50), random.randint(1000, 1000000000)
            self.vals[a], self.vals[b] = self.getVal(b), self.getVal(a)

    def readInput(self):
        N = int(input())
        for i in range(N):
            a, b = [int(x) for x in input().split()]
            self.vals[a], self.vals[b] = self.getVal(b), self.getVal(a)

    def getVal(self, pos):
        if pos in self.vals:
            return self.vals[pos]
        return pos


    def inversionCount(self, vals, l, r):
        if r - l <= 1:
            return 0

        hlf = (l + r) // 2
        leftCount = self.inversionCount(vals, l, hlf)
        rightCount = self.inversionCount(vals, hlf, r)

        count = leftCount + rightCount
        li = l
        ri = hlf
        ai = 0
        A = [0] * (r-l)
        while li < hlf and ri < r:
            if vals[li] <= vals[ri]:
                A[ai] = vals[li]
                li += 1
            else:
                A[ai] = vals[ri]
                ri += 1
                # L[li:]所以的数字都大于R[ri]，构成len(L)-li+1个逆序对
                count += hlf-li
            ai += 1
        while li < hlf:
            A[ai] = vals[li]
            ai += 1
            li += 1
        while ri < r:
            A[ai] = vals[ri]
            ai += 1
            ri += 1
        for i in range(r-l):
            vals[l+i] = A[i]

        return count

    def lowerBounds(self, vals, val):

        l = 0
        r = len(vals)

        while l < r:
            mid = (l + r) // 2
            if vals[mid] >= val:
                r = mid
            elif vals[mid] < val:
                l = mid + 1
        return r

    def upperBounds(self, vals, val):
        l = 0
        r = len(vals)
        while l < r:
            mid = (l + r) // 2
            if vals[mid] > val:
                r = mid
            elif vals[mid] <= val:
                l = mid + 1

        return l

    def countSwaps(self, vals, l, r):
        # return self.lowerBounds(vals, r) - self.upperBounds(vals, l)
        return bisect.bisect_left(vals, r, 0, len(vals)) - bisect.bisect_right(vals, l, 0, len(vals))





solution = Solution()
# solution.readInput()
solution.readMockInput()
startTime = datetime.datetime.now()
solution.solve()
sys.stderr.write('Time Cost:{}\n'.format(datetime.datetime.now()-startTime))