
#created recursion function to call simply

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.c=0
        def check(root,s):
            if root.left is None and root.right is None:
                s+=str(root.val)
                self.c+=int(s)
            s+=str(root.val)
            if root.left:check(root.left,s)
            if root.right:check(root.right,s)

        check(root,'')
        return self.c



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
                           
        