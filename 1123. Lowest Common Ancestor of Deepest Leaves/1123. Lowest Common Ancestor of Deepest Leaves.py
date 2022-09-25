import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root):
        
        def LCA(node, p, q):
            if not node or node==p or node==q:
                return node
            left = LCA(node.left, p, q)
            right = LCA(node.right, p, q)
            
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None
            
        
        if not root:
            return root
        
        deepest = collections.defaultdict(list)
        maxdepth = float('-inf')
        
        q = collections.deque([(root, 0)])
        while q:
            node, depth = q.popleft()
            maxdepth = max(maxdepth, depth)
            deepest[depth].append(node)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        
        if len(deepest[maxdepth])==1:
            return deepest[maxdepth][0]
        
        return LCA(root, deepest[maxdepth][0], deepest[maxdepth][-1])
        
            