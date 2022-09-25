'''
Idea: Perform tree traversal and compare every node value with target value 

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
    def closestValue(self, root, target):
        q = collections.deque([root])
        diff = float('inf')
        res = None
        while q:
            node = q.popleft()
            if abs(node.val - target) < diff:
                diff = abs(node.val - target)
                res = node.val
            if node.left:
                q.append((node.left))
            if node.right:
                q.append((node.right))
        return res