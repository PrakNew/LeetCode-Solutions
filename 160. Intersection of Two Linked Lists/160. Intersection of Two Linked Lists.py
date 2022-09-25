# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        sizeA, sizeB = 0, 0
        
        temp = headA
        while temp:
            temp = temp.next
            sizeA+=1
        
        temp = headB
        while temp:
            temp = temp.next
            sizeB+=1
            
        temp1, temp2 = headA, headB
        
        while sizeA!=sizeB:
            if sizeA>sizeB:
                temp1 = temp1.next
                sizeA-=1
            else:
                temp2 = temp2.next
                sizeB-=1
        
        
        while temp1 and temp2 and temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next
        
        return temp1
                
            
        