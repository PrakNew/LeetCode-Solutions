import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0 
        
        bfs = collections.deque([(root, root.val)])
        total_sum = 0
        
        while bfs:
            node, curr_sum = bfs.popleft()
            if not node.left and not node.right: # leaf node
                total_sum += curr_sum
            
            if node.left:
                bfs.append((node.left, curr_sum*10 + node.left.val))
            
            if node.right:
                bfs.append((node.right, curr_sum*10 + node.right.val))
        
        return total_sum
                           
        