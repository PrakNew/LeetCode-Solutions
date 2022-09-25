/*
Time complexity : O(n)
Space complexity: O(1)
*/

#include<vector>
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
    ListNode* oddEvenList(ListNode* head) {
        if(!head || !head->next)
            return head;
        
        ListNode* oddHead = head;
        ListNode* evenHead = head->next;
        ListNode* p1 = oddHead;
        ListNode* p2 = evenHead;
        int ct = 0;
        
        while(p2->next){
            ListNode* nextNode = p1->next;
            p1->next = p2->next;
            p2 = p1->next;
            p1 = nextNode;
            ct++;
        }
        
        if(ct & 1){      // p1 is even
            p1->next = NULL;
            p2->next = evenHead;
        }
        else{       // p1 is odd
            p1->next = evenHead;
            p2->next = NULL;
        }
        
        return oddHead;
    }
};