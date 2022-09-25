# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        bfs = collections.deque([root])
        ct = 0
        while bfs:
            node = bfs.popleft()
            ct+=1
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        
        return ct