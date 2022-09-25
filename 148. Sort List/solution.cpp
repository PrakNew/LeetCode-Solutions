/*
Time complexity : O(n log n)
Space complexity: O(1)
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
    ListNode* sortList(ListNode* head) {
        return mergeSort(head);
    }
private:
    ListNode* mergeSort(ListNode* head){
        
        // Base case - 0 or 1 node
        if(!head || !head->next)
            return head;
        
        ListNode* middleNode = findMiddle(head);
        ListNode* middleNext = middleNode->next;
        
        // Break list into two halves
        middleNode->next = NULL;
        
        
        // Sort left and right halves
        ListNode* l1 = mergeSort(head);
        ListNode* l2 = mergeSort(middleNext);
        
        // Merge two sorted halves
        return merge(l1, l2);
    }
    
    ListNode* findMiddle(ListNode* head){
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast and fast->next and fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
    
    ListNode* merge(ListNode* l1, ListNode* l2){
        ListNode* newHead = new ListNode(INT_MIN);
        ListNode* temp = newHead;
        
        while(l1 and l2){
            if(l1->val < l2->val){
                temp->next = l1;
                l1 = l1->next;
            }
            else{
                temp->next = l2;
                l2 = l2->next;
            }
            temp = temp->next;
        }
        
        temp->next = (l1) ? l1 : l2;
        
        return newHead->next;
    }
};