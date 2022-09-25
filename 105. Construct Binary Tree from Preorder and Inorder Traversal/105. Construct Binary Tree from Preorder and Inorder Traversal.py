import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index = {val:ind for ind, val in enumerate(inorder)}
        preorder = collections.deque(preorder)
        
        def recur(left, right):
            if left > right:
                return None
            root = TreeNode(preorder.popleft())
            root_index = inorder_index[root.val]
            root.left = recur(left, root_index-1)
            root.right = recur(root_index+1, right)
            return root
        
        return recur(0, len(inorder)-1)
        