import collections

class Solution:
    def eventualSafeNodes(self, graph):
        # 3 color problem: 0. Unvisited 1. Processing 2. Processed
        
        def dfs(node):
            if visited[node]!=0:
                return visited[node]==2
            visited[node] = 1
            for nei in graph[node]:
                if visited[nei]==1:
                    return False
                elif visited[nei]==0 and not dfs(nei):
                    return False
            
            visited[node] = 2
            return True
        
        n = len(graph)
        visited = [0] * n
        res = []
        for i in range(n):
            if dfs(i):
                res += i,
        
        return res