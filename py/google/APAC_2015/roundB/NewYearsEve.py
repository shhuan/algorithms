# -*- coding: utf-8 -*-

"""
created by 'huash' at '2015-04-03 19:24'

新年的时候把酒杯堆成金字塔形状，然后从顶部往下倒酒，计算倒完B瓶酒之后第L层第N个酒杯里面有多少酒。

所有酒都倒入了最上面的一个杯子，杯子装不下的部分被平均装入了它下面的三个杯子中，依次递推即可。 不要尝试模拟。

Java中使用数组比Map快很多，大概是5s VS 3s，但是在Python中明显使用dict更快，不过也需要超过20s

"""
__author__ = 'huash'

import sys
import os
import math
import py.lib.Utils as Utils
# import numpy
# import datetime

sys.stdin = open('input/B-large-practice.in', 'r')
# sys.stdin = open('input/sample.txt', 'r')
sys.stdout = open('output/B-large-practice.out', 'w')

# start_time = datetime.datetime.now()

Q = dict()

reader = Utils.Reader()
reader.read()

MAXN = 405

# Row[i] = r means the ith cup at row r
Row = [0 for col in range(MAXN*MAXN//2)]

# Col[i] = c means the ith cup at col c
Col = [0 for col in range(MAXN*MAXN//2)]

# Num[i][j] = n means the number of jth cup on row i is n
Num = [[0 for col in range(MAXN)] for col in range(MAXN)]

# slow than dict Q, cost 33s, but same approach only cost 4s in Java
# Count = [[[[0.0, 0.0] for x in range(MAXN)] for y in range(MAXN)] for z in range(2)]

num = 1
for row in range(1, MAXN):
    for col in range(1, row+1):
        Row[num] = row
        Col[num] = col
        Num[row][col] = num
        num += 1

T = reader.next_int()
for ti in range(1, T + 1):
    B = reader.next_int()
    L = reader.next_int()
    N = reader.next_int()
    Q.clear()
    Q[(1, 1, 1)] = [0.0, B*750.0]
    # Count[1][1][1] = [0.0, B*750.0]
    for level in range(1, L+1):

        # clean next level before calculate
        # for row in range(1, level+2):
        #     for col in range(1, row+3):
        #         Count[(level+1) % 2][row][col] = [0.0, 0.0]

        # calculate status on next level
        for row in range(1, level+1):
            for col in range(1, row+1):
                # c, r = Count[level % 2][row][col]
                cr = Q.get((level, row, col))
                c, r = 0.0, 0.0
                if cr is not None:
                    c = cr[0]
                    r = cr[1]
                if r > 0.0:
                    if c < 250.0:
                        c += r
                        r = max(0.0, c-250.0)
                        c = min(c, 250.0)
                    # Count[(level+1) % 2][row][col][1] += r/3
                    # Count[(level+1) % 2][row+1][col][1] += r/3
                    # Count[(level+1) % 2][row+1][col+1][1] += r/3
                    if Q.get((level+1, row, col)) is None:
                        Q[(level+1, row, col)] = [0, 0]
                    Q[(level+1, row, col)][1] += r/3
                    if Q.get((level+1, row+1, col)) is None:
                        Q[(level+1, row+1, col)] = [0, 0]
                    Q[(level+1, row+1, col)][1] += r/3
                    if Q.get((level+1, row+1, col+1)) is None:
                        Q[(level+1, row+1, col+1)] = [0, 0]
                    Q[(level+1, row+1, col+1)][1] += r/3
    # for k, v in Q.items():
    #     print('{} = {}'.format(k, v))
    #
    # print('Getting {}'.format((L, Row[N], Col[N])))
    if Q.get((L, Row[N], Col[N])) is not None:
        cr = Q[(L, Row[N], Col[N])]
        print('Case #%d: %.7f' % (ti, min(cr[0]+cr[1], 250.0)))
    else:
        print('Case #%d: %.7f' % (ti, 0.0))

    # cr = Count[L % 2][Row[N]][Col[N]]
    # print('Case #%d: %.7f' % (ti, min(cr[0]+cr[1], 250.0)))

# end_time = datetime.datetime.now()
#
# print('Time cost {}'.format(end_time - start_time))