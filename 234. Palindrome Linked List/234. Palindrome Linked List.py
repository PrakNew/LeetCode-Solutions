# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        
        def reverse(head):
            if not head:
                return head
            
            temp = head
            prev = None
            while temp:
                next_node = temp.next
                temp.next = prev
                prev = temp
                temp = next_node
                
            return prev
            
        n = 0
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = reverse(slow)
        
        while mid and head:
            if mid.val != head.val:
                return False
            mid = mid.next
            head = head.next
        
        return True