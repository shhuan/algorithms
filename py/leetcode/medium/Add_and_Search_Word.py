# -*- coding: utf-8 -*-
"""
created by huash at 2015/9/4 10:34

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A .
means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.

"""
__author__ = 'huash'

import sys
import os
import datetime
import functools
import itertools
import collections

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hit = False
        self.children = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.hit = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        if len(word) == 1:
            return (word == '.' and len(filter(lambda x: x.hit, self.children.values())) > 0) or \
                   (word in self.children and self.children[word].hit)
        if word[0] == '.':
            for node in self.children.values():
                if node.search(word[1:]):
                    return True
            return False
        else:
            if word[0] not in self.children:
                return False
            return self.children[word[0]].search(word[1:])

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
print(wordDictionary.search("a"))
print(wordDictionary.search(".at"))
wordDictionary.addWord("bat")

print(wordDictionary.search(".at"))
print(wordDictionary.search("an."))
print(wordDictionary.search("a.d."))
print(wordDictionary.search("b."))
print(wordDictionary.search("a.d"))
print(wordDictionary.search("."))

print("[false,false,true,true,false,false,true,false]")