# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-16 15:53

小蒜头又调皮了。这一次，姐姐的实验报告惨遭毒手。
姐姐的实验报告上原本记录着从 1 到 n 的序列，任意两个数字间用空格间隔。
但是“坑姐”的蒜头居然把数字间的空格都给删掉了，整个数字序列变成一个长度为 1 到 100 的且首部没有空格的数字串。
现在姐姐已经怒了，蒜头找你写个程序快点把试验数据复原。
输入
输入文件有一行，为一个字符串——被蒜头搞乱的实验数据。
字符串的长度在 1 到 100 之间。
输出
输出共一行，为姐姐的原始测试数据—— 1 到 n 的输出。
任意两个数据之间有一个空格。
如果有多组符合要求的正确解，输出其中任意一组即可。
样例1
输入：
4111109876532
输出：
4 1 11 10 9 8 7 6 5 3 2
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections

line = raw_input()

if len(line) > 9:
    maxV = (len(line) - 9) // 2 + 9
else:
    maxV = len(line)
visited = [0 for x in range(maxV + 1)]
visited[0] = -1


def dfs(line, index, count):
    if index >= len(line):
        return True

    v1 = int(line[index])
    if visited[v1] == 0:
        visited[v1] = count
        if dfs(line, index + 1, count + 1):
            return True
        visited[v1] = 0

    v2 = int(line[index:index + 2])
    if v2 <= maxV and visited[v2] == 0:
        visited[v2] = count
        if dfs(line, index + 2, count + 1):
            return True
        visited[v2] = 0
    return False


if dfs(line, 0, 1):
    v = sorted([(i, x) for (x, i) in enumerate(visited)])
    print(' '.join(map(str, [x[1] for x in v[1:]])))
else:
    print('Fail')





