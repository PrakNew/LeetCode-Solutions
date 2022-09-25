# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        
        def merge(l1, l2):
            head = ListNode()
            temp = head
            
            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    temp.next = ListNode(l2.val)
                    l2 = l2.next
                temp = temp.next

            while l1:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            
            while l2:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
                
            return head.next
        
        
        while len(lists)>1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(merge(l1, l2))
        
        if len(lists)==1:
            return lists[0]
        
        return None