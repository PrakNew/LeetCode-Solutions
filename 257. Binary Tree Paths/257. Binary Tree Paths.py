'''
Time complexity : O(n)
Space complexity: O(n)
'''
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.l=[]
        def check(root,s):
            if not root.left and not root.right:
                s+=str(root.val)
                self.l.append(s)
            s += f'{str(root.val)}->'
            if root.left:check(root.left,s)
            if root.right:check(root.right,s)

        check(root,'')
        return self.l

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        def recursive():
            if not root:
                return []
            def util(node, path, res):
                if not node.left and not node.right: # leaf node
                    res.append("->".join(path))
                    return
                if node.left:
                    util(node.left, path + [str(node.left.val)], res)
                if node.right:
                    util(node.right, path + [str(node.right.val)], res)

            res = []
            util(root, [str(root.val)], res)
            return res

        def iterative():
            if not root:
                return []
            res = []
            q = collections.deque([(root, [str(root.val)])])
            while q:
                node, path = q.popleft()
                if not node.left and not node.right: # leaf node
                    res.append("->".join(path))
                    continue
                if node.left: q.append((node.left, path + [str(node.left.val)]))
                if node.right: q.append((node.right, path + [str(node.right.val)]))
            return res

        return recursive()