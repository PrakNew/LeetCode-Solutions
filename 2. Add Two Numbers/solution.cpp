/*
Time complexity : O(n)
Space complexity: O(n)
*/

#include<vector>
#include<string>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0, x, y, sum;
        ListNode* head = new ListNode(-1);
        ListNode* temp = head;
        while(l1 || l2){
            x = l1 ? l1->val : 0;
            y = l2 ? l2->val : 0;
            sum = x + y + carry;
            carry = sum / 10;
            temp->next = new ListNode(sum % 10);
            if(l1)
                l1 = l1->next;
            if(l2)
                l2 = l2->next;
            temp = temp->next;
        }
        if(carry)
            temp->next = new ListNode(carry);
        return head->next;      
    }
};