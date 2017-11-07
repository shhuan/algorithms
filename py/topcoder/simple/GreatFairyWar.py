# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-06 15:59
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class GreatFairyWar:
    def minHP(self, dps, hp):
        if not dps or not hp:
            return 0

        attack = sum(dps)
        res = 0
        enemies = len(dps)
        for i, h in enumerate(hp):
            res += h * attack
            attack -= dps[i]
            enemies -= 1
        return res



s = GreatFairyWar()
print(s.minHP([1, 2], [3, 4]))
