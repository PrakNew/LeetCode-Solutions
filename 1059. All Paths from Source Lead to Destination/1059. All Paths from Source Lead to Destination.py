import collections

class Solution:
    def leadsToDestination(self, n, edges, source, destination):
        # 3 color problem
        # 0 - unprocessed
        # 1 - processing
        # 2 - processed
        
        if not edges:
            return True
        
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
        
        
        visited = [0] * n 

        
        def dfs(node):
            if node not in graph: # leaf node 
                return node == destination
            
            visited[node] = 1
            
            for nei in graph[node]:
                if visited[nei]==1: # cycle detected
                    return False
                elif visited[nei]==0 and not dfs(nei):
                    return False
            
            visited[node] = 2
            return True
            
        return dfs(source)
      
            
        