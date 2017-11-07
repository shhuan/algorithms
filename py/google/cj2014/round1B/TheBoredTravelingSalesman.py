# -*- coding: utf-8 -*-

"""
created by huash at 2015-04-08 20:20
"""
__author__ = 'huash'

import sys
import os
from operator import itemgetter
import pydot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class Reader:
    def __init__(self, path=None):
        self.path = path
        self.index = -1
        self.data = []

    def next_int(self):
        self.index += 1
        if self.index < len(self.data):
            return int(self.data[self.index])
        else:
            return None

    def next_str(self):
        self.index += 1
        if self.index < len(self.data):
            return self.data[self.index]
        return None

    def read(self):
        self.data = list(self.read_impl())

    def read_impl(self):
        if self.path is not None:
            for line in open(self.path):
                for val in line.strip().split():
                    yield val
        else:
            for line in sys.stdin:
                for val in line.strip().split():
                    yield val

sys.stdin = open('input/sample.txt', 'r')
sys.stdin = open('input/C-small-practice.in', 'r')
sys.stdout = open('output/C-small-practice.out', 'w')

reader = Reader()
reader.read()


def edge_reachable(edges, active, dead, city):
    """
    判斷城市city是否可達，使用bfs判斷city與active的城市是否連通即可
    :param edges:
    :param active:
    :param dead:
    :param city:
    :return:
    """
    if len(active) <= 0:
        return False

    q = list()
    q.append(city)
    v = set()
    v.add(city)
    while len(q) > 0:
        head = q.pop()
        if head in active:
            return True
        for n in edges[head]:
            if n not in dead and n not in v:
                q.append(n)
                v.add(n)
    return False

def next_smallest_feasible_node_to_visit(edges, zips, dead, active, head):
    """
    從已經到達的城市active中找到下一個可以去的編號最小的城市
    :param edges:
    :param zips:
    :param dead: cities that can't be reached any more
    :param active: cities that passed and can return to
    :param head:
    :return:
    """
    temp = list()
    best = -1
    while len(active) > 0:
        head = active[-1]
        for city in edges[head]:
            if city not in dead and city not in active:
                if best == -1 or zips[city] < zips[best]:
                    best = city
        temp.append(head)
        dead.add(head)
        active.pop()

        if len(active) <= 0:
            break

        # 如果從當前city乘坐回程飛機，再也不會來當前城市。
        # 如果因此導致某些城市無法達到，不再回溯
        unreachable = False
        for city in edges[head]:
            if city not in dead and city not in active:
                if not edge_reachable(edges, active, dead, city):
                    unreachable = True
                    break

        if unreachable:
            break

    # 狀態恢復
    while len(temp) > 0:
        head = temp[-1]
        dead.remove(head)
        temp.pop()
        active.append(head)

    return best

def greedy(edges, zips, root):
    """
    Before we provide the pseudocode of the greedy algorithm, let’s define some variables.
    We provide examples that make use of these variables in subsequent paragraphs:

    DEAD: The set of nodes we’ve already visited and left (which we may never visit again).
    ACTIVE: The stack of nodes along our current path (originating from the source node).
    HEAD: The node at the top of the ACTIVE stack, which is the node we are currently on.
    At each step, we may either:

    Visit some not-yet-visited neighbor of HEAD, which adds the newly visited node to the
    top of the ACTIVE stack and make it as the new HEAD. This action is analogous to flying
    to a new city for the first time. Note that when we visit a new city, we should concatenate
    its zip code to our final answer.

    Leave HEAD, which pops HEAD from the ACTIVE stack and moves it to the DEAD set.
    This action is analogous to taking the return flight from HEAD using the return ticket
    used to visit HEAD. Note that we do not concatenate the city’s zip code to the final
    answer when leaving the city.
    :param edges:
    :param zips:
    :param root:
    :return:
    """
    dead = set()
    # active是一個棧，因為先到的城市肯定後返回，即先進後出
    active = list()
    active.append(root)
    answer = ''
    answer += zips[root]
    while len(active) > 0:
        head = active[-1]
        next = next_smallest_feasible_node_to_visit(edges, zips, dead, active, head)
        if next < 0 or next not in edges[head]:
            # 如果next<0，表示當前head不和其他沒去過的城市相連。
            # 如果下一個可以去的編號最小的城市不和head直接相連，把head移入dead之後不能再到達head是因為
            # 題目條件:
            # At most 1 outbound flight going to each city, although there is no limit on the
            # return flights (multiple return flights can go to the same city).
            dead.add(head)
            active.pop()
        else:
            # 選擇的下一個城市是從head出發，且一定是第一次到達。
            # 需要加上下一個城市的編號
            active.append(next)
            answer += zips[next]
    return answer



T = reader.next_int()
for ti in range(1, T + 1):
    N = reader.next_int()
    M = reader.next_int()

    zips = dict()
    for i in range(N):
        zips[i+1] = reader.next_str()

    graph = pydot.Dot(graph_type='graph', size='16', ratio="auto", rankdir='LR', K='1', sep="+1,+1", labelfloat='true', splines='true', dpi='300', pad=1, model='mds')

    edges = dict()
    for i in range(1, N+1):
        edges[i] = list()
    # gnodes = list()
    # gedges = list()
    for i in range(M):
        s = reader.next_int()
        t = reader.next_int()
        edges[s].append(t)
        edges[t].append(s)
        # if s not in gnodes:
        #     gnodes.append(s)
        # if t not in gnodes:
        #     gnodes.append(t)
        # if (s, t) not in gedges and (t, s) not in gedges:
        #     gedges.append((s, t))

    # for s in gnodes:
    #     graph.add_node(pydot.Node(s, label='{}\n{}'.format(s, zips[s])))
    # for e in gedges:
    #     graph.add_edge(pydot.Edge(e))
    #
    # op = 'output/graph-{}.png'.format(ti)
    # graph.write_png(op)

    # image = mpimg.imread(op)
    # plt.imshow(image)
    # plt.show()

    # for k, v in zips.values():
    # print(zips.values())
    # print(zips.items())

    sorted_zips = sorted(zips.items(), key=itemgetter(1))
    # print(sorted_zips)
    root = sorted_zips[0][0]

    # You can start your trip from any city you choose. You may not take an outbound flight to your starting city.
    # 由於城市是個連通圖，所以選取編號最小的城市出發一定能夠遊完所有城市，且得到最小的編號序列
    print('Case #{}: {}'.format(ti, greedy(edges, zips, root)))

