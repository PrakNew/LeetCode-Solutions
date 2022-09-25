# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        
        if not head:
            return None
        
        temp = head
        prev = None
        
        while temp.next:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        
        temp.next = prev
        
        return temp