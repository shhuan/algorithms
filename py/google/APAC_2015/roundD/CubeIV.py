# -*- coding: utf-8 -*-

"""
created by 'huash' at '2015'-'03'-'26' '19':'16'

题意：数字1-S^2被随即放置在正方形方格S*S中，要求找出一条最长的连续递增路径，路径上的每一个数字比前一个数字大1，并且位置在前一个数字
的左、右、上、下4个位置之一。

分析：
便利所以数字，如果当前数字四周没有比他更大的数字，就从这个数字作为起点找比他小1的周围一个点，对找到的点重复这个操作直到没有更小的数字，
就得到一条路径。
从所以路径中找出最长的路径即可。
"""
__author__ = 'huash'

import sys
import os

import py.lib.Utils as Utils


# sys.stdin = open('input/A-small-practice.in', 'r')
# sys.stdout = open('output/A-small-practice.out', 'w')

sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-large-practice.out', 'w')

# sys.stdin = open('input/sample.txt', 'r')

reader = Utils.Reader()
reader.read()

T = reader.next_int()
deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for ti in range(1, T + 1):
    S = reader.next_int()
    M = [[0 for row in range(S + 1)] for col in range(S + 1)]
    for i in range(S):
        for j in range(S):
            M[i][j] = reader.next_int()

    number = 0
    count = 0
    for i in range(S):
        for j in range(S):
            is_max_el = True
            for delta in deltas:
                x = i + delta[0]
                x = max(x, 0)
                x = min(x, S - 1)
                y = j + delta[1]
                y = max(y, 0)
                y = min(y, S - 1)
                if M[i][j] == M[x][y] - 1:
                    is_max_el = False
                    break
            if is_max_el:
                c = 1
                ended = False
                px = i
                py = j
                while not ended:
                    ended = True
                    for delta in deltas:
                        x = px + delta[0]
                        x = max(x, 0)
                        x = min(x, S - 1)
                        y = py + delta[1]
                        y = max(y, 0)
                        y = min(y, S - 1)
                        if M[x][y] == M[px][py] - 1:
                            c += 1
                            px = x
                            py = y
                            ended = False
                            break
                if c > count:
                    count = c
                    number = M[px][py]
                elif c == count and number > M[px][py]:
                    number = M[px][py]
    print('Case #{}: {} {}'.format(ti, number, count))




