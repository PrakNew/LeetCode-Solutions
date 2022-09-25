import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root):
        left_boundary = []
        right_boundary = []
        leaves = []
        
        def leftChildFlag(curr, flag):
            if flag in [0, 1]: # root child
                return 1
            elif flag==2 and not curr.right: 
                return 2
            return 3
        
        def rightChildFlag(curr, flag):
            if flag in [0, 2]:
                return 2
            elif flag==1 and not curr.left:
                return 1
            return 3
        
        def preorder(node, flag):
            if node:
                if flag==0 or flag==1:
                    left_boundary.append(node.val)
                elif flag==2:
                    right_boundary.append(node.val)
                elif not node.left and not node.right:
                    leaves.append(node.val)
            
                preorder(node.left, leftChildFlag(node, flag))
                preorder(node.right, rightChildFlag(node, flag))
            
        
        preorder(root, 0)
        return left_boundary + leaves + right_boundary[::-1]