import collections

class Solution: 
            
    def checkIfPrerequisite(self, n, prerequisites, queries):
        
        graph = collections.defaultdict(list)
        
        if prerequisites == []:
            return [False] * len(queries)
        
        for u, v in prerequisites:
            graph[u].append(v)
        
        def topologicalSortUtil( i, visited, stack):
            visited[i] = True

            for nei in graph[i]:
                if not visited[nei]:
                    topologicalSortUtil(nei, visited, stack)

            stack.insert(0, i)
        
        res = []
        
        for u, v in queries:
            visited = [False] * n
            stack = list()
            
            topologicalSortUtil(u, visited, stack)
            
            if u in stack and v in stack:
                res.append(stack.index(u) < stack.index(v))
            else:
                res.append(False)
            
        
        return res
        