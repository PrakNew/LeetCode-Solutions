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