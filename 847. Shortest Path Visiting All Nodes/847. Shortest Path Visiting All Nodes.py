"""
Idea: BFS on state of each node

Time complexity : O(2^N * N)
Space complexity: O(2^N * N)
"""

import collections

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        q = collections.deque()
        dist = collections.defaultdict(lambda: float('inf'))       # initial values are inf
        
        for x in range(n):
            q += (1 << x, x),
            dist[1 << x, x] = 0
            
        while q:
            
            cover, head = q.popleft()
            d = dist[cover, head]
            
            if cover == 2**n-1:
                return d
            
            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2, child]:
                    dist[cover2, child] = d + 1
                    q += (cover2, child),
        
        