/*
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

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
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr){
            return nullptr;
        }

        auto slow = head;
        auto fast = head->next;

        int k1 = 1;
        int k2 = 2;
        while (slow && fast && fast->next){
            if (slow == fast){
                break;
            }
            slow = slow->next;
            fast = fast->next->next;
            k1++;
            k2 += 2;
        }
        if(!slow || !fast || !fast->next){
            return nullptr;
        }

        int k = k2-k1;
        for (int i = 1; i <= k; i++){
            if (k % i == 0){
                auto h1 = head;
                for (int j=0; j<i; j++){
                    h1 = h1->next;
                }
                auto h2 = head;
                for (int l = 0; l < k1; ++l) {
                    if (h1 == h2){
                        return h1;
                    }
                    h1 = h1->next;
                    h2 = h2->next;
                }

            }
        }
        return nullptr;
    }

};


void test(ListNode* head){
    Solution s;
    ListNode* c = s.detectCycle(head);
    if (c){
        cout << c->val << endl;
    }else{
        cout << "NULL" << endl;
    }
}

int main(){

    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = head->next;
    test(head);

    head = new ListNode(5);
    test(head);

    head = new ListNode(5);
    head->next = head;
    test(head);

}