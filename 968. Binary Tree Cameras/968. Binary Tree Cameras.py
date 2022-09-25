"""
Idea: Recursion greedy.

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
    def minCameraCover(self, root):
        
        # state 0: leaf node not covered
        # state 1: parent of leaf node with camera
        # state 2: already covered
        
        self.res = 0
        
        def dfs(root):
            if not root:
                return 2
            
            l, r = dfs(root.left), dfs(root.right)
            
            if l == 0 or r == 0:
                self.res += 1
                return 1
            
            return 2 if l == 1 or r == 1 else 0
        
        return (dfs(root) == 0) + self.res 
    

