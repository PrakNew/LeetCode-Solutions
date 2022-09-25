'''
Time complexity : O(n)
Space complexity: O(n)
'''

import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        q = collections.deque([(root, 1)])
        res = 0
        while q:
            node, depth = q.popleft()
            res = depth if depth > res else res
            for childNode in node.children:
                q.append((childNode, depth+1))
        return res