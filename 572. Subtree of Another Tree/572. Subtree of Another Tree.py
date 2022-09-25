# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s, t):
        
        def equal(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            
            return t.val==s.val and equal(s.left, t.left) and equal(s.right, t.right)
        
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        if equal(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)