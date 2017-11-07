# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-06 19:29

从宽度为M*M的木料上切需要的正方形木料，问总共需要多少块木料。


"""
__author__ = 'huash'

import sys
import os
import py.lib.Utils as Utils

# sys.stdin = open('input/sample.txt', 'r')
sys.stdin = open('input/D-large-practice.in', 'r')

sys.stdout = open('output/D-large-practice.out', 'w')


reader = Utils.Reader()
reader.read()
T = reader.next_int()

for ti in range(1, T+1):
    N = reader.next_int()
    M = reader.next_int()
    tiles = []
    for i in range(N):
        tiles.append(1 << reader.next_int())

    tiles.sort()
    tiles.reverse()

    result = 1
    Q = [[M, M]]

    for i in range(N):
        cutted = False
        for tile in Q:
            if tile[0] >= tiles[i] and tile[1] >= tiles[i]:
                cutted = True
                w, h = tile
                tile[0] -= tiles[i]
                Q.insert(0, [tiles[i], h-tiles[i]])
                break
        if not cutted:
            result += 1
            Q.insert(0, [M-tiles[i], M])
            Q.insert(0, [tiles[i], M-tiles[i]])

    print('Case #{}: {}'.format(ti, result))