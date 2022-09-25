class Solution:
    def reverseKGroup(self, head, k):
        ct = 0
        temp = head

        while temp: # check if there are atleast k nodes
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
                ct += 1
            # prev becomes head 
            # head becomes tail 
            if next_node:
                head.next = self.reverseKGroup(next_node, k)
            return prev
            
        else:
            return head