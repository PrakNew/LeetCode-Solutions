/*
Time complexity : O(n^2)
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
    ListNode* insertionSortList(ListNode* head) {
        ListNode* newHead = new ListNode(INT_MIN);
        
        ListNode* input = head;
        ListNode* nextNode = NULL;
        ListNode* prev = NULL;
        ListNode* temp = NULL;
        
        while(input){
            nextNode = input->next;
            prev = NULL;
            temp = newHead;
            while(temp and temp->val <= input->val){
                prev = temp;
                temp = temp->next;
            }
            
            input->next = prev->next;
            prev->next = input;
            
            input = nextNode;
        }
        
        head = newHead->next;
        
        delete input, nextNode, prev, temp, newHead;
        
        return head;
    }
};