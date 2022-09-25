/*
    Time complexity : O(n)
    Space complexity: O(1)
*/

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

#include<iostream>
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
    ListNode* rotateRight(ListNode* head, int k) {
        int size, ct;
        size = ct = 0;
        if(!head)
            return head;
        
        // Step 1: Compute length of list
        ListNode* temp = head;
        ListNode* tail, *old, *new_head;
        while(temp!=NULL){
            tail = temp;
            temp = temp->next;
            size++;
        }
        
        k = k % size;
        if(k==0)
            return head;
        
        // Step 2: Locate new head
        new_head = head;
        while(ct < size - k){
            old = new_head;
            new_head = new_head->next;
            ct++;
        }
        
        // Step 3: Disconnect list before new head
        old->next = NULL;
        
        // Step 4: Connect tail node to old head
        tail->next = head;
        
        return new_head;  
    }
};