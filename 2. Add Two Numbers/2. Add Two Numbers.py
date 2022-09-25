# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode()
        curr = head
        
        while l1 or l2 or carry>0:
            if l1:
                carry += l1.val
            if l2:
                carry += l2.val
                
            digit = carry % 10
            carry = carry // 10
            
            if l2:
                l2 = l2.next
            
            if l1:
                l1 = l1.next
            
            curr.next = ListNode(digit)
            curr = curr.next
        
        return head.next