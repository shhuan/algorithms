# -*- coding: utf-8 -*-

"""
Microsoft

给一个栈的入栈序列，判断另外一个序列是否是它的出栈序列


Sample Input
1 2 3; 2 1 3

Sample Output
True

分析：
直接模拟

"""
__author__ = 'huangshuangquan'

def isPopSeq(pushArray, popArray):
    if not pushArray or not popArray:
        return False
    # 注意这个判断条件不要写掉
    if len(pushArray) != len(popArray):
        return False

    stack = []
    pushIndex = 0
    popIndex = 0
    while pushIndex < len(pushArray):
        stack.append(pushArray[pushIndex])
        pushIndex += 1
        while stack and stack[-1] == popArray[popIndex]:
            stack.pop()
            popIndex += 1

    return not stack

if __name__ == "__main__":
    pushArray = [1, 2, 3]
    popArray = [1, 3, 2]
    print(isPopSeq(pushArray, popArray))

    popArray = [3, 1, 2]
    print(isPopSeq(pushArray, popArray))

    popArray = [1, 2, 3]
    print(isPopSeq(pushArray, popArray))

    popArray = [2, 1, 3]
    print(isPopSeq(pushArray, popArray))

    popArray = [3, 1, 3]
    print(isPopSeq(pushArray, popArray))