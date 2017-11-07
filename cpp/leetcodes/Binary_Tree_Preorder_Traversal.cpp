/*
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode*> q;
        TreeNode* node = root;
        vector<int> res;
        while (node || !q.empty()){
            while (node) {
                res.push_back(node->val);
                q.push(node);
                node = node->left;
            }
            if (!q.empty()){
                node = q.top();
                q.pop();
                node = node->right;
            }
        }
        return res;
    }

};
int main(){
    Solution s;
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(2);
    root->left->right = new TreeNode(1);
    root->right = new TreeNode(4);
    vector<int> p = s.preorderTraversal(root);
    for_each(begin(p), end(p), [](int x){cout << x << ", ";});
    cout << endl;

}