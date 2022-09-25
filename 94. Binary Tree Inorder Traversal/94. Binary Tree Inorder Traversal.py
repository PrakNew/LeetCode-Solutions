# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        
        # Inorder: Left -> Node -> Right
        stack = []
        inorder = []
        
        while root or stack:
            
            while root:
                stack += root,
                root = root.left
            
            root = stack.pop()
            inorder += root.val,
            root = root.right
        
        return inorder
            
        