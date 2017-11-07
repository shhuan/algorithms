# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-12 22:43

There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


"""
__author__ = 'huash'

import sys
import os
# import bisect

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if not A:
            if len(B) % 2 == 0:
                return B[len(B) // 2 - 1]
            else:
                return B[len(B) // 2]
        if not B:
            if len(A) % 2 == 0:
                return A[len(A) // 2 - 1]
            else:
                return A[len(A) // 2]
        if len(A) < 3 and len(B) < 3:
            k = len(A) + len(B)
            k = k//2 if (k % 2 != 0) else k//2-1
            return sorted(A + B)[k]
        m = len(A)
        n = len(B)
        i = (m+n) // 2
        if (m+n) % 2 == 0:
            i -= 1
        if A[-1] < B[0]:
            if i < m:
                return A[i]
            else:
                return B[i-m]
        elif B[-1] < A[0]:
            if i < n:
                return B[i]
            return A[i-n]
        a = A
        b = B
        if A[0] <= B[-1]:
            a = B
            b = A
        m = len(a)
        n = len(b)

        al = self.bisect(a, b[0])
        ar = len(a)
        bl = 0
        br = self.bisect(b, a[-1])

        kth = m + n
        kth = kth//2 if (kth % 2 != 0) else (kth//2 - 1)
        kth -= al
        kth += 1

        return self.find_kth(a[al:ar], b[bl:br], kth)

    def find_kth(self, A, B, K):
        if K < 1:
            return -1
        if not A:
            return B[K-1]
        if not B:
            return A[K-1]
        if K > len(A) + len(B):
            return -1
        elif K == len(A) + len(B):
            return max(A[-1], B[-1])
        elif K == 0:
            return max(A[0], B[0])
        elif len(A) <= 2 and len(B) <= 2:
            return sorted(A + B)[K-1]

        if A[0] > B[-1]:
            if len(B) >= K:
                return B[K-1]
            else:
                return A[K-len(B)-1]
        elif A[-1] < B[0]:
            if len(A) >= K:
                return A[K-1]
            else:
                return B[K-len(A)-1]


        ka = len(A)//2
        kb = self.bisect(B, A[ka])
        k = ka + kb + 1
        if k != K:
            if k > K:
                return self.find_kth(A[:ka], B[:kb], K)
            else:
                return self.find_kth(A[ka:], B[kb:], K-k+1)
        return A[ka]

    def bisect(self, A, v):
        if not A:
            return -1
        if v < A[0]:
            return 0
        elif v > A[-1]:
            return len(A)

        l = 0
        r = len(A)-1

        while l <= r:
            k = (l+r) // 2
            if A[k-1] <= v < A[k]:
                return k
            elif A[k] > v:
                r = k-1
            else:
                l = k+1
        return -1


# k = bisect.bisect(A, v); A[:k-1]<v, A[k:]>v
# print(bisect.bisect([11, 21, 33, 55, 77], 44))

s = Solution()
# print(s.bisect([11, 21, 33, 55, 77], 44))
# print(s.find_kth([2, 4, 6, 8], [1, 3, 5, 7], 5))
# print(s.find_kth([1, 3, 5, 7], [2, 4, 6, 8], 5))

print(s.findMedianSortedArrays([1, 3, 4], [2, 5]))
print(s.findMedianSortedArrays([1, 2, 3, 5], [4]))
print(s.findMedianSortedArrays([2], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 5, 6, 7, 8, 9, 11, 23]))
print(s.findMedianSortedArrays([11, 12], [1, 2, 3, 4, 5]))
print(s.findMedianSortedArrays([1, 2, 3, 4, 5], [11, 12]))
print(s.findMedianSortedArrays([1, 2, 3, 4, 5], []))
print(s.findMedianSortedArrays([1, 2, 3, 4], []))

print(s.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8]))

print(s.findMedianSortedArrays([1, 3, 5, 7, 9, 11], [2, 4, 6, 8]))
print(s.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8, 9, 11]))
