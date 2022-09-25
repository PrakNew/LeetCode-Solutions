# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        q = collections.deque()
        q += root,
        
        while q:
            node = q.pop()
            if node.val == val:
                return node
            if node.left:
                q += node.left,
            if node.right:
                q += node.right,
        
        return None