# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-07 11:40

一個餅乾遊戲，開始時候會每秒鐘產生2塊餅乾，當收集到C塊餅乾的時候可以製造一架餅乾機器，
餅乾製造機每秒鐘可以生產F塊餅乾。

要求計算最少需要多少時間能夠生產X塊餅乾。


分析：
分別計算生產k架機器時，製造X塊餅乾需要的時間，
T = Tm+Tx, Tm是生產機器花的時間，Tx是有m架機器時生產X塊餅乾需要的時間
Tm = sigma{C/(F*(k-2)+1)}, k>=2
Tm = 0, k<2, 假設初始有一台秒產量為2的機器
Tx = X/(F*(k-2)+2)



"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

__DEBUG__ = True

sys.stdin = open('input/B-small-practice.in', 'r')
sys.stdout = open('output/B-small-practice.out', 'w')


T = int(sys.stdin.readline())
for ti in range(1, T+1):
    C, F, X = map(float, sys.stdin.readline().strip().split(' '))

    # 總共K個餅乾製造機，初始一個
    K = 1
    # T表示K個餅乾製造機的時候需要的時間，時間是先遞減後遞增
    T = X/2.0
    # tc表示生產K個餅乾製造機器所花費的時間
    tc = 0
    while True:
        K += 1
        tc += C/(F*(K-2)+2)
        t = tc + X/(F*(K-1)+2)
        if t < T:
            T = t
        if t > T:
            break
    print('Case #%d: %.7f' % (ti, T))