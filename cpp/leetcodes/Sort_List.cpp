/*
 *Sort a linked list in O(n log n) time using constant space complexity.

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
    ListNode* sortList(ListNode* head) {
        if (head == nullptr){
            return nullptr;
        }
        if (head->next == nullptr){
            return head;
        }
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (slow && fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* h2 = slow->next;
        slow->next = nullptr;
        auto h1 = sortList(head);
        h2 = sortList(h2);
        return mergeList(h1, h2);
    }
    ListNode* mergeList(ListNode* h1, ListNode* h2) {
        if (h1 == nullptr){
            return h2;
        }else if (h2 == nullptr) {
            return h1;
        }
        ListNode* res = new ListNode(0);
        ListNode* node = res;
        while (h1 && h2){
            if (h1->val < h2->val){
                node->next = h1;
                h1 = h1->next;
            }else{
                node->next = h2;
                h2 = h2->next;
            }
            node = node->next;
        }
        if (h1 != nullptr){
            node->next = h1;
        }else{
            node->next = h2;
        }
        return res->next;
    }

    void outputList(ListNode* head){
        ListNode* node = head;
        while (node != nullptr){
            cout << node->val << ", ";
            node = node->next;
        }
        cout << endl;
    }
};

int main(){
    Solution s;
    ListNode* h1 = new ListNode(1);
    h1->next = new ListNode(3);
    h1->next->next = new ListNode(5);
    ListNode* h2 = new ListNode(2);
    h2->next = new ListNode(3);
    h2->next->next = new ListNode(4);
    s.outputList(s.mergeList(h1, h2));


    h1 = new ListNode(3);
    h1->next = new ListNode(2);
    h1->next->next = new ListNode(4);
    s.outputList(s.sortList(h1));

    h1 = new ListNode(2);
    s.outputList(s.sortList(h1));


}