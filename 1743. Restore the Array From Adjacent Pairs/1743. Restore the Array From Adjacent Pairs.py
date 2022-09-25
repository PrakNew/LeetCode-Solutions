"""
Idea: DFS

Time complexity: O(E + V)
Space complexity: O(E + V)
"""

import collections


class Solution:
    def restoreArray(self, adjacentPairs):
        graph = collections.defaultdict(list)
        ends = []
        
        for a, b in adjacentPairs:
            graph[a] += b,
            graph[b] += a,
        
        for node in graph:
            if len(graph[node]) == 1:
                ends += node,
        
        n = len(graph)
        
        res = [None] * n
        
        res[0] = ends[0]
        res[-1] = ends[1]
        
        visited = set([*ends])
        q = collections.deque([(ends[0], 0)])
        
        while q:
            node, ind = q.pop()
            if res[ind] == None:
                res[ind] = node 
                
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q += (nei, ind + 1),
        
        return res
        
        
        