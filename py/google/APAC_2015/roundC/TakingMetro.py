# -*- coding: utf-8 -*-

"""
created by huash06


有一个地铁线路图，给出以下信息：
1. 每条线路上每一站之间的运行时间；
2. 换乘通道以及通过换乘通道的时间；
3. 乘客在上车之前需要等待，给出了每条线路的等待时间

计算给定的起始站到目的站所需要的最短时间

一开始想到用BFS计算最短路径，由于有些站需要等待，处理起来非常困难。
下面是我一开始的不正确解法：

initialize(Q)
Q <- departStation
while Q is not empty:
    S <- first elemet of Q
    update time of stations which linked to S
    Q <- add all updated stations

假设先搜索到乘客不经过换乘到达换乘站s1的时间是t1，而后又搜索到乘客经过换乘通道来到站s1的时间是t2；
如果t2<t1，更新TRAVEL_TIME[s1]=t2；然后从队列中取出s1，更新s1的下一站s2的时间为t2+t(s1,s2)，
而实际时间应该为t1+t(s1,s2)或者t2+t(s1,s2)+wait。
所以如果使用这种方式，必须为每个站记录多个时间，使得复杂度上升。

比较简单的方法是在更新到达某一个站的最短时间的同时，先更新整体线路上所有站点的时间，
然后在以这条线路上的换乘站为起点更新其他线路上所有站点的时间。

类似于多线程的原子操作。



"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils
import pydot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

__DEBUG__ = True

# if __DEBUG__:
#     sys.stdin = open('input/sample.txt', 'r')


sys.stdin = open('input/B-small-practice.in', 'r')
# sys.stdin = open('input/sample.txt', 'r')
sys.stdout = open('output/B-small-practice.out', 'w')

MAXNN = 301
reader = Utils.Reader()
reader.read()
T = reader.next_int()

# TRAVEL_TIME[i][j means time cost to line i station j
TRAVEL_TIME = [[0 for row in range(MAXNN)] for col in range(MAXNN)]

# STATION_GAP[(i,j)=t means from line i station j to line i staion j+1 will cost time t
STATION_GAP = dict()

# STATION_COUNT[i] means count of stations of line i
STATION_COUNT = dict()

# TRANSFER_STATION[(i,j)] = (k, l, t) means from line i station j to line k station l will cost time t
TRANSFER_STATION = dict()

# WAIT_TIMT[i] = t means customer need wait time t to get up train
WAIT_TIME = dict()

# PATH[(i, j)] = (k, l) means customer arrived at line i station j from line k station l
PATH = dict()


def travel_on_line(position):
    """
    travel from line position[0] station position[1]
    :param position: 2d tuple (i,j) means line i station j
    :param waiting: boolean to indication whether customer is on train
    :return:
    """
    line = position[0]
    station = position[1]

    # wt = WAIT_TIME[line] if waiting else 0
    cost = TRAVEL_TIME[line][station]+WAIT_TIME[line]
    updated = list()
    for si in range(station+1, STATION_COUNT[line]+1):
        cost += STATION_GAP[(line, si-1)]
        if cost < TRAVEL_TIME[line][si]:
            updated.append((line, si))
            TRAVEL_TIME[line][si] = cost
            PATH[(line, si)] = (line, si-1)

    cost = TRAVEL_TIME[line][station]+WAIT_TIME[line]
    for si in range(station-1, 0, -1):
        cost += STATION_GAP[(line, si)]
        if cost < TRAVEL_TIME[line][si]:
            updated.append((line, si))
            TRAVEL_TIME[line][si] = cost
            PATH[(line, si)] = (line, si+1)

    transfer(position)
    for p in updated:
        transfer(p)


def transfer(position):
    """
    
    :param position: 2d tuple (i,j) means line i station j 
    :return:
    """
    tfs = TRANSFER_STATION.get(position)
    if tfs is not None:
        line = position[0]
        station = position[1]
        for tf in tfs:
            dest_line = tf[0]
            dest_station = tf[1]
            transfer_time = tf[2]
            dest = (dest_line, dest_station)
            cost = TRAVEL_TIME[line][station] + transfer_time
            if cost < TRAVEL_TIME[dest_line][dest_station]:
                TRAVEL_TIME[dest_line][dest_station] = cost
                PATH[dest] = position
                travel_on_line(dest)


def drawMetroLine(dest, outputPath):
    """
    draw result
    :return:
    """
    COLORS = ['#00CCCC', '#CC00CC', '#CC0066', '#00CC66', '#0066CC', '#66CC00', '#CC0000', '#CCCC00', '#6600CC', '#CC6600']

    graph = pydot.Dot(graph_type='digraph', size='16', ratio="auto", rankdir='LR', K='1', sep="+1,+1", labelfloat='true', splines='true', dpi='300', pad=1, model='mds')


    path = dict()

    d = dest
    pos = PATH.get(d)
    while pos is not None:
        path[pos] = d
        d = pos
        pos = PATH.get(d)


    # 画出所有站
    for li in range(1, N+1):
        for si in range(1, STATION_COUNT[li]+1):
            label = si
            if si == 1:
                label = 'L{}\nW{}'.format(li, WAIT_TIME[li])
            sn = pydot.Node('{}.{}'.format(li, si), label=label, style='filled', color=COLORS[li-1])
            if (li, si) == depart or (li, si) == dest:
                sn.set_style('dashed')
            graph.add_node(sn)

        # 画出同一条线路上站点间的连线
        for si in range(1, STATION_COUNT[li]):
            edge = pydot.Edge('{}.{}'.format(li, si), '{}.{}'.format(li, si+1), label='{}'.format(STATION_GAP[(li, si)]), dir='both')
            s = (li, si)
            t = (li, si+1)
            ct = 0
            if path.get(s) is not None and path.get(s) == t:
                edge.set_dir('forward')
                ct = TRAVEL_TIME[t[0]][t[1]]
            elif path.get(t) is not None and path.get(t) == s:
                edge.set_dir('back')
                ct = TRAVEL_TIME[s[0]][s[1]]
            if ct > 0:
                edge.set_color('red')
                edge.set_label('{} {}'.format(STATION_GAP[(li, si)], ct))
            graph.add_edge(edge)

    # 画出换乘站的连线
    drawed = list()
    for k, tfs in TRANSFER_STATION.items():
        for tf in tfs:
            es = '{}.{}'.format(k[0], k[1])
            et = '{}.{}'.format(tf[0], tf[1])
            if (es, et) in drawed:
                continue
            drawed.append((es, et))
            drawed.append((et, es))
            edge = pydot.Edge(es, et, label='{}'.format(tf[2]), color='#00900', dir='both')
            s = k
            t = (tf[0], tf[1])
            ct = 0
            if path.get(s) is not None and path.get(s) == t:
                edge.set_dir('forward')
                ct = TRAVEL_TIME[t[0]][t[1]]
            elif path.get(t) is not None and path.get(t) == s:
                edge.set_dir('back')
                ct = TRAVEL_TIME[s[0]][s[1]]
            if ct > 0:
                edge.set_label('{} {}'.format(tf[2], ct))
                edge.set_color('red')
            graph.add_edge(edge)

    graph.write_png(outputPath)

if __name__ == '__main__':
    for ti in range(1, T+1):
        print('Case #{}:'.format(ti))
        N = reader.next_int()

        STATION_GAP.clear()
        STATION_COUNT.clear()
        TRANSFER_STATION.clear()

        for ni in range(1, N+1):
            sc = reader.next_int()
            STATION_COUNT[ni] = sc
            waitTime = reader.next_int()
            WAIT_TIME[ni] = waitTime
            time = list()
            for i in range(1, sc):
                tij = reader.next_int()
                STATION_GAP[(ni, i)] = tij

        M = reader.next_int()
        for mi in range(M):
            s = reader.next_int()
            ss = reader.next_int()
            t = reader.next_int()
            ts = reader.next_int()
            tt = reader.next_int()
            tfs = TRANSFER_STATION.get((s, ss))
            if tfs is None:
                TRANSFER_STATION[(s, ss)] = list()
            TRANSFER_STATION[(s, ss)].append((t, ts, tt))
            tfs = TRANSFER_STATION.get((t, ts))
            if tfs is None:
                TRANSFER_STATION[(t, ts)] = list()
            TRANSFER_STATION[(t, ts)].append((s, ss, tt))

        Q = reader.next_int()
        for qi in range(Q):
            s = reader.next_int()
            ss = reader.next_int()
            t = reader.next_int()
            ts = reader.next_int()
            depart = (s, ss)
            dest = (t, ts)

            # reset global virables
            for i in range(MAXNN):
                for j in range(MAXNN):
                    TRAVEL_TIME[i][j] = 100000
            PATH.clear()

            TRAVEL_TIME[s][ss] = 0
            travel_on_line((s, ss))

            if TRAVEL_TIME[t][ts] < 100000:
                print(TRAVEL_TIME[t][ts])
                drawMetroLine((t, ts), 'output/{}-{}.png'.format(ti, qi))
            else:
                print(-1)
