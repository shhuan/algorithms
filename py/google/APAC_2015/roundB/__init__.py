# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-03 13:55
"""
__author__ = 'huash06'

import sys
import os
import py.lib.Utils as Utils

__DEBUG__ = True

if __DEBUG__:
    sys.stdin = open('input/sample.txt', 'r')

# sys.stdin = open('input/A-large-practice.in', 'r')
# sys.stdout = open('output/A-large-practice.out', 'w')

MAXNN = 301
reader = Utils.Reader()