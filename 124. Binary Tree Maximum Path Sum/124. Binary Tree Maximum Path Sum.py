'''
Time complexity: O(n)
Space complexity: O(1)
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        self.res = float('-inf')
        
        def util(root):
            if not root:
                return 0
            
            left = util(root.left)
            right = util(root.right)
            
            '''
            Path can either look like        /    or  /     not like       /
                                         -> /     -> /                 -> /
                                           /         \                   / \
            
            So atmost one child can participate when parent of node is participating
            '''
            
            # parent_path -> parent of node is interested in participating
            # atmost one child of current node can participate - why ???
            parent_path = max(root.val, root.val + max(left, right))
            
            # node_path -> parent of root does not show interest
            # so consider both the child of current node
            node_path = root.val + left + right
            
            self.res = max(self.res, node_path, parent_path)  # update result
            
            return parent_path  # allow parent to get its result
            
        util(root)
        return self.res
        