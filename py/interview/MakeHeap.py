# -*- coding: utf-8 -*-

"""
Microsoft

给出Make_Heap过程的实现，并分析复杂度，用数组表示栈


"""
__author__ = 'huangshuangquan'



def make_heap(anArray):
    if not anArray or len(anArray) <= 1:
        return

    # 复杂度分析： 这里使用自底向上构建
    # 直接计算最里面的循环执行的次数为 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3
    # s = sigma(i*pow(2,i))
    # O(N)
    for i in range(1, len(anArray)):
        currentIndex = i
        parentIndex = (currentIndex - 1) // 2
        while anArray[parentIndex] > anArray[currentIndex]:
            anArray[parentIndex], anArray[currentIndex] = anArray[currentIndex], anArray[parentIndex]
            currentIndex = parentIndex
            parentIndex = (parentIndex - 1) // 2
            if parentIndex <= 0:
                break

if __name__ == "__main__":
    inputArray = [4, 2, 1, 4, 5, 2, 9, 2]
    make_heap(inputArray)
    print(inputArray)

    inputArray = [3, 9, 2, 8]
    make_heap(inputArray)
    print(inputArray)