"""
Idea: Start from root with unbounded limits. Perform BFS and keep updating the limits of node at each level

Time complexity : O(n)
Space complexity: O(n)
"""


import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        
        q = collections.deque([(float('-inf'), root, float('inf'))])
        
        while q:
            low, node, high = q.popleft()
            
            if not low < node.val < high:
                return False
            
            if node.left:
                q += (low, node.left, node.val),
            
            if node.right:
                q += (node.val, node.right, high),
            
        
        return True