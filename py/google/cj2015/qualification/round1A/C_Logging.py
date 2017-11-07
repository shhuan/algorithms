# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-08 22:09


森林中有N个树，每棵树上有个松鼠。
对于任意一个松鼠，要使它所在的树在森林的边界上，至少需要砍掉多少课树？


"""
__author__ = 'huash'

import sys
import os
import pydot
import matplotlib.pyplot as plt
import math
import datetime

SMALL_DATASET = False
sys.stdin = open('input/sampleC.txt', 'r')
if SMALL_DATASET:
    sys.stdin = open('input/C-small-practice.in', 'r')
    sys.stdout = open('output/C-small-practice.out', 'w')
else:
    sys.stdin = open('input/C-large-practice.in', 'r')
    sys.stdout = open('output/C-large-practice.out', 'w')



def solve1(forest):
    """
    对于每一个点，任选另外一个点组成一条线，把他们左边的树都砍掉。
    暴力枚举最少砍掉的数量
    :param forest:
    :return:
    """
    if not forest or len(forest) <= 1:
        return [0]
    cuts = []
    for p in forest:
        minCut = len(forest)
        for q in forest:
            if q == p:
                continue
            # 砍掉以p，q左边的树
            cut = 0
            for r in forest:
                if r == q or r == p:
                    continue
                # r在p,q的左边pq X pr > 0
                pq = q[0]-p[0], q[1]-p[1]
                pr = r[0]-p[0], r[1]-p[1]
                if pq[0]*pr[1] - pq[1]*pr[0] > 0:
                    cut += 1
            minCut = min(cut, minCut)
        cuts.append(minCut)
    return cuts

def solve2(forest):
    """
    在solve1的基础上，选定p之后，把其它点按照和p的夹角排序，然后使用窗口滑动的方式判断左边最少有几棵树。
    需要注意的是：
    1. 窗口会越过数组末尾
    2. 同一个角度上有多颗树，不需要特殊处理因为不是最少需要砍掉的数量
    3. 浮点数的精度

    :param forest:
    :return:
    """

    if not forest or len(forest) <= 1:
        return [0]

    eps = 1e-15
    cuts = []
    for p in forest:
        angles = sorted([math.atan2(y-p[1], x-p[0]) for x, y in list(filter(lambda x: x != p, forest))])
        # angles = []
        # for q in forest:
        #     if q != p:
        #         angles.append(math.atan2(q[1]-p[1], q[0]-p[0]))
        # angles.sort()
        angles += [angle+2*math.pi for angle in angles]
        l = r = 0
        cut = len(angles)
        for i in range(len(angles) // 2):
            while l + 1 < len(angles) and angles[l] - angles[i] < eps:
                l += 1
            while r < len(angles) and angles[r] - angles[i] < math.pi - eps:
                r += 1
            cut = min(cut, r-l)
            if cut == 0:
                break
        cuts.append(cut)
    return cuts

startTime = datetime.datetime.now()
T = int(input())
for ti in range(1, T + 1):
    print('Case #%d:' % ti)
    N = int(input())
    forest = []
    for i in range(N):
        forest.append(list(map(int, input().split())))

    # figure = plt.figure('Trees')
    # xs = [pos[0] for pos in forest]
    # ys = [pos[1] for pos in forest]
    # plt.xlim(min(min(xs)*1.1, 0), max(max(xs)*1.1, 0))
    # plt.ylim(min(min(ys)*1.1, 0), max(max(ys)*1.1, 0))
    # plt.plot(xs, ys, 'ro')
    # plt.show()

    result = solve2(forest)
    for cut in result:
        print(cut)

sys.stderr.write('Time cost: {}'.format(datetime.datetime.now()-startTime))