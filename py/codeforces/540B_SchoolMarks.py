# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-18 20:03


"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime


n, k, p, x, y = list(map(int, input().split()))

exits = list(map(int, input().split()))

half = n//2

if x < y:
    print(-1)
elif n <= 1:
    if p >= x:
        print(x)
    else:
        print(-1)
elif not exits:
    if p < y or half + y * (half + 1) > x:
        print(-1)
    else:
        l = (x - y*(half + 1)) // half
        if l < 1:
            print(-1)
        else:
            res = [y] * (n//2 + 1) + [l] * half
            print(' '.join(list(map(str, res))))

else:
    exsum = sum(exits)

    if len(exits) >= n:
        print(-1)
    elif exsum + (n - len(exits)) > x:
        print(-1)
    else:
        median = y
        left = list(filter(lambda x: x < median, exits))
        right = list(filter(lambda x: x >= median, exits))
        if len(left) > n // 2:
            median = sorted(left)[n//2]
        elif len(right) > n // 2:
            median = sorted(right)[len(right) - n//2 - 1]

        left = list(filter(lambda x: x < median, exits))
        right = list(filter(lambda x: x >= median, exits))


        res = []
        if len(right) > n//2:
            left.extend(right[:len(right)-n//2])
            right = right[len(right)-n//2:]
        elif len(left) > n//2:
            right.extend(left[n//2:])
            left = left[:n//2]

        noMedian = False
        if left and left[-1] >= median:
            left = left[:-1]
        elif right and len(right) > 0:
            right = right[1:]
        else:
            # res.append(median)
            noMedian = True

        lenRigh = n//2 - len(right)
        lenLeft = n//2 - len(left)
        if noMedian:
            lenRigh += 1



        if median < y or exsum + lenLeft + median*lenRigh > x:
            print(-1)
        else:
            maxsum = x - exsum
            minsum = max(lenLeft + lenRigh*y - exsum, 1)

            if lenRigh == 0:
                v = max(minsum//lenLeft, 1)
                for i in range(lenLeft):
                    if minsum > lenLeft and i < minsum % lenLeft:
                        res.append(v+1)
                    else:
                        res.append(v)
                print(' '.join(list(map(str, res))))
            elif lenLeft == 0:
                v = max(minsum//lenRigh, median)
                for i in range(lenRigh):
                    res.append(v)
                print(' '.join(list(map(str, res))))
            else:

                rightSum = min(lenRigh*p, maxsum-lenLeft)
                lefSum = max(minsum-rightSum, lenLeft)

                v = lefSum // lenLeft
                for i in range(lenLeft):
                    if lefSum > lenLeft and i < lefSum % lenLeft:
                        res.append(v+1)
                    else:
                        res.append(v)
                v = rightSum // lenRigh
                for i in range(lenRigh):
                    if rightSum > lenRigh and i < rightSum % lenRigh:
                        res.append(v+1)
                    else:
                        res.append(v)
                # print(len(res), sum(res))
                # print(res.count(1), res.count(2), res.count(3))
                print(' '.join(list(map(str, res))))

