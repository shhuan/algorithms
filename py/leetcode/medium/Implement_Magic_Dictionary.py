# -*- coding: utf-8 -*-
"""


Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

"""


class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """

        for i, word in enumerate(dict):
            t = self.trie
            for j, v in enumerate(word):
                if v not in t:
                    t[v] = {'#': False}
                t = t[v]
            t['#'] = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        chs = [chr(i) for i in range(ord('a'), ord('a') + 26)]
        for i in range(len(word)):
            for ch in chs:
                if ch != word[i]:
                    # print("searching " + word[:i] + ch + word[i+1:])
                    if self.search_impl(word[:i] + ch + word[i + 1:], self.trie):
                        return True

        return False

    def search_impl(self, word, trie):
        t = trie
        for i, v in enumerate(word):
            if v not in t:
                return False
            t = t[v]

        return t['#']


        # Your MagicDictionary object will be instantiated and called as such:
        # obj = MagicDictionary()
        # obj.buildDict(dict)
        # param_2 = obj.search(word)

d = MagicDictionary()
d.buildDict(["hello", "hallo", "leetcode"])
print(d.search("hello"))
print(d.search("hello"))
print(d.search("hell"))
print(d.search("leetcodd"))