# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-10 08:21

有一些連接火車車廂，計算能把它們拼成多少種合法的火車。
每一節火車車廂上有一個字母，合法的意思是所有一樣的字母必須相連。
比如有3個相連的車廂集合
a-b, b-c, c-d
他們可以組成一個合法火車a-b-b-c-c-d。

如果車廂集合是
a-b-c, b-c-d
就不能組合成合法的火車。

注意如果有兩個火車集合
a, a-a
他們能夠組成合法火車的方式有2種，而不是一種。



分析：
1. 把火車分組，不同組之間的火車之間沒有任何順序關聯性。
    比如 [a-b, b-c] 和 [d-e]
2. 判斷能否組成合法的火車，條件是：
    1. 同一組內的所有火車如果按照任意一種頭尾相連的方式組合之後是合法的
    2. 不同組的車廂上的字母不一樣
3. 計算數量
    count = mul{count_group(i)} * fact(group_count)
        fact(group_cout)是group_count的阶乘，group_count是分组的数量
        mul{count_group(i)} = count_group(1)*count_group(2)*...*count_group(group_count)
        count_group(i)是第i组内部合法的摆放数量
            count_group(i) = mul{fact(j)}
                mul{fact(j)} = fact(s1)*...*fact(sn)
                在一个组内，如果两个火车段可以互换位置的条件是他们都是同一个字母的集合，比如
                a-b,b,b-b,b-b-b,b-b,b-c
                中b,b-b,b-b-b,b-b的位置可以互换，其数量是fact(4) == 24.
                fact(si)中si表示第i组一样的字母集合的火车车厢数量，上面的例子si=4，fact(si)=24



"""
__author__ = 'huash06'

import sys
import os
import functools

sys.stdin = open('input/sample.txt', 'r')
sys.stdin = open('input/B-small-practice.in', 'r')
sys.stdout = open('output/B-small-practice.out', 'w')

sys.stdin = open('input/B-large-practice.in', 'r')
sys.stdout = open('output/B-large-practice.out', 'w')

MAXNN = 301
__DEBUG__ = False


def is_adjacent(groups):
    """
    After group cars into different group,
    check whether all same character are adjacent.

    1. If same characters occur in different group, them are not adjacent.
    2. If same characters only occur in one group, but them are not adjacent, them are not adjacent.

    :param groups:
    :return: true if all all same character are adjacent.
    """
    used = set()
    pre = ''
    for group in groups:
        for car in group:
            for ch in car:
                if pre == '':
                    pre = ch
                    used.add(ch)
                else:
                    if ch != pre:
                        if ch in used:
                            return False
                        else:
                            used.add(ch)
                            pre = ch
    return True


def add_car_into_group(group, car):
    """
    If car can be inserted into group, it must satisfy one of below condition:
    1. Insert into middle.
        insert car into .*b->b.* ==> car == b+
    2. Insert into first.
        car[-1] == group[0][0]
    3. Insert into last.
        car[0] == group[-1][-1]
    :param group:
    :param car:
    :return:
    """
    if len(group) <= 0:
        group.append(car)
        return True
    if car[-1] == group[0][0]:
        group.insert(0, car)
        return True
    elif car[0] == group[-1][-1]:
        group.append(car)
        return True
    for i in range(1, len(group)):
        if group[i-1][-1] == car[0] and group[i][0] == car[-1]:
            group.insert(i, car)
            return True
    return False


def group_cars(car_list):
    """
    Put cars in different group, cars are in same group when them can be linked together.

    like [ab, bb, bc] is a group, because the can make ab->bb->bc.
    but [ab, ab] is not a group.

    If there are 3 cars [ab, bc, bd] in total, them will be putted in 2 groups:
    Maybe [ab, bc], [bd] or [ab, bd], [bc].
    I don't care which one is final result, because all of them will be judged in valid in 'is_adjacent()'.

    Further more, if one character occurs in different groups, these cars can't make a valid train.

    :param car_list:
    :return:
    """
    if __DEBUG__:
        print('GROUPING CARS')
        print(car_list)
    groups = []
    group = []
    grouped = [0]*len(car_list)
    while grouped.count(0) > 0:
        for i in range(len(car_list)):
            if grouped[i] == 0:
                group = [car_list[i]]
                grouped[i] = 1
                break
        found_one = True
        while found_one:
            found_one = False
            for i in range(len(car_list)):
                if grouped[i] == 0:
                    if add_car_into_group(group, car_list[i]):
                        grouped[i] = 1
                        found_one = True
        groups.append(group)
        group = []
    if __DEBUG__:
        print('GROUPED CARS')
        for group in groups:
            print(group)
    return groups


def count_group(car_group):
    count = 1
    repeat = 1
    pre = ''
    for car in car_group:
        if pre == '':
            if car[0] == car[-1]:
                pre = car
                repeat = 1
        else:
            if pre[-1] == car[0] == car[-1]:
                repeat += 1
            else:
                pre = ''
                count *= perm_count(repeat)
                count %= 1000000007
                repeat = 1
    count *= perm_count(repeat)
    count %= 1000000007
    return count


def perm_count(N):
    count = 1
    for i in range(1, N+1):
        count *= i
        count %= 1000000007
    return count


T = int(input())
for ti in range(1, T + 1):

    N = int(input())
    car_set = input().split(' ')
    grouped_cars = group_cars(car_set)

    valid_count = 1
    if is_adjacent(grouped_cars):
        for gc in grouped_cars:
            valid_count *= count_group(gc)
            valid_count %= 1000000007
        valid_count *= perm_count(len(grouped_cars))
        valid_count %= 1000000007
    else:
        if __DEBUG__:
            print('INVALID CAR SET')
            print(car_set)
        valid_count = 0

    print('Case #{}: {}'.format(ti, valid_count))
    if __DEBUG__:
        print('=====================')
