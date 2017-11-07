#!/usr/bin/python
# -*- coding: UTF-8 -*-

# __author__ = 'huash'

import sys

__DEBUG = False

if __DEBUG:
    import matplotlib.pyplot as plt
    # import numpy as nm
    import math


ONLINE_JUDGE = True


if not ONLINE_JUDGE:
    sys.stdin = open('Input/input_1144.txt', 'r')

STATE = [[[1 for x in range(102)] for y in range(102)] for z in range(102)]
W, H, T = map(int, sys.stdin.readline().split())

case_index = 1
while W != 0:
    if case_index > 1:
        print('')
    print('Robbery #%d:' % case_index)
    case_index += 1

    # T -= 1
    N = int(sys.stdin.readline())
    # 初始化
    for t in range(1, T+1):
        for x in range(1, W+1):
            for y in range(1, H+1):
                STATE[t][x][y] = 1

    # 获取输入
    # noinspection PyRedeclaration
    for i in range(N):
        ti, l, b, r, t = map(int, sys.stdin.readline().split())
        for x in range(l, r + 1):
            for y in range(b, t + 1):
                STATE[ti][x][y] = 0

    # 正向推导
    for t in range(2, T + 1):
        for x in range(1, W + 1):
            for y in range(1, H + 1):
                STATE[t][x][y] = 0 if STATE[t][x][y] == 0 else int(STATE[(t - 1)][x][y] or
                                                                   STATE[(t - 1)][x][max(y - 1, 1)] or
                                                                   STATE[(t - 1)][x][min(y + 1, H)] or
                                                                   STATE[(t - 1)][max(x - 1, 1)][y] or
                                                                   STATE[(t - 1)][min(x + 1, W)][y])

    if __DEBUG:
        plt.figure(u'正推')
        row = math.sqrt(T) + 1
        for t in range(1, T + 1):
            plt.subplot(row, row, t)
            plt.title('T=%d' % t)
            plt.xlim(0, W + 1)
            plt.ylim(0, H + 2)
            for x in range(1, W + 1):
                for y in range(1, H + 1):
                    if STATE[t][x][y] == 1:
                        plt.plot(x, y, 'go')
                    else:
                        plt.plot(x, y, 'rx')

    # 如果到最后的时间都还有位置藏身
    final_loc = 0
    for x in range(1, W + 1):
        for y in range(1, H + 1):
            if STATE[T][x][y] == 1:
                final_loc += 1

    # 从最后的位置往前倒推
    if final_loc > 0:
        for t in range(T, 1, -1):
            for x in range(1, W + 1):
                for y in range(1, H + 1):
                    STATE[(t - 1)][x][y] = 0 if STATE[(t - 1)][x][y] == 0 else int(STATE[t][x][y] or
                                                                                   STATE[t][x][max(y - 1, 1)] or
                                                                                   STATE[t][x][min(y + 1, H)] or
                                                                                   STATE[t][max(x - 1, 1)][y] or
                                                                                   STATE[t][min(x + 1, W)][y])
        # 找出每个时间的位置
        loc_count_at_time = [0 for i in range(1, T+2)]
        loc_at_time = [(0, 0) for row in range(1, T+2)]
        for t in range(1, T + 1):
            loc_count = 0
            for x in range(1, W + 1):
                for y in range(1, H + 1):
                    if STATE[t][x][y] == 1:
                        loc_count += 1
                        loc_at_time[t] = (x, y)
                        # print('%d -> %d,%d' % (t, x, y))
            loc_count_at_time[t] = loc_count
        # print(loc_count_at_time)
        # print(loc_at_time)

        reduced_count = 0
        for t in range(1, T+1):
            if loc_count_at_time[t] == 1:
                print('Time step {}: The robber has been at {},{}.'.format(t, loc_at_time[t][0], loc_at_time[t][1]))
                reduced_count += 1
        if reduced_count == 0:
            print('Nothing known.')

        if __DEBUG:
            plt.figure(u'倒推')
            row = math.sqrt(T) + 1
            for t in range(1, T + 1):
                plt.subplot(row, row, t)
                plt.title('T=%d' % t)
                plt.xlim(0, W + 1)
                plt.ylim(0, H + 2)
                for x in range(1, W + 1):
                    for y in range(1, H + 1):
                        if STATE[t][x][y] == 1:
                            plt.plot(x, y, 'go')
                        else:
                            plt.plot(x, y, 'rx')
    else:
        print('The robber has escaped.')

    if __DEBUG:
        plt.show()

    W, H, T = map(int, sys.stdin.readline().split())





