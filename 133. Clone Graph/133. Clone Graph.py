"""
Idea: Do tree traversal and keep creating nodes and their respective links, if they are not present in hash table.


Time complexity : O(n)
Space complexity: O(n)

"""


import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        dic = collections.defaultdict(Node)
        nodeCopy = Node(node.val)
        dic[node] = nodeCopy
        q = collections.deque([node])
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors += neighborCopy,
                    q += neighbor,
                else:
                    dic[node].neighbors += dic[neighbor],
                    
        return nodeCopy