# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, m, n):
        ct = 1
        temp = head
        old_chain = None
        
        while temp and ct<m:
            old_chain = temp
            temp = temp.next
            ct+=1
        
        new_tail = temp
        curr = temp
        next_node = None
        prev = None
        
        while curr and ct<=n:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            ct+=1
        
        
        if old_chain:
            old_chain.next = prev
        else:
            head = prev
            
        if new_tail:
            new_tail.next = curr
        
        return head
        
        