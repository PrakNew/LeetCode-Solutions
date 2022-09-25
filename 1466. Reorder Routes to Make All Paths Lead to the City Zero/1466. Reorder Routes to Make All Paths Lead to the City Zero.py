import collections

class Solution:
    def minReorder(self, n, connections):
        graph = collections.defaultdict(list)
        
        for a, b in connections:
            graph[a].append(b)
        
        visited = [False] * n
        visited[0] = True
        res = 0
        
        for i in range(n):
            for city in graph[i]:
                if not visited[city]:
                    res+=1
                    visited[city] = True
                elif visited[city]:
                    visited[i] = True

        return res
        
            