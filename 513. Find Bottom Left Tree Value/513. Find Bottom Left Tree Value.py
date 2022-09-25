'''
Time complexity : O(n)
Space complexity: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def findBottomLeftValue(self, root):
        q = collections.deque([(root)])
        bottomLeftNode = 0
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i==0:
                    bottomLeftNode = node.val
                if node.left: q += (node.left),
                if node.right: q += (node.right),

        return bottomLeftNode