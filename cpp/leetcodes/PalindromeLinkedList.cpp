//
// Created by huash06 on 2015/7/12.
//


#include <iostream>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (head == nullptr){
            return true;
        }
        ListNode* mid = this->mid(head);
        ListNode* rev = this->reverse(mid);
        return this->equals(rev, head);
    }

    ListNode* mid(ListNode* head){
        ListNode* h = head;
        ListNode* mid = head;
        while(h != nullptr && h->next != nullptr){
            h = h->next->next;
            mid = mid->next;
        }
        if(h != nullptr){
            return mid->next;
        }
        return mid;
    }

    ListNode* reverse(ListNode* head){
        if(head == nullptr){
            return nullptr;
        }
        ListNode* h = head;
        ListNode* hn = h->next;
        head->next = nullptr;
        while(h != nullptr && hn != nullptr){
            ListNode* tmp = hn->next;
            hn->next = h;
            h = hn;
            hn = tmp;
        }
        return h;
    }

    bool equals(ListNode* h1, ListNode* h2){
        while(h1 != nullptr && h2 != nullptr){
            if(h1->val != h2->val){
                return false;
            }
            h1 = h1->next;
            h2 = h2->next;
        }
        return true;
    }

    ListNode* toList(int* vals, int size){
        if(vals == nullptr || size <= 0){
            return nullptr;
        }
        ListNode* head = new ListNode(vals[0]);
        ListNode* h = head;
        for (int i = 1; i < size; ++i) {
            h->next = new ListNode(vals[i]);
            h = h->next;
        }
        return head;
    }

    void outputList(ListNode* head){
        if (head == nullptr){
            cout<<endl;
            return;
        }
        cout << head->val <<" ";
        outputList(head->next);
    }
    void test(int vals[], int size){
        ListNode* head = toList(vals, size);
        outputList(head);
        cout << (isPalindrome(head)? "True":"False" )<<endl;
    }
};

int main() {
    Solution* s = new Solution();
    s->test(new int[5]{1, 2, 3, 2, 1}, 5);
    s->test(new int[2]{1, 1}, 2);
    s->test(new int[1]{3}, 1);

    return 0;
}