'''
Time complexity : O(n)
Space complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head, val):
        if not head:
            return head
        
        prev = head
        temp = head.next
        
        while temp:
            while temp and temp.val==val:
                temp = temp.next
            prev.next = temp
            
            prev = prev.next if prev else None
            temp = temp.next if temp else None
            
        
        while head and head.val == val:
            head = head.next
        
        return head
            
        