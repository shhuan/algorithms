# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-10 16:37



1. 暴力枚举可以过掉小数据
2. 使用区间树行不通，
    因为假设查询区间[l,r]，区间树上面可以直接查询得到[l, a]和[a+1, r]合并的复杂度是(a-l+1)*(r-a)


"""
__author__ = 'huash'

import sys
import os
import collections
# import py.lib.TreeViewer as TreeViewer
#
# sys.stdin = open('input/sampleG.txt', 'r')
# sys.stdout = open('output/-small-practice.out', 'w')


class TreeNode:
    def __init__(self, l, r):
        self.left = l
        self.right = r
        self.wc = collections.defaultdict(int)
        self.leftChild = None
        self.rightChild = None
        self.q0 = 0
        self.q1 = 0
        self.q2 = 0

    def __str__(self):
        return '[{},{}]\n{},{},{}'.format(self.left, self.right, self.q0, self.q1, self.q2)

    def __getattr__(self, item):
        if item == 'children':
            if self.leftChild and self.rightChild:
                return [self.leftChild, self.rightChild]
            elif self.leftChild:
                return [self.leftChild]
            elif self.rightChild:
                return [self.rightChild]
            else:
                return []


def buildTreeFromRange(left, right):
    if left > right:
        return None
    if left == right:
        return TreeNode(left, right)
    root = TreeNode(left, right)
    mid = left + (right - left) // 2
    root.leftChild = buildTreeFromRange(left, mid)
    root.rightChild = buildTreeFromRange(mid+1, right)
    return root


def calCharCount(p, root):
    if not root:
        return
    if root.left == root.right:
        root.wc[p[root.left]] = 1
        return
    calCharCount(p, root.leftChild)
    calCharCount(p, root.rightChild)
    # print(root.leftChild.wc)
    # print('items {} '.format(root.leftChild.wc.items()))
    for k, v in root.leftChild.wc.items():
        root.wc[k] += v
    for k, v in root.rightChild.wc.items():
        root.wc[k] += v
    root.q0 = root.leftChild.q0 + root.rightChild.q0
    root.q1 = root.leftChild.q1 + root.rightChild.q1
    root.q2 = root.leftChild.q2 + root.rightChild.q2

    mid = (root.left + root.right) // 2
    l = root.left
    r = root.right
    for i in range(mid-l+1):
        wc = collections.defaultdict(int)
        for k in range(i+1):
            wc[p[mid-i]] += 1
        for j in range(r-mid):
            wc[p[mid+j+1]] += 1
            if sum(wc.values()) % 2 == 0 and \
                len(list(filter(lambda x: x%2 != 0, wc.values()))) == 0:
                wl = i+j+2
                root.q0 += 1
                root.q1 += wl
                root.q2 += wl*wl

    return


def buildTreeFromString(p):
    n = len(p)
    root = buildTreeFromRange(0, len(p)-1)
    calCharCount(p, root)
    return root






def solve(p, l, r, type):
    l -= 1
    r -= 1
    res = 0
    for i in range(l, r):
        for j in range(i+1, r+1):
            if isBalancedString(p, i, j):
                res += pow(j-i+1, type)
    # print(l+1, r+1, type, res)
    return res

def isBalancedString(p, l, r):
    """
    根据平衡字符串的定义，如果一个字符串中每个自负出现的次数是偶数，那么这个字符串就是平衡字符串。
    :param p:
    :param l:
    :param r:
    :return:
    """
    if r <= l:
        return False
    if (r-l+1) % 2 != 0:
        return False
    charCount = collections.defaultdict(int)
    for i in range(l, r+1):
        charCount[p[i]] += 1
    return len(list(filter(lambda x: x%2 != 0, charCount.values()))) == 0


def solveInTree(root, p, l, r, type):
    l -= 1
    r -= 1
    # res = 0
    # for i in range(l, r):
    #     for j in range(i+1, r+1):
    #         if isBalancedStrInTree(root, i, j):
    #             res += pow(j-i+1, type)
    # # print(l+1, r+1, type, res)
    # return res
    return queryInTree(root, p, l, r, type)

def queryInTree(root, p, l, r, type):
    if r <= l:
        return 0
    return queryInTreeImpl(root, p, l, r, type)

def queryInTreeImpl(root, p, l, r, type):
    if l == root.left and r == root.right:
        if type == 0:
            return root.q0
        elif type == 1:
            return root.q1
        else:
            return root.q2

    mid = (root.left + root.right) // 2
    if l > mid:
        return queryInTreeImpl(root.rightChild, p, l, r, type)
    elif r <= mid:
        return queryInTreeImpl(root.leftChild, p, l, r, type)
    else:
        ql = queryInTreeImpl(root.leftChild, p, l, mid, type)
        qr = queryInTreeImpl(root.rightChild, p, mid+1, r, type)
        res = ql + qr

        mid = root.leftChild.right
        for i in range(mid-l+1):
            wc = collections.defaultdict(int)
            for k in range(i+1):
                wc[p[mid-i]] += 1
            for j in range(r-mid):
                wc[p[mid+j+1]] += 1
                if sum(wc.values()) % 2 == 0 and \
                    len(list(filter(lambda x: x%2 != 0, wc.values()))) == 0:
                    if type == 0:
                        res += 1
                    elif type == 1:
                        res += (j-i+1)
                    else:
                        res += pow(j+i+2, 2)
        return res

def isBalancedStrInTree(root, l, r):
    if r <= l:
        return False
    if (r-l+1) % 2 != 0:
        return False
    wc = charCountInTree(root, l, r)
    return len(list(filter(lambda x: x%2 != 0, wc.values()))) == 0
def charCountInTree(root, l, r):

    if l == root.left and r == root.right:
        return root.wc
    if r < root.left or l > root.right:
        return {}

    mid = (root.left + root.right) // 2

    if l > mid:
        return charCountInTree(root.rightChild, l, r)
    elif r <= mid:
        return charCountInTree(root.leftChild, l, r)
    else:
        leftwc = charCountInTree(root.leftChild, l, mid)
        rightwc = charCountInTree(root.rightChild, mid+1, r)
        wc = collections.defaultdict(int)
        for k, v in leftwc.items():
            wc[k] += v
        for k, v in rightwc.items():
            wc[k] += v
        return wc


def decode(p, queries):
    a = 0
    b = 0
    n = len(p)

    root = buildTreeFromString(p)
    # TreeViewer.draw_tree(root, 'tree.png')


    for x, y, type in queries:
        l = (x + a) % n + 1
        r = (y + b) % n + 1
        if l > r:
            l, r = r, l
        # ans = solve(p, l, r, type)
        ans = solveInTree(root, p, l, r, type)
        print(ans)
        a, b = b, ans


T = int(input())
for ti in range(1, T + 1):
    p = input()
    q = int(input())
    queries = []
    for qi in range(q):
        l, r, type = list(map(int, input().split()))
        queries.append((l, r, type))
    decode(p, queries)