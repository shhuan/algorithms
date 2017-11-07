# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-16 15:27

赛车比赛在潘多拉星球变得越来越流行了。但是他们的比赛跟我们平常的不太一样：n 辆赛车在一条长长的直道上展开同台竞技。每辆赛车的速度都为 1m/s，整条赛道在每一米都有坐标标记。
在比赛的赛车中，赛车 i 从 0 秒开始由 ai 向 bi 移动。到达 bi 之后转而返回由 bi 向 ai 移动。循环往复。
又是蒜头菌！原来这是蒜头菌正在玩的一个手机小游戏。蒜头菌可以在某些位置放下 TNT 炸毁某些赛车。因为他有 m 个问题。其中，问题 j 是：在 tj 时刻，在 xi 到 yi 之间共有几辆赛车？
你的任务就是回答萌蒜头的问题。
输入
输入的第一行包含两个数字 n 和 m（1 ≤ n, m ≤ 1000），分别代表正在比赛的赛车数量和蒜头的问题数。
接下来的 n 行中，每行包含 2 个整数 ai、bi（0 ≤ ai, bi ≤ 109, ai != bi），分别代表赛车 i 的起点和终点。
再接下来的 m 行中，每行包含 3 个整数 xj，yj，tj（0 ≤ xj ≤ yj ≤ 109, 0 ≤ tj ≤ 109)，分别代表问题 j 的左右坐标边界和询问的时间。
输出
输出共有 m 行，每行各有一个整数，分别代表对应的 m 个问题的答案。
样例1
输入：
5 5
0 1
0 2
2 3
3 5
4 5
0 5 0
0 1 2
0 2 1
2 5 2
2 5 3
输出：
5
1
2
4
3

"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections


N, M = [int(x) for x in raw_input().split()]
loops = []
for i in range(N):
    s, t = [int(x) for x in raw_input().split()]
    loops.append((s, t))

for i in range(M):
    x, y, t = [int(x) for x in raw_input().split()]
    count = 0
    for l, r in loops:
        if l > y or r < x:
            continue
        c = l
        length = r - l
        if (t // length) & 1 == 0:
            c += t % length
        else:
            c += length - t % length
        if x <= c <= y:
            count += 1
    print(count)


