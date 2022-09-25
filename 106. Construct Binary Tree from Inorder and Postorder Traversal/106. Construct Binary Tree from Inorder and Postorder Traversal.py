'''
Idea: Make use of postorder to find the root and use the index of root from inorder to fetch
        range of left and right subtrees.

Time complexity : O(N)
Space complexity: O(N)

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        # inorder  : Left, .... Node, .... Right
        # postorder: Left, .... Right, .... Node
        
        inorder_index = {val:ind for ind, val in enumerate(inorder)}
        
        def recur(left, right):
            if left > right:
                return None
            root = TreeNode(postorder.pop())
            root_index = inorder_index[root.val]
            root.right = recur(root_index+1, right)
            root.left = recur(left, root_index-1)
            return root
        
        return recur(0, len(inorder)-1)