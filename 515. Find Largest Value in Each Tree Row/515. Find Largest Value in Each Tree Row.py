'''
Idea: Perform BFS. At each level find the maximum and add it to the result array.

Time complexity : O(n)      (Visiting all the nodes exactly once)
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
    def largestValues(self, root):
        if not root:
            return []
        q = collections.deque()
        res = []
        q += root,
        while q:
            size = len(q)
            curr_level = float('-inf')
            for _ in range(size):
                node = q.popleft()
                curr_level = max(curr_level, node.val)
                if node.left:   q += node.left,
                if node.right:  q += node.right,
            res += curr_level,
        return res
        