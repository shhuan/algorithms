# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-08 09:48

有N排插線孔，每排有L位。
另外有L個開關，每個開關控制一列插線孔。
要求操作最少數量的開關使得N的設備能同時充電。

假設插線孔是
Outlet 0: 10
Outlet 1: 01
Outlet 2: 11

設備是
Device 0: 00
Device 1: 11
Device 2: 10

操作第二列開關使得插線孔變為：
Outlet 0: 11
Outlet 1: 00
Outlet 2: 10

這時按照如下對應方式充電即可
Device 0: Outlet 1
Device 1: Outlet 0
Device 2: Outlet 2



分析：

需要找到一個開關組合(1?0?){L,L}，L位每位是0或1的開關，
如果第i位是1，就反轉第i列的所有插線孔，否則不變。

暴力解O(2^L)只能解決小輸入。

需要注意到的是一個合法的開關組合至少能夠使得一排插線孔對應上一個設備。
所以只需要假設第一排插線孔能夠被第i個設備使用，再判斷此時的開關組合是否合法即可。

1. 假設：Outlet[0] + Switch = Device[i]
2. 根據Switch操作所有Outlet, Outlet[i] + Switch = Switched_Outlet[i]
3. 對Device 和 Switched_Outlet分別排序
4. 如果Device[i] == Switched_Outlet[i], 0<=i<=N，
    這個Switch是可能的

需要找到所有的可能的Switch，然後挑選一個調整數量最少的。


"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

__DEBUG__ = True

if __DEBUG__:
    sys.stdin = open('input/sample.txt', 'r')

sys.stdin = open('input/A-large-practice.in', 'r')
sys.stdout = open('output/A-large-practice.out', 'w')

MAXNN = 301

def verify(outlets, devices, switch):
    switched_outltes = list()
    for i in range(len(outlets)):
        outlet = list()
        for j in range(len(switch)):
            if switch[j] == '1':
                if outlets[i][j] == '1':
                    outlet.append('0')
                else:
                    outlet.append('1')
            else:
                outlet.append(outlets[i][j])
        switched_outltes.append(outlet)

    for di in range(len(devices)):
        if devices[di] not in switched_outltes:
            return False
    return True


T = int(sys.stdin.readline())
for ti in range(1, T+1):

    N, L = map(int, sys.stdin.readline().strip().split(' '))

    OUTLETS = map(list, sys.stdin.readline().strip().split(' '))
    DEVICES = map(list, sys.stdin.readline().strip().split(' '))
    SWITCH = ['0'] * L

    count = MAXNN
    for i in range(len(DEVICES)):
        device = DEVICES[i]
        outlet = OUTLETS[0]
        SWITCH[:] = '0'*L
        for j in range(L):
            if device[j] != outlet[j]:
                SWITCH[j] = '1'
            else:
                SWITCH[j] = '0'
        if verify(OUTLETS, DEVICES, SWITCH):
            c = SWITCH.count('1')
            if c < count:
                count = c
    if count < MAXNN:
        print('Case #{}: {}'.format(ti, count))
    else:
        print('Case #{}: NOT POSSIBLE'.format(ti))
