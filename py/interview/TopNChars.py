# -*- coding: utf-8 -*-

"""
微软电话面试。
给出一个字符串，找出出现次数最多的N个字符并给出他们的出现次数

Sample Input:
aabbcd, 3

Sample Output:
a, 2
b, 2
c, 1

"""
__author__ = 'huangshuangquan'

import collections
import functools

def cmpCharCount(charCount1, charCount2):
    ch1, count1 = charCount1[0], charCount1[1]
    ch2, count2 = charCount2[0], charCount2[1]
    if count1 > count2:
        return -1
    elif count1 < count2:
        return 1
    else:
        return ord(ch1) - ord(ch2)

def getTopNChars(inputStr, N):
    if not inputStr:
        return []

    charCounts = collections.defaultdict(int)
    for ch in inputStr:
        charCounts[ch] += 1
    sortedCharCounts = sorted(charCounts.items(), key=functools.cmp_to_key(cmpCharCount))

    return sortedCharCounts[:N]

if __name__ == "__main__":
    inputStr = "aabbcd"
    print(getTopNChars(inputStr, 3))
    print(getTopNChars(inputStr, 2))
    print(getTopNChars(inputStr, 10))

    inputStr = "csdaqwduihuwqdhuwqhduwqdhwqdwqdwqwq"
    print(getTopNChars(inputStr, 3))
    print(getTopNChars(inputStr, 2))
    print(getTopNChars(inputStr, 10))

    inputStr = "bbaadc"
    print(getTopNChars(inputStr, 3))
    print(getTopNChars(inputStr, 2))
    print(getTopNChars(inputStr, 10))
