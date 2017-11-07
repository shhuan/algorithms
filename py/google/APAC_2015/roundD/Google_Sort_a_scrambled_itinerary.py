# -*- coding: utf-8 -*-

"""

题意： 有很多张飞机票，上面有出发地和目的地，每个城市只到一次，根据这些飞机票找出旅行路线，路线是确定的唯一一条。

分析： 用Map保存所以得机票信息，找出始发城市，即只出现一次的出发地，然后逐个遍历下一个城市即可

"""
__author__ = 'huash06'

import sys
import os


# print(os.getcwd())
sys.stdin = open('input/C-large-practice.in', 'r')
sys.stdout = open('output/C-large-practice.out', 'w')

T = int(sys.stdin.readline())
for case_index in range(1, T + 1):
    N = int(sys.stdin.readline())
    itinerary = dict([])
    count = dict([])
    for iti in range(N):
        depart = sys.stdin.readline().rstrip()
        destination = sys.stdin.readline().rstrip()

        count[depart] = 1 if count.get(depart) is None else count[depart] + 1
        count[destination] = 1 if count.get(destination) is None else count[destination] + 1
        itinerary[depart] = destination
    # print(itinerary)

    depart = None
    destination = None
    depart_count = 0
    for k, v in count.items():
        if v == 1:
            if itinerary.get(k) is not None:
                depart = k
            else:
                destination = k

    sys.stdout.write('Case #{}:'.format(case_index))
    while itinerary.get(depart) is not None:
        sys.stdout.write(' {0}-{1}'.format(depart, itinerary[depart]))
        depart = itinerary[depart]
    print('')