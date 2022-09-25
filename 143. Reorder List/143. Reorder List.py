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
    def reorderList(self, head):
        def splitList(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle
        
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        def mergeList(h1, h2):
            while h1 and h2:
                next_node = h1.next
                h1.next = h2
                h2 = h2.next
                h1.next.next = next_node
                h1 = next_node
            
        if not head:
            return head
        h1, h2 = splitList(head)
        h2 = reverseList(h2)
        t = h2
        mergeList(h1, h2)