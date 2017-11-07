# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-16 08:53

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections


class Solution:
    # @param s, a string
    # @return a string[]
    def restoreIpAddresses(self, s):
        if not s:
            return []
        return self.dfs(s, '', 0)


    def dfs(self, rawstr, ipaddr, count):
        # print('{}, {}, {}'.format(rawstr, ipaddr, count))
        if not rawstr:
            if count == 4:
                return [ipaddr]
            return []
        if count >= 4:
            return []
        elif len(rawstr) // (4-count) > 3:
            return []
        result = []
        if rawstr[0] == '0':
            nextip = ''
            if ipaddr:
                nextip = ipaddr+'.0'
            else:
                nextip = ipaddr+'0'
            result.extend(self.dfs(rawstr[1:], nextip, count+1))
            return result
        for i in range(1, len(rawstr)+1):
            if int(rawstr[:i]) <= 255:
                nextip = ''
                if ipaddr:
                    nextip = ipaddr+'.'+rawstr[:i]
                else:
                    nextip = ipaddr+rawstr[:i]
                result.extend(self.dfs(rawstr[i:], nextip, count+1))
            else:
                break
        return result


s = Solution()
print(s.restoreIpAddresses('25525511135'))
print(s.restoreIpAddresses('010010'))