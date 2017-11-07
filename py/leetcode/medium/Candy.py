# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-27 10:05


There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings:
            return 0

        cadies = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and cadies[i] < cadies[i-1]+1:
                cadies[i] = cadies[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and cadies[i] < cadies[i+1]+1:
                cadies[i] = cadies[i+1]+1
        return sum(cadies)