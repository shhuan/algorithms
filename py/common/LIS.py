# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-07 10:19

以下分析内容参考
http://www.cnblogs.com/liyukuneed/archive/2013/05/26/3090402.html

给定一个长度为N的数组，找出一个最长的单调自增子序列（不一定连续，但是顺序不能乱）。
例如：给定一个长度为6的数组A{5， 6， 7， 1， 2， 8}，则其最长的单调递增子序列为{5，6，7，8}，长度为4.



解法一：最长公共子序列法：
仔细思考上面的问题，其实可以把上面的问题转化为求最长公共子序列的问题。原数组为A{5， 6， 7， 1， 2， 8}，
下一步，我们对这个数组进行排序，排序后的数组为A‘{1， 2， 5， 6， 7， 8}。我们有了这样的两个数组后，
如果想求数组A的最长递增子序列，其实就是求数组A与它的排序数组A‘的最长公共子序列。



解法二：动态规划法（O(N^2)）
既然是动态规划法，那么最重要的自然就是寻找子问题，对于这个问题，我们找到他的子问题：
对于长度为N的数组A[N] = {a0, a1, a2, ..., an-1}，假设假设我们想求以aj结尾的最大递增子序列长度，
设为L[j]，那么L[j] = max(L[i]) + 1, where i < j && a[i] < a[j], 也就是i的范围是0到j - 1。
这样，想求aj结尾的最大递增子序列的长度，我们就需要遍历j之前的所有位置i（0到j-1），找出a[i] < a[j]，
计算这些i中，能产生最大L[i]的i，之后就可以求出L[j]。之后我对每一个A[N]中的元素都计算以他们各自结尾的
最大递增子序列的长度，这些长度的最大值，就是我们要求的问题——数组A的最大递增子序列。
时间复杂度：由于每一次都要与之前的所有i做比较，这样时间复杂度为O(N^2)。



解法三：动态规划法（O(NlogN)）
上面的解法时间复杂度仍然为O(N^2)，与解法一没有明显的差别。仔细分析一下原因，之所以慢，
是因为对于每一个新的位置j都需要遍历j之前的所以位置，找出之前位置最长递增子序列长度。
那么我们是不是可以有一中方法能不用遍历之前所有的位置，而可以更快的确定i的位置呢？

d = [2,1,5,3,4,8,9,7]
这就需要申请一个长度为N的空间，B[N]，用变量len记录现在的最长递增子序列的长度。
B数组内任意元素B[i]，记录的是最长递增子序列长度为i的序列的末尾元素的值，也就是这个最长递增子序列的最大元素的大小值。
首先，把d[1]有序地放到B里，令B[1] = 2，就是说当只有1一个数字2的时候，长度为1的LIS的最小末尾是2。这时Len=1
然后，把d[2]有序地放到B里，令B[1] = 1，就是说长度为1的LIS的最小末尾是1，d[1]=2已经没用了，很容易理解吧。这时Len=1
接着，d[3] = 5，d[3]>B[1]，所以令B[1+1]=B[2]=d[3]=5，就是说长度为2的LIS的最小末尾是5，很容易理解吧。这时候B[1..2] = 1, 5，Len＝2
再来，d[4] = 3，它正好加在1,5之间，放在1的位置显然不合适，因为1小于3，长度为1的LIS最小末尾应该是1,
这样很容易推知，长度为2的LIS最小末尾是3，于是可以把5淘汰掉，这时候B[1..2] = 1, 3，Len = 2
继续，d[5] = 6，它在3后面，因为B[2] = 3, 而6在3后面，于是很容易可以推知B[3] = 6, 这时B[1..3] = 1, 3, 6，还是很容易理解吧？ Len = 3 了噢。
第6个, d[6] = 4，你看它在3和6之间，于是我们就可以把6替换掉，得到B[3] = 4。B[1..3] = 1, 3, 4， Len继续等于3
第7个, d[7] = 8，它很大，比4大，嗯。于是B[4] = 8。Len变成4了
第8个, d[8] = 9，得到B[5] = 9，嗯。Len继续增大，到5了。
最后一个, d[9] = 7，它在B[3] = 4和B[4] = 8之间，所以我们知道，最新的B[4] =7，B[1..5] = 1, 3, 4, 7, 9，Len = 5。
于是我们知道了LIS的长度为5。

注意，这个1,3,4,7,9不是LIS，它只是存储的对应长度LIS的最小末尾。有了这个末尾，我们就可以一个一个地插入数据。
虽然最后一个d[9] = 7更新进去对于这组数据没有什么意义，但是如果后面再出现两个数字 8 和 9，那么就可以把8更新到d[5], 9更新到d[6]，得出LIS的长度为6。

然后应该发现一件事情了：在B中插入数据是有序的，而且是进行替换而不需要挪动——也就是说，我们可以使用二分查找，
将每一个数字的插入时间优化到O(logN)~~~~~于是算法的时间复杂度就降低到了O(NlogN)～！



"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils



MAXNN = 301
reader = Utils.Reader()

def LIS_2(A):
    L = [0]*len(A)
    P = [0]*len(A)
    # L[i] = max{L[j]+1}, j<i and A[j]<=A[i]
    L[0] = 1
    # 前一个数字的下标
    P[0] = -1

    maxl = 0
    maxi = 0
    for i in range(1, len(A)):
        l = 0
        for j in range(i):
            if L[j] > l and A[j] <= A[i]:
                l = L[j]
                P[i] = j
        L[i] = l+1
        if l+1 > maxl:
            maxl = l+1
            maxi = i
    print('LIS = %d' % maxl)

    # 构造LIS序列
    s = list()
    while maxi >= 0:
        s.append(A[maxi])
        maxi = P[maxi]
    s.reverse()
    print(', '.join(map(str, s)))

A = [2, 1, 5, 3, 4, 8, 9, 7]
LIS_2(A)