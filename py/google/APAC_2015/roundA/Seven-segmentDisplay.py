# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-06 16:29
"""
__author__ = 'huash'

import sys
import os


sys.stdin = open('input/A-small-practice.in', 'r')
sys.stdout = open('output/A-small-practice.out', 'w')

sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-large-practice.out', 'w')

LED = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
]


T = int(input())
for ti in range(1, T+1):
    line = input().split(' ')
    N = int(line[0])

    count = 0
    BROKENS = [0]*7
    error = False
    last = 0

    for v in range(10):
        brokens = [0]*7
        error = False
        for i in range(1, len(line)):
            num = (v-i+11) % 10
            light = line[i]
            led = LED[num]
            for j in range(7):
                if light[j]:
                    if brokens[j] == 1:
                        error = True
                        break
                    elif led[j] == 0:
                        error = True
                        break
                    else:
                        brokens[j] == -1
                else:
                    if led[j] == 1:
                        if brokens[j] == -1:
                            error = True
                            break
                        else:
                            brokens[j] == 1
                if error:
                    break
            if error:
                break
        if not error and brokens.count(0) == 0:
            count += 1
            BROKENS = brokens
            last = v
        if count > 1:
            error = True
            break

    if error or count <= 0:
        print('Case #{}: ERROR!'.format(ti))
    else:
        v = (last - N + N*10) % 10
        led = LED[v]
        result = ''
        for i in range(7):
            if led[i] == 1 and BROKENS[i] == -1:
                result += '1'
            else:
                result += '0'
        print('Case #{}: {}'.format(ti, result))
