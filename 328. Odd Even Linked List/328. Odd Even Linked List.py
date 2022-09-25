# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        
        if not head:
            return None
        
        one = head
        two = None
        even_head = None
        
        if head.next:
            two = head.next
            even_head = head.next
        else:
            return head
        
        ct = 0
        
        while two.next is not None:
            one.next = two.next
            one, two = two, one.next
            ct+=1
        
        if ct%2==0:  # one is odd pointer, two is even pointer
            one.next = even_head
        
        else:   # one is even pointer, two is odd pointer
            one.next = two.next
            two.next = even_head
        
        return head
        
        
        