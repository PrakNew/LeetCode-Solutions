class Solution:
    
    def topologicalSortUtil(self, i, visited, stack):
        visited[i] = True
        for nei in self.graph[i]:
            if not visited[nei]:
                self.topologicalSortUtil(nei, visited, stack)
        stack.insert(0, i)
        
    
    def topologicalSort(self, n):
        visited = [False] * self.V
        stack = []
        
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        
        return stack
    
    def isCyclicUtil(self, node, visited, recStack):
        visited[node] = True
        recStack[node] = True
        
        for nei in self.graph[node]:
            if not visited[nei]:
                if self.isCyclicUtil(nei, visited, recStack):
                    return True
            elif recStack[nei]:
                return True
        
        # Backtrack
        recStack[node] = False
        return False
    
    
    def isCyclic(self):
        recStack = [False] * self.V
        visited = [False] * self.V
        
        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicUtil(i, visited, recStack):
                    return True
        return False
                
    
    def findOrder(self, n, courses):
        self.V = n
        self.graph = collections.defaultdict(list)
        for u, v in courses:
            self.graph[v].append(u)
        
        if self.isCyclic():
            return []
        
        return self.topologicalSort(n)
        