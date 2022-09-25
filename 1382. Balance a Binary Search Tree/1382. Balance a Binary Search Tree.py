'''
Idea: From the inorder rebuild a balanced BST.

Time complexity : O(n)
Space complexity: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root):
        
        def inorder(root):
            stack = list()
            result = list()
            while stack or root:
                while root:
                    stack += root,
                    root = root.left
                root = stack.pop()
                result += root,
                root = root.right
            return result
        
        def build(stack):
            if stack:
                mid = len(stack) >> 1
                mid_node = stack[mid]
                mid_node.left = build(stack[:mid])
                mid_node.right = build(stack[mid+1:])
                return mid_node
        
        return build(inorder(root))