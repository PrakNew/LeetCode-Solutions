/*
Idea: Maintain two pointers, one pointer n nodes ahead of another.

Time complexity : O(n)
Space complexity: O(1)
*/

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* newHead = new ListNode(-1);
        newHead->next = head;
        ListNode* slow = newHead;
        ListNode* fast = newHead;
        
        for(int i = 0; i <= n; ++i)
            fast = fast->next;
        
        while(fast){
            slow = slow->next;
            fast = fast->next;
        }
        
        slow->next = slow->next->next;
        
        return newHead->next;
    }
};