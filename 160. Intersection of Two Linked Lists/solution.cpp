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
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* l1 = headA;
        ListNode* l2 = headB;
        int n1 = 0, n2 = 0;
        
        while(l1){
            n1++;
            l1 = l1->next;
        }
        
        while(l2){
            n2++;
            l2 = l2->next;
        }
        
        l1 = headA;
        l2 = headB;
        
        while(n1 != n2){
            if(n1 > n2){
                n1--;
                l1 = l1->next;
            }
            else{
                n2--;
                l2 = l2->next;
            }
        }
        
        while(l1 and l2 and l1 != l2){
            l1 = l1->next;
            l2 = l2->next;
            n1--; n2--;
        }
        
        return l1 ? l1 : NULL;
    }
};