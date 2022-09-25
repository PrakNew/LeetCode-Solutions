"""
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
    def levelOrder(self, root):
        if not root:
            return []
        
        q = [root]
        level_order = []
        
        while q:       
            size = len(q)
            level = []            
            for _ in range(size):
                node = q.pop(0)
                level += node.val,
                if node.left:
                    q += node.left,
                if node.right:
                    q += node.right,
            level_order += level,
        
        return level_order