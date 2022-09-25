'''
Idea: Traverse through the binary tree to find the key. On reaching the key, find its inorder successor 
      and replace it with new value. Delete the inorder successor.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMinimum(self, root):
        while root and root.left:
            root = root.left
        return root
        
    def deleteNode(self, root, key):
        
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # only one child
            if not root.left:
                next_node = root.right
                root = None
                return next_node
            
            if not root.right:
                next_node = root.left
                root = None
                return next_node
            
            # two childen
            new_node = self.findMinimum(root.right)
            root.val = new_node.val 
            root.right = self.deleteNode(root.right, new_node.val)
        
        return root
        