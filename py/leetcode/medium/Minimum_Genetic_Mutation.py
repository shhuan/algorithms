# -*- coding: utf-8 -*-
"""

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3


"""

import collections
import itertools

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        if end not in bank:
            return -1

        def next_state(state):
            sg = ['A', 'C', 'G', 'T']
            return list(filter(lambda x: x in bank, [state[:i] + u + state[i + 1:] for u in sg for i in range(len(state))]))

        qs = {start}
        vs = {start}
        qe = {end}
        ve = {end}
        steps = 0
        while qs and qe:
            print(">>>>>", qs)
            print("<<<<<", qe)
            steps += 1
            qs = set(itertools.chain(*[next_state(s) for s in qs])) - vs
            vs |= qs

            if qs & qe:
                print("==========")
                print(qs, qe)
                return steps

            steps += 1
            qe = set(itertools.chain(*[next_state(s) for s in qe])) - ve
            ve |= qe

            if qs & qe:
                print("==========")
                print(qs, qe)
                return steps

        return -1


s = Solution()
print(s.minMutation("AAAAAAAA", "CCCCCCCC", ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]))
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

print(s.minMutation(start, end, bank))
print(s.minMutation("AACCGGTT", "AACCGGTA", []))

print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
