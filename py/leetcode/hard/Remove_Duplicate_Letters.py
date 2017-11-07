# -*- coding: utf-8 -*-
'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"




for "cbacdcbc", we counts each letter's index:

a----2
b----1,6
c----0,3,5,7
d----4
we go from a to d, to find the first letter who has a index smaller than the largest index of the rest. Here, index 2 of letter a is smaller than 6, 7, 4, so we first pick a; then we remove all index smaller than 2, and we have:

b----6
c----3,5,7
d----4
the next round we pick c not b, why ? cuz 6 of b is larger than 4, but 3 of c is smaller than 4 and 6.

b---6
d---4
then we pick d and b to form "acdb"

'''

import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return None

        indice = collections.defaultdict(list)

        for i, ch in enumerate(s):
            indice[ch].append(i)

        ret = []

        while indice:
            cds = []
            for ch, chi in indice.items():
                valid = True
                for k,v in indice.items():
                    if k != ch and max(v) < chi[0]:
                        valid = False
                if valid:
                    cds.append(ch)
            ch = min(cds)
            chidx = indice.pop(ch)[0]
            ret.append(ch)
            for k,v in indice.items():
                indice[k] = list(filter(lambda x: x > chidx, v))

        return "".join(ret)


s = Solution()
print(s.removeDuplicateLetters("dc"))
print(s.removeDuplicateLetters("c"))
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))
print(s.removeDuplicateLetters(""))
print(s.removeDuplicateLetters(None))