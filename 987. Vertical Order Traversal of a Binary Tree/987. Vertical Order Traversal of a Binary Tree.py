import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root):
        mp = collections.defaultdict(lambda : collections.defaultdict(list))
        q = collections.deque([(root, 0, 0)])
        while q:
            node, x, y = q.popleft()
            mp[y][x] += node.val,
            if node.left:
                q.append((node.left, x+1, y-1))
            if node.right:
                q.append((node.right, x+1, y+1))
        
        res = []
        for depth in sorted(mp):
            layer = []
            for level in mp[depth]: # elements in same depth and level need to be sorted
                layer += sorted(mp[depth][level])
            res.append(layer)
        return res
        