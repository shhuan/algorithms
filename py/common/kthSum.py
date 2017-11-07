# -*- coding: utf-8 -*-
"""


"""
__author__ = 'huash'


import random
import datetime


MAX_SIZE = 50


def get2Arrays():
    result = []

    len1 = random.randint(1, MAX_SIZE)
    len2 = random.randint(1, MAX_SIZE)

    a1 = []
    for i in range(len1):
        a1.append(random.randint(1, 100))

    a2 = []
    for i in range(len2):
        a2.append(random.randint(1, 100))

    result.append(list(sorted(a1)))
    result.append(list(sorted(a2)))

    return result


def getKthSum1(a1, a2, k):
    if k <= 0 or not a1 or not a2 or k > len(a1)*len(a2):
        return -1

    sums = []
    for v1 in a1:
        for v2 in a2:
            sums.append(v1 + v2)

    return sorted(sums)[k-1]


def getKthSum2(a, b, k):
    if k <= 0 or not a or not a or k > len(a) * len(b):
        return -1

    if k == 1:
        return a[0] + b[0]

    ki = 1
    ai = 0
    bi = 0
    current_sum = a[0] + b[0]
    while ki < k:
        if ai >= len(a) and bi >= len(b):
            print("###############ERROR#####################")
            # should never go here
            break
        next_ai = -1
        next_bi = -1
        next_sum = -1

        if ai < len(a) - 1 and bi < len(b) - 1:
            for i in range(ai + 1):
                temp_sum = a[i] + b[bi + 1]
                if temp_sum > current_sum:
                    next_ai = i
                    next_bi = bi + 1
                    next_sum = temp_sum
                    break
            for i in range(bi + 1):
                temp_sum = a[ai + 1] + b[i]
                if temp_sum > current_sum:
                    if temp_sum < next_sum:
                        next_bi = i
                        next_ai = ai + 1
                        next_sum = temp_sum
                    break

        elif ai < len(a) - 1:
            next_ai = ai
            bmax = bi + 1
            while bmax > 0 and next_ai < len(a) - 1:
                next_ai += 1
                next_bmax = -1
                for i in range(bmax):
                    temp_sum = a[next_ai] + b[i]
                    if temp_sum > current_sum:
                        next_bmax = i
                        next_sum = temp_sum
                        next_bi = i
                        break
                bmax = next_bmax
        elif bi < len(b) - 1:
            next_bi = bi + 1
            amax = ai + 1
            while amax > 0 and next_bi < len(b) - 1:
                next_bi += 1
                next_amax = -1
                for i in range(amax):
                    temp_sum = a[i] + b[next_bi]
                    if temp_sum > current_sum:
                        next_amax = i
                        next_sum = temp_sum
                        next_ai = i
                        break
                amax = next_amax
        ai = next_ai
        bi = next_bi
        current_sum = next_sum
        ki += 1

    return current_sum



if __name__ == '__main__':
    arrs = get2Arrays()

    # arrs = [
    #     [7, 14, 26, 32],
    #     [8, 38, 52, 55]
    # ]
    print(arrs[0])
    print(arrs[1])

    size = len(arrs[0]) * len(arrs[1])
    result = []
    start1 = datetime.datetime.now()
    for i in range(1, size+1):
        result.append(getKthSum1(arrs[0], arrs[1], i))
    t1 = datetime.datetime.now() - start1
    print(result)


    result2 = []
    start2 = datetime.datetime.now()
    for i in range(1, size+1):
        result2.append(getKthSum2(arrs[0], arrs[1], i))
    t2 = datetime.datetime.now() - start2
    print(result2)

    print('{}, {}'.format(t1, t2))







