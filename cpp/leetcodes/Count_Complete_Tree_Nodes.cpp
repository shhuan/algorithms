/*
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
 is completely filled, and all nodes in the last level are as far left as possible.
 It can have between 1 and 2h nodes inclusive at the last level h.
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
    int countNodes(TreeNode* root) {
        int height = heightOfTree(root);
        if (height <= 1){
            return height;
        }

        TreeNode* node = root;
        int ht = height;
        int count = pow(2, height-1)-1;
        TreeNode* parent = nullptr;
        while (node){
            if (rightHeightOfTree(node) == ht){
                count += pow(2, ht-1);
                break;
            }
            parent = node;
            node = node->left;
            ht--;
        }
        int h = 0;
        if (parent && parent->right){
            node = parent->right;
            while (node->left){
                node = node->left;
                h++;
            }
            if (h == ht-1){
                count++;
            }
        }

        return count;
    }

    int rightHeightOfTree(TreeNode* root){
        if(!root){
            return 0;
        }
        TreeNode* node = root;
        int h = 0;
        while (node){
            node = node->right;
            h++;
        }
        return h;
    }

    int heightOfTree(TreeNode* root){
        if(!root){
            return 0;
        }
        int h = 0;
        TreeNode* node = root;
        while (node){
            h++;
            node = node->left;
        }
        return h;
    }
};

int main(){
    Solution s;
    TreeNode* root = new TreeNode(1);
    cout << s.countNodes(root) << endl;

    root->left = new TreeNode(2);
    cout << s.countNodes(root) << endl;

    root->right = new TreeNode(3);
    cout << s.countNodes(root) << endl;

    root->left->left = new TreeNode(4);
    cout << s.countNodes(root) << endl;

    root->left->right = new TreeNode(5);
    cout << s.countNodes(root) << endl;

    root->right->left = new TreeNode(6);
    cout << s.countNodes(root) << endl;

    root->right->right = new TreeNode(7);
    cout << s.countNodes(root) << endl;

    root->left->left->left = new TreeNode(8);
    cout << s.countNodes(root) << endl;

    root = new TreeNode(1);
    queue<TreeNode*> q;
    q.push(root);
    int val = 2;
    while (val < 1000){
        queue<TreeNode*> nextLevel;
        while (!q.empty()){
            TreeNode* node = q.front();
            q.pop();
            node->left = new TreeNode(val++);
            cout << s.countNodes(root) << endl;

            node->right = new TreeNode(val++);
            cout << s.countNodes(root) << endl;

            nextLevel.push(node->left);
            nextLevel.push(node->right);
        }
        q = nextLevel;
    }

}