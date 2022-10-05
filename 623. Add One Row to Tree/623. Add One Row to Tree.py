# recursive approach to add an element just after the depth is reached 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        head=root
        if depth==1:
            t1=TreeNode(val=val)
            t1.left=root
            return t1
        def check(root,d):
            if root.left is None and root.right is None:
                if d==(depth-1):
                    t1=TreeNode(val=val)
                    t2=TreeNode(val=val)
                    root.left=t1
                    root.right=t2
                return 
            if d==(depth-1):
                t1=TreeNode(val=val)
                t1.left=root.left
                t2=TreeNode(val=val)
                t2.right=root.right
                root.left=t1
                root.right=t2
                return 
            if root.left:check(root.left,d+1)
            if root.right:check(root.right,d+1)
        check(root,1)
        return head