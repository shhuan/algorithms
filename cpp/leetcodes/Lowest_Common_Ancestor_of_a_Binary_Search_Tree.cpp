#include <iostream>

using namespace std;



struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr || p == nullptr || q == nullptr){
            return nullptr;
        }
        if (p->val > q->val){
            return lowestCommonAncestor(root, q, p);
        }
        if(root->val >= p->val && root->val <= q->val){
            return root;
        }else if(root->val >= p->val && root->val >= q->val){
            return lowestCommonAncestor(root->left, p, q);
        }else{
            return lowestCommonAncestor(root->right, p, q);
        }

    }

    TreeNode* lowestCommonAncestor2(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr || p == nullptr || q == nullptr){
            return nullptr;
        }
        int minVal = min(p->val, q->val);
        int maxVal = max(p->val, q->val);
        TreeNode* node = root;
        while (node != nullptr){
            if(node->val < minVal) {
                node = node->right;
            } else if(node->val > maxVal){
                node = node->left;
            } else{
                return node;
            }
        }
        return nullptr;
    }
};



int main() {
    cout << "Hello, World!" << endl;
    return 0;
}