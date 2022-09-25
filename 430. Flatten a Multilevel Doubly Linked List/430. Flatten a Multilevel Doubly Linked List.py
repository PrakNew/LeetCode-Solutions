"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:        
    def flatten(self, head):
        if not head:
            return head
    
        temp = head
        stack = [temp]
        q = []
        while stack:
            node = stack.pop()
            q.append(node)
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)

        new_head = Node(q[0].val)
        temp = new_head
        n = len(q)
        for i in range(1, n):
            next_node = Node(q[i].val)
            next_node.prev = temp
            temp.next = next_node
            temp = temp.next
        return new_head