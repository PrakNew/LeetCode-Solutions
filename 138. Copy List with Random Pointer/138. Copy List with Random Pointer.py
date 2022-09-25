import collections 

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        
        deep_copy = collections.defaultdict(lambda : Node(0))
        temp = head
        deep_copy[None] = None
        
        while temp:
            deep_copy[temp].val = temp.val
            deep_copy[temp].next = deep_copy[temp.next]
            deep_copy[temp].random = deep_copy[temp.random]
            temp = temp.next
            
        return deep_copy[head]