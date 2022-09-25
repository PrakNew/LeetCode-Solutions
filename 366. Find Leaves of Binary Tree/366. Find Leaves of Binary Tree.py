# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root):
        
        def dfs(node, path):
            if not node.left and not node.right:
                path.append(node.val)
                return None
            else:
                if node.left:
                    node.left = dfs(node.left, path)
                if node.right:
                    node.right = dfs(node.right, path)
            return node 
        
        res = []
        while root:
            path = []
            root = dfs(root, path)        
            res.append(path)
        
        return res
        
        