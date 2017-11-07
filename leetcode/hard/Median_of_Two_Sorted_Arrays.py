# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-03 11:36

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).



"""
__author__ = 'huash'

import sys
import os
import math
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return self.findMedianSortedArrays_Log(nums1, nums2, 0, len(nums1), 0, len(nums2), length//2 + 1)
        else:
            # print('avg')
            return (self.findMedianSortedArrays_Log(nums1, nums2, 0, len(nums1), 0, len(nums2), length//2) + \
            self.findMedianSortedArrays_Log(nums1, nums2, 0, len(nums1), 0, len(nums2), length//2 + 1)) / 2.0

    def findMedianSortedArrays_Log(self, nums1, nums2, astart, aend, bstart, bend, length):
        if aend - astart > bend - bstart:
            return self.findMedianSortedArrays_Log(nums2, nums1, bstart, bend, astart, aend, length)
        if astart - aend == 0:
            return nums2[bstart+length-1]
        if length == 1:
            return nums1[astart] if nums1[astart] < nums2[bstart] else nums2[bstart]
        pa = aend - astart if aend - astart < length // 2 else length // 2
        pb = length - pa
        if nums1[astart + pa - 1] == nums2[bstart + pb - 1]:
            return nums1[astart + pa - 1]
        elif nums1[astart + pa - 1] < nums2[bstart + pb - 1]:
            return self.findMedianSortedArrays_Log(nums1, nums2, astart+pa, aend, bstart, bend, length-pa)
        else:
            return self.findMedianSortedArrays_Log(nums1, nums2, astart, aend, bstart+pb, bend, length-pb)

    def findMedianSortedArrays2(self, A, B):
        l=len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0


    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            #Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)


    def findMedianSortedArrays3(self, A, B):
        l=len(A)+len(B)
        return self.findKth2(A, B, l//2+1, 0, len(A)) if l % 2 == 1 else \
            (self.findKth2(A, B, l//2, 0, len(A))+self.findKth2(A, B, l//2+1, 0, len(A)))/2.0

    def findKth2(self, A, B, k, s, t):
        """
        在数组A[s:t+1]中找下中位数

        中位数要么出现在数组A中，要么出现在数组B中，我们先从数组A开始找。考察数组A中的一个元素A[p]， 在数组A中，
        有 p 个数比A[p]小，如果数组B中恰好有 c-p 个数比 A[p] 小， 则俩数组合并后就恰好有 c 个数比A[p]小，
        于是A[p]就是要找的中位数。

        如果A[p] 小于 B[c-p-1] ，说明A[p] 太小了，接下来从 A[p+1] ~A[m-1]开始找
        如果A[p] 大于 B[c-p] ，说明A[p] 太大了，接下来从 A[0] ~A[p-1]开始找。
        如果数组A没找到，就从数组B找。
        :param A:
        :param B:
        :param s:
        :param t:
        :return:
        """
        if not A:
            return B[k-1]
        if not B:
            return A[k-1]

        if s >= t:
            return self.findKth2(B, A, k, 0, len(B))

        p = (s + t) // 2

        # 以下三个条件太容易出错了
        if k > p+1 and k-p-2 < 0:
            return self.findKth2(A, B, k, s, t-1)
        if k-p-2 >= len(B):
            return self.findKth2(A, B, k, s+1, t)
        if k <= p:
            return self.findKth2(A, B, k, s, t-1)

        # 数组A中有p个数小于A[p], 当且进当数组B中有c-p个数小于A[p], A[p]才是中位数
        if (k-p-2 < 0 or B[k-p-2] <= A[p]) and (k-p-1 >= len(B) or A[p] <= B[k-p-1]):
            return A[p]

        # A[p]太小了，从数组A中找一个更大的数尝试
        if k-p-2 >= 0 and A[p] < B[k-p-2]:
            return self.findKth2(A, B, k, p+1, t)

        # A[p]太大了，从数组A中找一个更小的数尝试
        return self.findKth2(A, B, k, s, p)



    def findMedianSortedArrays4(self, A, B):
        l=len(A)+len(B)
        return self.findKth3(A, B, l//2+1) if l % 2 == 1 else \
            (self.findKth3(A, B, l//2)+self.findKth3(A, B, l//2+1))/2.0
    def findKth3(self, A, B, k,):
        """
        分别取两个数组中间索引的数，a[x]和b[y]，比较两个数的大小：

        if( a[x] <= a[y] ):
            如果k <= x+y+1，则可以判断出b[y]以及b[y]后面的元素都可以排除在外，减小搜索规模。
            如果k  > x+y+1，则可以判断出a数组的前半部分元素都不符合条件，减少a一半的搜索规模。

        该算法利用了递归的思想，结束条件是：
            a中元素排除出去，则选择b中得第k大元素；
            b中元素全部排除，选择a中第k大元素。

        此方法比较简单容易记忆
        :param A:
        :param B:
        :param k:
        :return:
        """
        if not A:
            return B[k-1]
        if not B:
            return A[k-1]

        x = len(A) // 2
        y = len(B) // 2

        if A[x] < B[y]:
            if k <= x + y + 1:
                return self.findKth3(A, B[:y], k)
            else:
                return self.findKth3(A[x+1:], B, k-x-1)
        else:
            if k <= x + y + 1:
                return self.findKth3(A[:x], B, k)
            else:
                return self.findKth3(A, B[y+1:], k-y-1)

    def findMedianSortedArrays5(self, A, B):
        l=len(A)+len(B)
        return self.findKth4(A, B, l//2+1, 0, len(A), 0, len(B)) if l % 2 == 1 else \
            (self.findKth4(A, B, l//2, 0, len(A), 0, len(B))+self.findKth4(A, B, l//2+1, 0, len(A), 0, len(B)))/2.0

    def findKth4(self, A, B, k, sa, ta, sb, tb):
        """
        findKth3的使用索引的版本，128ms -> 124ms，速度没有提升
        :param A:
        :param B:
        :param k:
        :param sa:
        :param ta:
        :param sb:
        :param tb:
        :return:
        """
        if sa >= ta:
            return B[sb+k-1]
        if sb >= tb:
            return A[sa+k-1]

        x = sa + (ta-sa)//2
        y = sb + (tb-sb)//2

        if A[x] < B[y]:
            if k <= (x-sa) + (y-sb) + 1:
                return self.findKth4(A, B, k, sa, ta, sb, y)
            else:
                return self.findKth4(A, B, k-(x-sa)-1, x+1, ta, sb, tb)
        else:
            if k <= (x-sa) + (y-sb) + 1:
                return self.findKth4(A, B, k, sa, x, sb, tb)
            else:
                return self.findKth4(A, B, k-(y-sb)-1, sa, ta, y+1, tb,)



    def findMedianSortedArrays_Simeple(self, nums1, nums2):
        """
        O(m+n)
        直接使用MergeSort的Merge
        :param nums1:
        :param nums2:
        :return:
        """
        m = len(nums1)
        n = len(nums2)
        k = (m+n) % 2
        mIndex = int(math.ceil(float(m+n) / 2.0))
        if k == 0 or mIndex == 0:
            mIndex += 1
    
        i = 0
        j = 0
    
        saved = 0
        while i < m or j < n:
            if mIndex == 0 and k != 0:
                return saved #only one median
            if mIndex == 0 and k == 0:
                return saved/2.0
            if (mIndex > 1 and k == 0) or k != 0:
                saved = 0
    
            if (i < m and j < n and nums1[i] > nums2[j]) or (i >= m and j < n):
                saved += nums2[j]
                mIndex -= 1
                j += 1
            elif (i < m and j < n) or (i < m and j >= n):
                saved += nums1[i]
                mIndex -= 1
                i += 1

        if mIndex == 0 and k !=0:
            return saved #only one median
        if mIndex == 0 and k == 0:
            return saved/2.0



s = Solution()
print(s.findKth2([], [2, 3], 1, 0, 0))
print(s.findMedianSortedArrays5([1,2,3,4,5,7,8,9,10], [6]))
print(s.findMedianSortedArrays5([1], [1]))
print(s.findMedianSortedArrays5([1, 4], [2, 3]))
print(s.findMedianSortedArrays_Simeple([3, 5, 6, 7], [1, 2]))
print(s.findMedianSortedArrays_Simeple([1, 2], [4, 5, 6]))
print(s.findMedianSortedArrays_Simeple([4, 5, 6], [1, 2]))
print(s.findMedianSortedArrays_Simeple([2], [3, 4]))
print(s.findMedianSortedArrays_Simeple([], [2, 3]))
print(s.findMedianSortedArrays_Simeple([], [1, 2, 3, 4]))
print('==============')

print(s.findMedianSortedArrays3([3, 5, 6, 7], [1, 2]))
print(s.findMedianSortedArrays3([1, 2], [4, 5, 6]))
print(s.findMedianSortedArrays3([4, 5, 6], [1, 2]))
print(s.findMedianSortedArrays3([2], [3, 4]))
print(s.findMedianSortedArrays3([], [2, 3]))
print(s.findMedianSortedArrays3([], [1, 2, 3, 4]))
print('==============')

print(s.findMedianSortedArrays([3, 5, 6, 7], [1, 2]))
print(s.findMedianSortedArrays([1, 2], [4, 5, 6]))
print(s.findMedianSortedArrays([4, 5, 6], [1, 2]))
print(s.findMedianSortedArrays([2], [3, 4]))
print(s.findMedianSortedArrays([], [2, 3]))
print(s.findMedianSortedArrays([], [1, 2, 3, 4]))


