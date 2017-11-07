# -*- coding: utf-8 -*-

"""
Microsoft Phone Screen

给一个数组，找出其中一个区间，其和是所以区间中最接近0的

Sample Input
1 2 3 2 -5 2

Sample Output
[2, 4]


分析：
设si表示前i项的和，那么如果si==sj就表示区间[i+1, j]之间的数字相加等于0

"""

__author__ = 'huangshuangquan'

def zeroRange(anArray):
    if not anArray:
        return -1, -1
    if len(anArray) == 1:
        return 0, 0

    sumOfPreviousIElements = 0
    sumAndIndex = []
    for i in range(len(anArray)):
        sumOfPreviousIElements += anArray[i]
        sumAndIndex.append((sumOfPreviousIElements, i))

    sumAndIndex.sort()

    minGap = sumAndIndex[0][0]
    minRange = 0, sumAndIndex[0][1]

    if minGap == 0:
        return minRange
    for i in range(1, len(sumAndIndex)):
        gap = abs(sumAndIndex[i][0] - sumAndIndex[i-1][0])
        if gap < minGap:
            minGap = gap
            minRange = sumAndIndex[i][1], sumAndIndex[i-1][1]
            if gap == 0:
                break

    return min(minRange) + 1, max(minRange)

if __name__ == "__main__":
    inputArray = [1, -1, 0]
    print(zeroRange(inputArray))

    inputArray = [1, 2, 3, 2, -5, 2]
    print(zeroRange(inputArray))

    inputArray = [2]
    print(zeroRange(inputArray))

    inputArray = [1, 2, 3]
    print(zeroRange(inputArray))

    inputArray = [1, 0, 3]
    print(zeroRange(inputArray))

    inputArray = [1, 1, 0]
    print(zeroRange(inputArray))

    inputArray = [2, 3, -1, -2, 3]
    print(zeroRange(inputArray))