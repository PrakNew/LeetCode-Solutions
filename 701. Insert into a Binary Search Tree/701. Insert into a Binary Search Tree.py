'''
Idea: Keep searching for the value to be inserted in the BST. Once a null is reached, insert the new node here.

Time complexity : O(log N) or O(h) , where h is the height of the BST
Space complexity: O(1)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root, key):
        if not root:
            root = TreeNode(key)
        elif root.val < key:
            root.right = self.insertIntoBST(root.right, key)
        else:
            root.left = self.insertIntoBST(root.left, key)
        
        return root