'''
Idea: Choose the next highest element. It can be found in either of two places:
      1. Left most child of right subtree
      2. One of the ancestors of current node

Time complexity : O(logN)
Space complexity: O(1)
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node):
        # If right child exists
        if node.right:
            temp = node.right
            while temp.left:
                temp = temp.left
            return temp 
        # If no right child exists
        else:
            temp = node.parent
            while temp and temp.val < node.val:
                temp = temp.parent
            return temp