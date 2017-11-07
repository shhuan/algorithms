/*
 * Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>

using namespace std;

class TrieNode {
public:
    // Initialize your data structure here.
    TrieNode() {
        hit = false;
        children.resize(26);
        fill(begin(children), end(children), nullptr);
    }

    bool hit;
    vector<TrieNode *> children;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) {
        TrieNode *node = root;
        for (char ch : word) {
            int idx = char2Int(ch);
            if (node->children[idx] == nullptr) {
                node->children[idx] = new TrieNode();
            }
            node = node->children[idx];
        }
        node->hit = true;
    }

    // Returns if the word is in the trie.
    bool search(string word) {
        TrieNode *node = root;
        for (char ch : word) {
            if (node == nullptr) {
                return false;
            }
            node = node->children[char2Int(ch)];
        }
        return node != nullptr && node->hit;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        TrieNode *node = root;
        for (char ch : prefix) {
            if (node == nullptr) {
                return false;
            }
            node = node->children[char2Int(ch)];
        }
        return node != nullptr;
    }

    int char2Int(char ch) {
        return int(ch - 'a');
    }

private:
    TrieNode *root;
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");

void test(vector<pair<int, string> > ops) {
    cout << "==============test started==============" << endl;
    Trie trie;
    for (auto op : ops) {
        int type = op.first;
        string word = op.second;
        switch (type) {
            case 0:
                cout << "inserting " << word << endl;
                trie.insert(word);
                break;
            case 1:
                cout << "searching " << word << ": " << trie.search(word) << endl;
                break;
            case 2:
                cout << "is prefix " << word << ": " << trie.startsWith(word) << endl;
                break;
        }
    }
    cout << "==============test finished==============" << endl << endl;
}

int main() {
    test(vector<pair<int, string> > {
            make_pair(0, "somethig"),
            make_pair(0, "some"),
            make_pair(1, "somethig"),
            make_pair(1, "k"),
            make_pair(1, "key"),
            make_pair(1, "s"),
            make_pair(1, "some"),
            make_pair(1, "str"),
            make_pair(2, "k"),
            make_pair(2, "some"),
            make_pair(2, "str"),
    });

    test(vector<pair<int, string> > {
            make_pair(0, "ab"),
            make_pair(1, "a"),
            make_pair(2, "a")
    });
}