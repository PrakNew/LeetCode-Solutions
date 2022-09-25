# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        # Floyds algorithm for detecting cycle
        
        # Phase 1: Find the interesection point
        hare, tortoise = head, head
        while True:
            if hare and hare.next and tortoise:
                hare = hare.next.next
                tortoise = tortoise.next
            else:
                return None
 
            if hare==tortoise:
                break
        
        # No cycle
        if hare!=tortoise:
            return None
        
        # Phase 2: Find the entrance of cycle
        tortoise = head
        while tortoise!=hare:
            tortoise = tortoise.next
            hare = hare.next
        
        return hare
        