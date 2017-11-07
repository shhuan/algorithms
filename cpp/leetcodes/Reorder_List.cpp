/*
 *
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

 */


#include <iostream>
#include <vector>
#include <bits/stl_algo.h>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <regex>


using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr){
            return;
        }
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (slow && fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* h2 = slow->next;
        slow->next = nullptr;

        // reverse the second half and merge
        h2 = reverse(h2);
        ListNode* h1 = head;
        while (h1 && h2){
            ListNode* t1 = h1->next;
            ListNode* t2 = h2->next;
            h1->next = h2;
            h2->next = t1;
            h1 = t1;
            h2 = t2;
        }
    }

    ListNode* reverse(ListNode* head){
        if (head == nullptr || head->next == nullptr){
            return head;
        }
        ListNode* h = head;
        ListNode* hn = head->next;
        h->next = nullptr;
        while (h && hn){
            ListNode* t = hn->next;
            hn->next = h;
            h = hn;
            hn = t;
        }
        return h;
    }

    void outputList(ListNode* head){
        ListNode* node = head;
        while (node){
            cout << node->val << " ";
            node = node->next;
        }
        cout << endl;
    }

    ListNode* toList(vector<int>& nums){
        ListNode* head = new ListNode(0);
        ListNode* h = head;
        for (int v : nums){
            h->next = new ListNode(v);
            h = h->next;
        }
        return head->next;
    }
};

int main(){
    Solution s;
    auto nums = vector<int>{1, 2, 3, 4, 5, 6, 7};
    ListNode* head = s.toList(nums);
    s.reorderList(head);
    s.outputList(head);

    nums = vector<int>{1, 2, 3, 4, 5, 6, 7, 8};
    head = s.toList(nums);
    s.reorderList(head);
    s.outputList(head);
}