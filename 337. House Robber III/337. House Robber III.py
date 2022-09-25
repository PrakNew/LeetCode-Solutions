# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        
        def rob(root):
            if not root:
                return 0
            
            if root in dp:
                return dp[root]

            val = 0

            if root.left: # left grandchildren
                val += rob(root.left.left) + rob(root.left.right)

            if root.right: # right grandchildren
                val += rob(root.right.left) + rob(root.right.right)

            dp[root] = max(val + root.val, rob(root.left) + rob(root.right))
            
            return dp[root]
        
        dp = {}
        return rob(root)
            
            
        