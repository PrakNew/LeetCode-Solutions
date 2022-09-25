"""
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
    def maxDepth(self, root):
        if not root:
            return 0
        
        q = collections.deque([(root, 1)])
        res = 0
        
        while q:
            node, depth = q.popleft()
            res = max(res, depth)
            if node.left:
                q += (node.left, depth + 1),
            if node.right:
                q += (node.right, depth + 1),
        
        return res