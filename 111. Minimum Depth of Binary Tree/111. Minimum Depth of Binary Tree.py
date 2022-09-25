"""
Idea: BFS search and check for first leaf node.

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
    def minDepth(self, root):
        
        if not root:
            return 0
        
        q = collections.deque([(root, 1)])
        
        while q:
            node, path = q.popleft()
            
            if not node.left and not node.right:
                return path
            
            if node.left:
                q += (node.left, path + 1),
            
            if node.right:
                q += (node.right, path + 1),
        
        return -1
        