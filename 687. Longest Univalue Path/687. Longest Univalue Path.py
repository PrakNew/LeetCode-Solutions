'''
Time complexity : O(n)
Space complexity: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root):
        self.ans = 0
        
        def util(node):
            if not node:
                return 0
            left_len = util(node.left)
            right_len = util(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.val == node.left.val:
                left_arrow = 1 + left_len
            if node.right and node.val == node.right.val:
                right_arrow = 1 + right_len
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)
        util(root)
        return self.ans
        