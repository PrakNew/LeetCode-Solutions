class Solution:
    def allPathsSourceTarget(self, graph):
               
        n = len(graph)
        
        def dfs(node, path, res):
            if node==n-1:
                res.append(path+[node])
            
            for nei in graph[node]:
                dfs(nei, path + [node], res)
        
        res = []
        dfs(0, [], res)
        return res
                