import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        q = collections.deque([(root, 1)])
        res = []
        while q:
            size = len(q)
            max_index = -1
            right_most = None
            for _ in range(size):
                node, index = q.popleft()
                if index > max_index:
                    max_index = index
                    right_most = node.val
                if node.left:
                    q.append((node.left, index*2))
                if node.right:
                    q.append((node.right, index*2+1))
            res.append(right_most)
        
        return res
        