# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-17 11:30
"""
__author__ = 'huash'

import sys
import os
import random
sys.stdout = open('sampleF-gen.txt', 'w')

caseCount = 100
print(caseCount)

for ci in range(caseCount):
    N = random.randint(1, 10)
    K = random.randint(1, 4)
    print(N, K)


