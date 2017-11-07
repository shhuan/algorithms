# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-09 13:27
"""
__author__ = 'huash06'

import sys
import os


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
sys.stdin = open('input/C-large-practice.in', 'r')
sys.stdout = open('output/C-large-practice.out', 'w')

reader = Reader()
reader.read()

# sys.stdin = open('input/A-large-practice.in', 'r')
# sys.stdout = open('output/A-large-practice.out', 'w')

MAXNN = 301
T = int(sys.stdin.readline())

for ti in range(1, T + 1):
    # N, L = map(int, sys.stdin.readline().strip().split(' '))

    result = ''

    print('Case #{}: {}'.format(ti, result))