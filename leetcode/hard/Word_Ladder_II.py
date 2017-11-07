# -*- coding: utf-8 -*-

"""
created by huash at 2015-05-01 17:50

Given two words (start and end), and a dictionary,
find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.

"""
__author__ = 'huash'

import sys
import os
import collections
import itertools
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        """
        保持start到所有其他能够转换的字符串的最短距离，以及得到这个最短距离时候的所有前一个字符串。
        然后dfs遍历即可
        :param start:
        :param end:
        :param dict:
        :return:
        """
        if not start or not end or not dict:
            return []

        transfers = {}
        dict.add(end)
        q = [(1, start)]
        while q:
            steps, word = q.pop(0)
            nexts = self.nextWords(word, dict)
            # print('{} ==> {}'.format(word, nexts))
            for nextword in nexts:
                if nextword not in transfers:
                    transfers[nextword] = steps, [word]
                    q.append((steps+1, nextword))
                    continue
                presteps, prepres = transfers[nextword]
                if presteps > steps:
                    transfers[nextword] = (steps, [word])
                    q.append((steps+1, nextword))
                elif presteps == steps:
                    prepres.append(word)
                else:
                    pass
        # print(list(sorted(transfers.items(), key=lambda x: x[1][0])))
        return self.dfs(transfers, start, end, [end])

    def dfs(self, transfers, start, end, pres):
        if end not in transfers:
            return []
        steps, prewords = transfers[end]
        if steps == 1:
            return [[start] + pres]

        res = []
        for preword in prewords:
            res.extend(self.dfs(transfers, start, preword, [preword] + pres))
        return res

    def nextWords(self, word, dict):
        wl = list(word)
        res = set()
        for i in range(len(wl)):
            bk = wl[i]
            for j in range(26):
                ch = chr(j+ord('a'))
                if ch != bk:
                    wl[i] = ch
                aword = ''.join(wl)
                if aword in dict:
                    res.add(aword)
            wl[i] = bk
        return res

    def isNext(self, worda, wordb):
        if not worda or not wordb:
            return False
        if len(worda) != len(wordb):
            return False
        diff = 0
        for i in range(len(worda)):
            if worda[i] != wordb[i]:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1


s = Solution()
print(s.findLadders('hit', 'cog', {"hot","dot","dog","lot","log"}))
print(s.findLadders('hit', 'dog', {'hot', 'dog'}))
print(s.findLadders("qa", "sq", {"si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"}))

# print(s.findLadders2('hit', 'cog', {"hot","dot","dog","lot","log"}))
# print(s.findLadders2('hit', 'dog', {'hot', 'dog'}))
# print(s.findLadders2("qa", "sq", {"si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"}))
#
#
