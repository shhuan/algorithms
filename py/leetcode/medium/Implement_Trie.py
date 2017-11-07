# -*- coding: utf-8 -*-
"""
created by huash at 2015/9/4 10:35

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""
__author__ = 'huash'

import sys
import os
import datetime
import functools
import itertools
import collections


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit = False

        # 476ms
        # Your runtime beats 32.05% of python coders.
        # self.children = [None] * 26

        # OOM
        # self.children = collections.defaultdict(TrieNode)

        # 312 ms
        # Your runtime beats 97.44% of python coders.
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return
        node = self.root
        # for ch in word:
        #     i = self.indexOfChar(ch)
        #     if not node.children[i]:
        #         node.children[i] = TrieNode()
        #     node = node.children[i]
        # node.hit = True

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.hit = True



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        # for ch in word:
        #     if not node:
        #         return False
        #     node = node.children[self.indexOfChar(ch)]
        # return node is not None and node.hit

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node is not None and node.hit



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        # for ch in prefix:
        #     if not node:
        #         return False
        #     node = node.children[self.indexOfChar(ch)]
        # return node is not None

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node is not None

    def indexOfChar(self, ch):
        return ord(ch) - 97

# Your Trie object will be instantiated and called as such:
trie = Trie()
print(trie.search("a"))
trie.insert("somestring")
print(trie.search("key"))
print(trie.startsWith("some"))
print(trie.search("some"))
print(trie.search("somestring"))
