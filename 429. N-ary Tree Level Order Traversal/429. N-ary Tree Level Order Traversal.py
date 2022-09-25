import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = collections.deque([root])
        res = []
        while q:
            size = len(q)
            temp = []
            for _ in range(size):
                node = q.popleft()
                temp += node.val,
                for nei in node.children:
                    q.append(nei)
            res.append(temp)
        return res