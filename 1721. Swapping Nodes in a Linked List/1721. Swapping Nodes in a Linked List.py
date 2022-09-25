"""
Idea: Go to respective nodes and swap their values

Time complexity : O(n)
Space complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k):
        if not head:
            return head
        
        n = 0
        temp = head
        
        while temp:
            temp = temp.next
            n += 1
        
        temp1 = head
        ct = 1
        while ct < k:
            temp1 = temp1.next
            ct += 1
        
        temp2 = head
        ct = 1
        while ct <= n - k:
            temp2 = temp2.next
            ct += 1
        
        temp1.val, temp2.val = temp2.val, temp1.val
        
        return head
        
        
        
        
        