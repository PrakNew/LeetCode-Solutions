"""
Idea: Iteratively find a value which is greater than root but less than answer. 

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
    def findSecondMinimumValue(self, root):
        
        res = float('inf')
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            
            if root.val < node.val <= res:
                res = node.val
            
            if node.left:
                q += node.left,
            
            if node.right:
                q += node.right,
        
        return res if res < float('inf') else -1