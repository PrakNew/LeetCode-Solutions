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
            return []
        q = collections.deque([(root, [root.val], root.val)])
        res = []
        while q:
            node, path, curr_sum = q.pop()
            if curr_sum == target and not node.left and not node.right: # leaf node with given sum
                res.append(path)
                continue
            if node.left:
                q.append((node.left, path + [node.left.val], curr_sum + node.left.val))
            if node.right:
                q.append((node.right, path + [node.right.val], curr_sum + node.right.val))
        
        return res