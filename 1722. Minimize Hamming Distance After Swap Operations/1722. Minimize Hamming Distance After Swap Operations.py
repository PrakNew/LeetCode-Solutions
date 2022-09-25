"""
Idea: DFS and find groups. Count the difference in source and target
"""

import collections

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        
        n = len(source)

        if len(allowedSwaps) == 0:
            res = 0
            for i in range(n):
                if source[i] != target[i]:
                    res += 1
            
            return res
        
        
        graph = collections.defaultdict(list)
        
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, visited, group):
            visited.add(node)
            group.append(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited, group)
        
        res = n
        visited = set()
        for i in range(n):
            if i not in visited:
                group = []
                dfs(i, visited, group)
                
                mp1 = collections.Counter(source[j] for j in group)
                mp2 = collections.Counter(target[j] for j in group)
                
                res -= sum((mp1 & mp2).values())
        
        return res
        
        