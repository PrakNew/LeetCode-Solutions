from collections import defaultdict

class Solution:

    def util(self, i, visited, recStack):
        visited[i] = True
        recStack[i] = True
        
        for j in self.graph[i]:
            if not visited[j]:
                if self.util(j, visited, recStack):
                    return True
            elif recStack[j]:
                return True
        
        recStack[i] = False
        return False
    
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        
        for i in range(self.V):
            if not visited[i]:
                if self.util(i, visited, recStack):
                    return True
        
        return False
    
    def canFinish(self, numCourses, prerequisites):
        
        self.V = numCourses
        self.graph = defaultdict(list)
        
        for edge in prerequisites:
            u, v = edge
            self.graph[u].append(v)
        
        return not self.isCyclic()