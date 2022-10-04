# I have used the method of recursion and there is second method using tabulization given below
from collections import defaultdict
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.d=defaultdict(lambda : [])
        def check(root,c,height):
            if root.left is None and root.right is None:
                if c==1:
                    self.d[height]+=[root.val]
                else:
                    self.d[height]=[root.val]+self.d[height]
            if c==1:
                self.d[height]+=[root.val]
            else:
                self.d[height]=[root.val]+self.d[height]
            if root.left:check(root.left,(c+1)%2,height+1)
            if root.right:check(root.right,(c+1)%2,height+1)

        check(root,1,0)
        for x in self.d:
            print(list((self.d[x])))


import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, target):
        if not root:
            return False
        q = collections.deque([(root, root.val)])
        while q:
            node, val = q.popleft()
            if val==target and not node.left and not node.right: # leaf node sum
                return True
            if node.left:
                q.append((node.left, val + node.left.val))
            if node.right:
                q.append((node.right, val + node.right.val))
        return False
        