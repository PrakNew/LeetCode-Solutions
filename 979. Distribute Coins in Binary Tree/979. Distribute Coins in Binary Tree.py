# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            
            L = dfs(node.left)
            R = dfs(node.right)
            
            self.ans += abs(L) + abs(R)
            
            return node.val + L + R - 1
    
        dfs(root)
        
        return self.ans