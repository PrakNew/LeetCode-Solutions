# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        q = [(root, root.val)]
        ans = 0
        
        while q:
            node, max_so_far = q.pop(0)
            
            if max_so_far <= node.val:
                ans += 1
            
            if node.left:
                q.append((node.left, max(max_so_far, node.left.val)))
            if node.right:
                q.append((node.right, max(max_so_far, node.right.val)))
        
        return ans