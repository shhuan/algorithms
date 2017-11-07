/*
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ? k ? BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
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
    int kthSmallest(TreeNode* root, int k) {
        //pre-order travel
        stack<TreeNode*> q;
        TreeNode* node = root;
        while (node != nullptr){
            q.push(node);
            node = node->left;
        }
        while (!q.empty()){
            node = q.top();
            k--;
            if (k == 0){
                return node->val;
            }
            q.pop();
            if(node->right != nullptr){
                node = node->right;
                while (node != nullptr){
                    q.push(node);
                    node = node->left;
                }
            }
        }
        return -1;
    }
};

int main(){
    TreeNode* root = new TreeNode(6);
    root->left = new TreeNode(4);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(5);
    root->right = new TreeNode(8);
    root->right->left = new TreeNode(7);
    root->right->right = new TreeNode(9);
    Solution s;
    for(int i=1; i <= 7; i++){
        cout << s.kthSmallest(root, i) << endl;
    }
}