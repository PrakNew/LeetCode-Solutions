'''
Idea : This is similar to Subarray sum equals K. Here there are multiple arrays along the depth
        of the trees, so carry out similar process for all the arrays.

Time complexity: O(n)
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
    def pathSum(self, root, target):
        if not root:
            return 0
        q = collections.deque([(root, root.val, {0: 1})])
        res = 0
        while q:
            node, curr_sum, mp = q.popleft()
            res += mp.get(curr_sum - target, 0)
            new_mp = {curr_sum: mp.get(curr_sum, 0) + 1}
            if node.left:
                q.append((node.left, curr_sum + node.left.val, {**mp, **new_mp}))
            if node.right:
                q.append((node.right, curr_sum + node.right.val, {**mp, **new_mp}))
        return res
        
        