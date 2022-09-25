# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root):
        
        if not root:
            return 0
        
        q = collections.deque([(root, None, None)])
        res = 0
        
        while q:
            node, maxval, minval = q.popleft()
            
            if maxval is not None:
                res = max(res, abs(maxval - node.val))
            if minval is not None:
                res = max(res, abs(minval - node.val))
            
            if maxval!=None:
                maxval = max(maxval, node.val)
            else:
                maxval = node.val
            
            if minval!=None:
                minval = min(minval, node.val)
            else:
                minval = node.val
            
            if node.left:
                q.append((node.left, maxval, minval))
            
            if node.right:
                q.append((node.right, maxval, minval))

            
        return res
        