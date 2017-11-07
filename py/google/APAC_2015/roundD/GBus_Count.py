# -*- coding: utf-8 -*-

"""
created by 'huash06' at 2015-03-26 14:52

有多列公交车以及他们经过的城市的序号， 求某个城市有几个公交车经过

分析：
    记录下所有的区间， 然后对于给定个城市编号p，遍历所有区间，如果p在这个区间内这到达p的公车数量加1


可以使用区间树，但是使问题复杂化
"""
__author__ = 'huash06'

import sys
import os
import py.lib.TreeViewer

class IntervalTree:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.key = (left+right)/2
        self.left_child = None
        self.right_child = None
        self.count = 0
        self.delta = 0


    @property
    def children(self):
        return self.left_child, self.right_child

    def __str__(self):
        return '[{},\n{},\nc={},\nd={}]'.format(self.left, self.right, self.count, self.delta)

    def insert(self, left, right):
        """
        区间树在插入的时候分裂
        :param left:
        :param right:
        :return:
        """
        # print('Insert [{},{}] into [{}, {}]'.format(left, right, self.left, self.right))
        if self.left == left and self.right == right:
            # 如果插入的是已经存在的区间，就不分裂子树，但是下次如果子树分裂的话计数就会少1，所以使用一个delta。
            # 在查询的时候从根往子节点遍历的时候需要加上这个delta
            if self.left < self.right:
                self.delta += 1
            else:
                self.count += 1
        elif self.key > right:
            if self.left_child is None:
                self.left_child = IntervalTree(self.left, self.key)
            self.left_child.insert(left, right)
        elif self.key < left:
            if self.right_child is None and self.key+1 <= self.right:
                self.right_child = IntervalTree(self.key+1, self.right)
            self.right_child.insert(left, right)
        else:
            if self.left_child is None:
                self.left_child = IntervalTree(self.left, self.key)
            if self.right_child is None and self.key+1 <= self.right:
                self.right_child = IntervalTree(self.key+1, self.right)
            self.left_child.insert(left, self.key)
            if self.key+1 <= right:
                self.right_child.insert(self.key+1, right)

    def query(self, key):
        if key < self.left or key > self.right:
            # 如果要查的值不在区间内就直接返回
            return 0
        elif key <= self.key:
            if self.left_child is None:
                return self.count + self.delta
            return self.delta + self.left_child.query(key)
        else:
            if self.right_child is None:
                return self.count + self.delta
            return self.delta + self.right_child.query(key)


class Reader:
    def __init__(self, data=None):
        self.data = data
        self.index = -1

    def nextInt(self):
        self.index += 1
        if self.index >= len(self.data):
            return None
        return self.data[self.index]


def sys_ints():
    for line in sys.stdin:
        for d in line.split():
            if d.isdigit():
                yield int(d)

sys.stdin = open('input/B-large-practice.in', 'r')
sys.stdout = open('output/B-large-output-interval.txt', 'w')

input_data = list(sys_ints())
reader = Reader(input_data)

T = reader.nextInt()

# tree = IntervalTree(0, 10)
# tree.insert(1, 3)
for ti in range(1, T+1):
    N = reader.nextInt()
    intervals = list()
    min_left = sys.maxint
    max_right = 0
    for i in range(N):
        left = reader.nextInt()
        right = reader.nextInt()
        intervals.append((left, right))
        min_left = min(min_left, left)
        max_right = max(max_right, right)
    tree = IntervalTree(min_left, max_right)
    for l, r in intervals:
        tree.insert(l, r)
    result = list()
    P = reader.nextInt()
    for pi in range(P):
        p = reader.nextInt()
        result.append(tree.query(p))
    # TreeViewer.draw_tree(tree, 'interval_tree_{}.png'.format(ti))

    # 使用简单的遍历方式，O(n)的时间效率
    # P = reader.nextInt()
    # for pi in range(P):
    #     p = reader.nextInt()
    #     c = 0
    #     for interval in intervals:
    #         if p >= interval[0] and p <= interval[1]:
    #             c += 1
    #     result.append(c)
    print('Case #{}: {}'.format(ti, ' '.join(map(str, result))))
