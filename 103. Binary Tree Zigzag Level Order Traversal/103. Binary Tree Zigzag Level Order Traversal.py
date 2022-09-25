import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        q = collections.deque([root])
        order = 0
        while q:
            size = len(q)
            temp = []
            for _ in range(size):
                node = q.popleft()
                temp += node.val,
                if node.left:
                    q += node.left,
                if node.right:
                    q += node.right,
                
            if order & 1:
                temp = temp[::-1]
            order = 1 - order
            res += temp,
        
        return res