# -*- coding: utf-8 -*-

"""

两个排序的数组A，B，
任取A中的元素a和B中的元素b相加后保持到数组C中。
求C中第k大的元素

例子
A = [1, 3, 7, 9]
B = [1, 2, 5, 8]
K = 3

ouput:
4

如果不计重复和又如何
上述例子C=[2, 3, 4, 5, 6, 8, 8, 9, 9, 10, 11, 11, 12, 14, 15, 17]。
不计重复和之后
C=[2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 17]

"""
__author__ = 'huangshuangquan'

import datetime
import random

def getKthSum_brutal(A, B, k):
    C = []
    for a in A:
        for b in B:
            C.append(a + b)
    return sorted(C)[k-1]

def getKthSum(A, B, k):
    lenA = len(A)
    c = [0] * lenA

    result = 0
    left = 0
    for i in range(k):
        minSum = 10000000
        minIndex = -1
        for j in range(left, lenA):
            if c[j] >= len(B):
                left = j
                continue
            s = A[j] + B[c[j]]
            if s < minSum:
                minSum = s
                minIndex = j
            if j+1 < lenA and c[j] < c[j+1]:
                break
        result = minSum
        c[minIndex] += 1
    return result


lenA = random.randint(1, 50)
lenB = random.randint(1, 50)
A = []
B = []
for i in range(lenA):
    A.append(random.randint(1, 1000))
for i in range(lenB):
    B.append(random.randint(1, 1000))
A.sort()
B.sort()

brutal_result = []
result = []
st1 = datetime.datetime.now()
for k in range(1, lenA*lenB+1):
    brutal_result.append(getKthSum_brutal(A, B, k))
et1 = datetime.datetime.now()

st2 = datetime.datetime.now()
for k in range(1, lenA*lenB+1):
    result.append(getKthSum(A, B, k))
et2 = datetime.datetime.now()

print('{} {}'.format(et1-st1, et2-st2))