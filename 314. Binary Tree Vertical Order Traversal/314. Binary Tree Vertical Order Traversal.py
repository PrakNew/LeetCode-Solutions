"""
Idea: Use hashmaps to store the nodes in the tree and sort them by columns

Time complexity: O(n log n)
Space complexity: O(n)
"""

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        mp = collections.defaultdict(list)
        q = collections.deque([(root, 0, 0)])
        
        while q:
            node, x, y = q.popleft()
            mp[y, x] += node.val,
            if node.left:
                q += (node.left, x + 1, y - 1),
            if node.right:
                q += (node.right, x + 1, y + 1),
                
        res = []
        prev = None
        
        for key in sorted(mp):
            if prev == key[0]:
                res[-1] += mp[key]
            else:
                res += mp[key],
            prev = key[0]
                
        
        return res