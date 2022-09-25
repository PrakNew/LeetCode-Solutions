# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root, p):
        stack = []
        flag = False
        while stack or root:
            while root:
                stack += root,
                root = root.left 
            root = stack.pop()
            if flag:
                return root
            if root.val == p.val:
                flag = True
            root = root.right 
        