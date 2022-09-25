'''
Time complexity : O(n)
Space complexity : O(n)
'''

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        res = 0
        q = collections.deque([(root, 'M')])
        while q:
            node, kind = q.popleft()
            if not node.left and not node.right and kind=='L': # left leaf node
                res += node.val 
                continue
            if node.left:
                q.append((node.left, 'L'))
            if node.right:
                q.append((node.right, 'R'))
        
        return res