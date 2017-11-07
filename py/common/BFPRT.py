# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-05 15:27


关于选择第k小的数字有许多方法，其效率和复杂度各不一样，可以根据实际情况进行选择。

1. 将n个数排序(比如快速排序或归并排序)，选取排序后的第k个数，时间复杂度为O(nlogn)。使用STL函数sort可以大大减少编码量。
2。 将方法1中的排序方法改为线性时间排序算法(如基数排序或计数排序)，时间复杂度为O(n)。但线性时间排序算法使用限制较多，不常使用。
3. 维护一个k个元素的最大堆，存储当前遇到的最小的k个数，时间复杂度为O(nlogk)。这种方法同样适用于海量数据的处理。
4. 部分的选择排序，即把最小的放在第1位，第二小的放在第2位，直到第k位为止，时间复杂度为O(kn)。实现非常简单。
5. 部分的快速排序（快速选择算法），每次划分之后判断第k个数在左右哪个部分，然后递归对应的部分，平均时间复杂度为O(n)。但最坏情况下复杂度为O(n^2)。
6. BFPRT算法，修改快速选择算法的主元选取规则，使用中位数的中位数的作为主元，最坏情况下时间复杂度为O(n)。

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import random



def NthElement(nums, l, r, n):
    """
    直接使用快速排序的划分寻找第n小的元素，即排序后的nums[n]
    :param nums:
    :param l:
    :param r:
    :param n:
    :return:
    """
    if l == r:
        print(l, r, n, nums[l])
        return nums[l]
    m = partition(nums, l, r)

    if n == m:
        return nums[m]
    elif n < m:
        return NthElement(nums, l, m - 1, n)
    else:
        return NthElement(nums, m + 1, r, n)


def partition(nums, left, right):
    """
    function partition(a, left, right, pivotIndex)
    pivotValue := a[pivotIndex]
    swap(a[pivotIndex], a[right]) // 把pivot移到結尾
    storeIndex := left
    for i from left to right-1
        if a[i] <＝ pivotValue
            swap(a[storeIndex], a[i])
            storeIndex := storeIndex + 1
    swap(a[right], a[storeIndex]) // 把pivot移到它最後的地方
    return storeIndex

    死记硬背
    :param nums:
    :param l:
    :param r:
    :return:
    """
    pivotIndex = random.randint(left, right)
    pivotValue = nums[pivotIndex]
    nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
    storeIndex = left
    for i in range(left, right):
        if nums[i] <= pivotValue:
            nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
            storeIndex += 1
    nums[right], nums[storeIndex] = nums[storeIndex], nums[right]

    return storeIndex




def BFPRT(nums, l, r, n):
    """
    1. 首先把数组按5个数为一组进行分组，最后不足5个的忽略。对每组数进行排序（如插入排序）求取其中位数。
    2. 把上一步的所有中位数移到数组的前面，对这些中位数递归调用BFPRT算法求得他们的中位数。
    3. 将上一步得到的中位数作为划分的主元进行整个数组的划分。
    4. 判断第k个数在划分结果的左边、右边还是恰好是划分结果本身，前两者递归处理，后者直接返回答案。

    :param nums:
    :param l:
    :param r:
    :param n:
    :return: nums下标l到r的第i个数
    """
    if r - l + 1 <= 5:
        insertionSort(nums, l, r)
        return nums[l + n - 1]

    t = l - 1
    st = l
    while st + 4 <= r:
        insertionSort(nums, st, st + 4)
        t += 1
        # 将中位数替换到数组前面，便于递归求取中位数的中位数
        nums[t], nums[st+2] = nums[st+2], nums[t]
        st += 5

    pivotId = l + (t - l) // 2

    # 通过划分保证中位数在正确的位置
    BFPRT(nums, l, t, pivotId)

    m = partition2(nums, l, r, pivotId)
    cur = m - l
    if n == cur:
        return nums[m]
    elif n < cur:
        return BFPRT(nums, l, m - 1, n)
    else:
        return BFPRT(nums, m + 1, r, n - cur)


def partition2(nums, left, right, pivotId):
    """
    以nums[pivotId]作为主元素划分
    :param nums:
    :param l:
    :param r:
    :param pivotId:
    :return:
    """
    pivotIndex = pivotId
    pivotValue = nums[pivotIndex]
    nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
    storeIndex = left
    for i in range(left, right):
        if nums[i] <= pivotValue:
            nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
            storeIndex += 1
    nums[right], nums[storeIndex] = nums[storeIndex], nums[right]

    return storeIndex


def insertionSort(nums, l, r):
    if l >= r:
        return
    for i in range(l, r):
        v = nums[i+1]
        for j in range(i, l-2, -1):
            if nums[j] <= v or j == l-1:
                nums[j+1] = v
                break
            else:
                nums[j+1] = nums[j]






# nums = [1, 4, 2, 2, 3]
# insertionSort(nums, 1, 3)
# print(nums)
# insertionSort(nums, 0, len(nums)-1)
# print(nums)
#
# nums = [1, 5, 2, 4, 3]
# print(partition2(nums, 0, len(nums)-1, 3))
# print(nums)
#
# nums = [0] * 20
# for i in range(len(nums)):
#     nums[i] = random.randint(1, 10)
# print(nums)
nums = [1, 10, 1, 8, 5, 4, 9, 2, 4, 3, 2, 4, 4, 5, 6, 10, 6, 5, 8, 1]
print(BFPRT(nums, 0, 19, 5))
print(nums)
# print(sorted(nums))
# print([i for i in range(20)])
# for i in range(1):
#     nums = [1, 10, 1, 8, 5, 4, 9, 2, 4, 3, 2, 4, 4, 5, 6, 10, 6, 5, 8, 1]
#     print(sorted(nums))
#     # print(nums)
#     res, exp = NthElement(nums, 0, 19, 5), 3
#     print(res, exp, res == exp)
#     print(sorted(nums))

# nums = [1, 10, 1, 8, 5, 4, 9, 2, 4, 3, 2, 4, 4, 5, 6, 10, 6, 5, 8, 1]
# print(nums)
# print(partition(nums, 0, 19))

# for i in range(10):
#     print(random.randint(1, 3))
# print(partition([1], 0, 0))
# print(partition([1, 2], 0, 1))
# print(partition([1, 1, 1, 2, 3, 2], 0, 5))

# for i in range(10):
#     nums = [0] * random.randint(1, 10)
#     for j in range(len(nums)):
#         nums[j] = random.randint(1, 10)
#     print(nums)
#     print(partition(nums, 0, len(nums)-1))

nums = [1, 10, 1, 8, 5, 4, 9, 2, 4, 3, 2, 4, 4, 5, 6, 10, 6, 5, 8, 1]
partition(nums, 0, 19)