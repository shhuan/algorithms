# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-18 10:34


开关一个房间的灯会同时开关它周围4个房间的灯。
找出一个能够关掉所有房间的灯的操作序列。


"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import random
import copy
sys.stdin = open('input/lightsoff.txt', 'r')
# sys.stdout = open('input/lightsoff.txt', 'w')
def genCase(n):
    print(n)
    for r in range(n):
        row = ''
        for c in range(n):
            row += '1' if random.randint(1, 10) > 5 else '0'
        print(row)



def allLightsOff(lights):
    for row in lights:
        if row.count(True) > 0:
            return False
    return True

DELTA = ((1, 0), (-1, 0), (0, 1), (0, -1))


def switch(lights, n, r, c):
    lights[r][c] = not lights[r][c]
    for d in DELTA:
        i = r + d[0]
        j = c + d[1]
        if 0 <= i < n and 0 <= j < n:
            lights[i][j] = not lights[i][j]

def canSwitch(lights, n, r, c):
    return lights[r][c]
    # for d in DELTA:
    #     i = r + d[0]
    #     j = c + d[1]
    #     if 0 <= i < n and 0 <= j < n:
    #         if lights[i][j]:
    #             return True
    # return False

def stateOfLights(lights):
    s = ''
    for row in lights:
        for col in row:
            s += '1' if col else '0'
    return s
def outputLights(lights):
    for r in lights:
        row = ''
        for c in r:
            row += '1' if c else '0'
        print(row)
    print()

def turnoff(lights, n):
    # if steps > 5000:
    #     return []

    # for row in lights:
    #     print(row)
    # print()

    visited = set()
    steps = [(lights, [])]

    while steps:
        l, s = steps.pop(0)
        print(s)
        outputLights(l)
        if allLightsOff(l):
            return s
        for r in range(N):
            for c in range(N):
                if canSwitch(l, n, r, c):
                    lc = copy.deepcopy(l)
                    switch(lc, n, r, c)
                    # s = stateOfLights(lights)
                    # if s not in visited:
                    #     visited.add(s)
                    #     steps.append()
                    st = stateOfLights(lc)
                    if st not in visited:
                        # print(st)
                        visited.add(st)
                        steps.append((lc, s+[(r, c)]))

    return []

#
# print('1')
# genCase(5)

T = int(input())
for ti in range(T):
    N = int(input())
    lights = []
    for i in range(N):
        lights.append([True if v == '1' else False for v in input()])
    ops = turnoff(lights, N)
    print(len(ops))
    for op in ops:
        print(op[0], op[1])
