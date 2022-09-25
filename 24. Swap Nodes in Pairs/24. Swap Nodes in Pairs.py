# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        
        def reverseKGroup(head, k):
            ct = 0
            temp = head
            while temp:
                temp = temp.next 
                ct += 1
                if ct==k:
                    break 
            if ct>=k:
                curr = head
                prev = None
                next_node = None
                ct = 0
                while curr and ct<k:
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node
                    ct+=1
                if next_node:
                    head.next = reverseKGroup(next_node, k)
                return prev
            else:
                return head
        
        return reverseKGroup(head, 2)
        