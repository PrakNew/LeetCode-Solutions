import collections

class Solution:
    def findMinHeightTrees(self, n, edges):
        # Iteratively find the leaf nodes and remove them from tree
        # Repeat until there are more than 2 nodes left
        
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        
        if n==1:
            return [0]
        
        for u, v in edges:
            graph[u] += v,
            graph[v] += u,
            degree[u] += 1
            degree[v] += 1
        
        q = collections.deque([leaf for leaf in graph if degree[leaf]==1])
        remaining_nodes = n
        
        while remaining_nodes > 2:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei]==1:
                        q.append(nei)
            remaining_nodes -= size
        
        return q
            
        
        
        