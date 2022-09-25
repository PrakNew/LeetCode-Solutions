'''
Time complexity : O(n)
Space complexity: O(n)
'''

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root):
        if not root:
            return 0
        q = collections.deque([(root, 1)])
        res = 0
        while q:
            node, length = q.popleft()
            res = max(res, length)
            if node.left:
                if node.val + 1 == node.left.val:
                    q.append((node.left, length+1))
                else:
                    q.append((node.left, 1))
            if node.right:
                if node.val + 1 == node.right.val:
                    q.append((node.right, length+1))
                else:
                    q.append((node.right, 1))
        return res