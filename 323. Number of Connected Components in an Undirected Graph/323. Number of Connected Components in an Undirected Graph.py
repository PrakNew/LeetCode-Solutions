import collections

class Solution:
    def countComponents(self, n, edges):

        def dfs(node):
            visited[node] = True 
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        components = 0
        visited = [False] * n 

        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
            
        return components
        