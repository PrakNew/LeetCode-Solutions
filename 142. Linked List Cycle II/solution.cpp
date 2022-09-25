/*
Idea: Floyds algorithm - hare tortoise

Time complexity : O(n)
Space complexity: O(1)
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        
        while(1){
            if(slow and fast and fast->next){
                slow = slow->next;
                fast = fast->next->next;
            }
            else
                return NULL;
            
            if(slow == fast)
                break;
        }

        fast = head;
        
        while(slow and fast and slow != fast){
            slow = slow->next;
            fast = fast->next;
        }
        
        return slow;
    }
};