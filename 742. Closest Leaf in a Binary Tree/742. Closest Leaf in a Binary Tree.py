'''
Idea: Construct a graph out of tree and do BFS to find closest leaf node

Time complexity : O(n)
Space complexity: O(n)

'''

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root, target):
        graph = collections.defaultdict(list)
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.val == target:
                targetNode = node
            if node.left:
                q.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                q.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)
        
        q = collections.deque([(targetNode)])
        visited = set([targetNode])
        while q:
            node = q.popleft()
            if not node.left and not node.right:
                return node.val 
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        