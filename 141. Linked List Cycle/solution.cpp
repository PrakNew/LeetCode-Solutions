/*
Idea: Hare tortoise algorithm

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
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(!head or !head->next)
            return true;
        
        ListNode* firstHalfEnd = getFirstHalfEnd(head);
        ListNode* secondHalfStart = reverseList(firstHalfEnd->next);
        
        ListNode* l1 = head;
        ListNode* l2 = secondHalfStart;
        
        bool isPalindrome = true;
        while(l2 and isPalindrome){
            if(l1->val != l2->val)
                return false;
            l1 = l1->next;
            l2 = l2->next;
        }
        return true;
    }

private:
    
    ListNode* getFirstHalfEnd(ListNode* head){
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast and fast->next and fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
    
    ListNode* reverseList(ListNode* head){
        ListNode* temp = head;
        ListNode* prev = NULL;
        while(temp){
            ListNode* next = temp->next;
            temp->next = prev;
            prev = temp;
            temp = next;
        }
        return prev;
    }
    
};