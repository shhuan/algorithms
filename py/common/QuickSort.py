# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-04 16:04
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import random


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])

def quickSort(nums, left, right):
    """

    Improvements:
        1. Cutoff to insertion sort. As with mergesort, it pays to switch to insertion sort for tiny arrays.
        The optimum value of the cutoff is system-dependent, but any value between 5 and 15 is likely to work
        well in most situations.
        2. Median-of-three partitioning. A second easy way to improve the performance of quicksort is to use
        the median of a small sample of items taken from the array as the partitioning item. Doing so will
        give a slightly better partition, but at the cost of computing the median. It turns out that most of
        the available improvement comes from choosing a sample of size 3 (and then partitioning on the middle item).

    :param nums:
    :param left:
    :param right:
    :return:
    """
    if left >= right:
        return

    index = partition(nums, left, right)
    quickSort(nums, left, index-1)
    quickSort(nums, index, right)

    return []

def partition(nums, left, right):
    i, j = left, right
    pivotId = random.randint(left, right)
    nums[pivotId], nums[0] = nums[0], nums[pivotId]
    pivot = nums[left]

    while i <= j:
        while i <= j and nums[i] < pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            # 注意交换后改变i和j，否则可能死循环
            i += 1
            j -= 1
    return i


def quickSort_3Way(nums, left, right):
    """
    Entropy-optimal sorting. Arrays with large numbers of duplicate sort keys arise frequently in applications.
    In such applications, there is potential to reduce the time of the sort from linearithmic to linear.

    One straightforward idea is to partition the array into three parts, one each for items with keys smaller than,
    equal to, and larger than the partitioning item's key. Accomplishing this partitioning was a classical
    programming exercise popularized by E. W. Dijkstra as the Dutch National Flag problem, because it is like
    sorting an array with three possible key values, which might correspond to the three colors on the flag.

    Dijkstra's solution is based on a single left-to-right pass through the array that maintains a pointer
    lt such that a[lo..lt-1] is less than v, a pointer gt such that a[gt+1..hi] is greater than v,
    and a pointer i such that a[lt..i-1] are equal to v, and a[i..gt] are not yet examined.


    Starting with i equal to lo we process a[i] using the 3-way compare given us by the Comparable interface to
    handle the three possible cases:
        a[i] less than v: exchange a[lt] with a[i] and increment both lt and i
        a[i] greater than v: exchange a[i] with a[gt] and decrement gt
        a[i] equal to v: increment i
    :param nums:
    :param left:
    :param right:
    :return:
    """

    if left >= right:
        return

    lt = left
    gt = right
    v = nums[lt]
    i = lt
    while i <= gt:
        if nums[i] < v:
            nums[lt], nums[i] = nums[i], nums[lt]
            i += 1
            lt += 1
        elif nums[i] > v:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
        else:
            i += 1
    quickSort_3Way(nums, left, lt-1)
    quickSort_3Way(nums, gt+1, right)


nums = [1, 12, 5, 26, 7, 14, 3, 7, 2]
quickSort(nums, 0, len(nums)-1)
print(nums)

nums = [1, 12, 5, 26, 7, 14, 3, 7, 2]
quickSort_3Way(nums, 0, len(nums)-1)
print(nums)
