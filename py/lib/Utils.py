# -*- coding: utf-8 -*-

"""
created by 'huash' at '2015'-'03'-'26' '19':'17'
"""
__author__ = 'huash'

import sys
import re

class Reader:
    def __init__(self, data=None, path=None):
        if data is not None:
            self.data = list(data)
        elif path is not None:
            self.read(path)
        else:
            self.data = []

        self.index = -1

    def next_int(self):
        self.index += 1
        if self.index < len(self.data):
            return int(self.data[self.index])
        else:
            return None

    def read(self, path=None):
        if path is not None:
            self.data = list(self.read_impl(path))
        else:
            self.data = list(self.read_impl())

    def read_impl(self, path=None):
        if path is not None:
            for line in open(path):
                for val in line.split():
                    yield val
        else:
            for line in sys.stdin:
                for val in line.split():
                    yield val


# def outputBinaryTree1(root):
#     if not root:
#         return
#     q = [(root, 0, 0)]
#     res = []
#     ri = 0
#     li = 0
#     while q:
#         node, level, index = q.pop(0)
#         nri = level*(level+1)//2+index
#         while ri < nri:
#             res.append('#')
#             ri += 1
#         res.append(node.val)
#         ri += 1
#         if node.left:
#             q.append((node.left, level+1, 2*index))
#         if node.right:
#             q.append((node.right, level+1, 2*index+1))
#     print(''.join(map(str, res)))

def outputBinaryTree(root):
    if not root:
        print('#')
        return
    q = [root]
    res = [root.val]
    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
            res.append(node.left.val)
        else:
            res.append('#')
        if node.right:
            q.append(node.right)
            res.append(node.right.val)
        else:
            res.append('#')
    res = ''.join(map(str, res))
    res = re.sub('#+$', '', res)
    print(res)


