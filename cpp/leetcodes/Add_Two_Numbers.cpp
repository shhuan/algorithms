//
// Created by huash06 on 2015/7/12.
//

/*
 * You are given two linked lists representing two non-negative numbers.
 * The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 *
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 *
 * Output: 7 -> 0 -> 8
 */

#include <iostream>
#include <vector>
#include <bits/stl_algo.h>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1 == nullptr || l2 == nullptr){
            return nullptr;
        }
        auto head = new ListNode(0);
        auto h = head;
        int car = 0;
        while (l1 != nullptr && l2 != nullptr){
            int v = l1->val+l2->val+car;
            h->next = new ListNode(v%10);
            car = v/10;
            h = h->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while (l1 != nullptr){
            int v = l1->val+car;
            h->next = new ListNode(v%10);
            car = v/10;
            h = h->next;
            l1 = l1->next;
        }

        while (l2 != nullptr){
            int v = l2->val+car;
            h->next = new ListNode(v%10);
            car = v/10;
            h = h->next;
            l2 = l2->next;
        }
        if(car > 0){
            h->next = new ListNode(car);
        }
        return head->next;
    }

    void outputList(ListNode* h){
        if(h == nullptr){
            cout << endl;
            return;
        }
        cout << h->val << ", ";
        outputList(h->next);

    }
    ListNode* toList(vector<int> vals){
        if(vals.empty()){
            return nullptr;
        }
        auto head = new ListNode(0);
        auto h = head;
        for_each(begin(vals), end(vals), [&h](int v){
            h->next = new ListNode(v);
            h = h->next;
        });
        return head->next;
    }
};

int main(){
    Solution s;
//    int a[3]{1, 2, 3};
    vector<int> a{2, 4, 3};
    vector<int> b{5, 6, 9};
    ListNode* res = s.addTwoNumbers(s.toList(a), s.toList(b));
    s.outputList(res);

    return 0;
}