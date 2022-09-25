"""
Idea: Inorder traversal of BST gives elements in ascending order.

Time complexity : O(n)
Space complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        node = root
        
        while node or stack:
            while node:
                stack += node,
                node = node.left
            
            node = stack.pop()
            k -= 1
            
            if k == 0:
                return node.val
            
            node = node.right
        
        return -1