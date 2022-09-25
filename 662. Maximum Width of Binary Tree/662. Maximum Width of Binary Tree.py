import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        max_width = 1
        q = collections.deque([(root, 0)])
        
        while q:
            level = len(q)
            min_val = 2**31 + 10
            max_val = -(2**31 + 10)
            for _ in range(level):
                node, val = q.popleft()
                if val < min_val:
                    min_val = val
                if val > max_val:
                    max_val = val
                if node.left:
                    q.append((node.left, val*2+1))
                if node.right:
                    q.append((node.right, val*2+2))
            if min_val < 2**31 + 10 and max_val > -(2**31 + 10):
                max_width = max(max_width, max_val - min_val + 1)
        
        return max_width
        
        