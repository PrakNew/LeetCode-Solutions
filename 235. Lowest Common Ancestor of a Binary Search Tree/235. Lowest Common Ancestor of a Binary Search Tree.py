"""
Time complexity : O(n)
Space complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if p.val <= node.val <= q.val:
                return node
            
            if q.val < node.val:
                queue += node.left,
            
            if p.val > node.val:
                queue += node.right,
        
        return -1