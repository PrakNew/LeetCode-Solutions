#Best question for DFS,BFS and backtracking
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        path = dict(zip(list(range(n)),graph))
        print(path)
        self.final=[]
        def dfs(node,l):
            if node==(n-1):
                self.final.append(l)
                return 
            for x in path[node]:
                dfs(x,list(l)+[x])
        dfs(0,[0])
        return self.final
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
                